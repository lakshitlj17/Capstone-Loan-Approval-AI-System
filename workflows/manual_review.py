"""
Manual review workflow for borderline cases.
Handles escalation and review queue management.
"""
from typing import Dict, Any, List
from enum import Enum
from datetime import datetime
import uuid

class ReviewPriority(Enum):
    """Priority levels for manual review."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class ReviewStatus(Enum):
    """Status of a review case."""
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    ESCALATED = "ESCALATED"

class ManualReviewCase:
    """Represents a case pending manual review."""

    def __init__(
        self,
        application_id: str,
        decision: str,
        confidence: float,
        reason: str,
        application_data: Dict[str, Any],
        recommendation: str
    ):
        self.review_id = f"REV-{uuid.uuid4().hex[:8].upper()}"
        self.application_id = application_id
        self.decision = decision
        self.confidence = confidence
        self.reason = reason
        self.application_data = application_data
        self.recommendation = recommendation
        self.status = ReviewStatus.PENDING
        self.created_at = datetime.utcnow()
        self.assigned_to = None
        self.reviewed_at = None
        self.review_notes = ""
        self.final_decision = None

        if confidence < 50:
            self.priority = ReviewPriority.CRITICAL
        elif confidence < 65:
            self.priority = ReviewPriority.HIGH
        elif confidence < 80:
            self.priority = ReviewPriority.MEDIUM
        else:
            self.priority = ReviewPriority.LOW

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "review_id": self.review_id,
            "application_id": self.application_id,
            "decision": self.decision,
            "confidence": self.confidence,
            "reason": self.reason,
            "priority": self.priority.name,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "assigned_to": self.assigned_to,
            "recommendation": self.recommendation,
            "final_decision": self.final_decision
        }

class ManualReviewQueue:
    """Manages the queue of applications pending manual review."""

    def __init__(self):
        self.queue: Dict[str, ManualReviewCase] = {}
        self.completed_reviews: List[ManualReviewCase] = []

    def add_case(
        self,
        application_id: str,
        decision: str,
        confidence: float,
        reason: str,
        application_data: Dict[str, Any],
        recommendation: str = ""
    ) -> ManualReviewCase:
        """Add a new case to the review queue."""
        case = ManualReviewCase(
            application_id=application_id,
            decision=decision,
            confidence=confidence,
            reason=reason,
            application_data=application_data,
            recommendation=recommendation
        )
        self.queue[case.review_id] = case
        return case

    def get_next_case(self) -> ManualReviewCase:
        """Get next case to review (highest priority first)."""
        pending_cases = [c for c in self.queue.values() if c.status == ReviewStatus.PENDING]

        if not pending_cases:
            return None

        pending_cases.sort(
            key=lambda x: (-x.priority.value, x.created_at)
        )

        return pending_cases[0]

    def assign_case(self, review_id: str, assigned_to: str) -> bool:
        """Assign a case to a reviewer."""
        if review_id not in self.queue:
            return False

        case = self.queue[review_id]
        case.assigned_to = assigned_to
        case.status = ReviewStatus.IN_PROGRESS
        return True

    def complete_review(
        self,
        review_id: str,
        final_decision: str,
        notes: str = ""
    ) -> bool:
        """Mark a review as complete."""
        if review_id not in self.queue:
            return False

        case = self.queue[review_id]
        case.final_decision = final_decision
        case.review_notes = notes
        case.reviewed_at = datetime.utcnow()
        case.status = ReviewStatus.APPROVED if final_decision in ["APPROVED", "REJECTED"] else ReviewStatus.ESCALATED

        self.completed_reviews.append(case)
        del self.queue[review_id]

        return True

    def get_queue_status(self) -> Dict[str, Any]:
        """Get overall queue status."""
        pending = [c for c in self.queue.values() if c.status == ReviewStatus.PENDING]
        in_progress = [c for c in self.queue.values() if c.status == ReviewStatus.IN_PROGRESS]

        return {
            "total_pending": len(pending),
            "total_in_progress": len(in_progress),
            "total_completed": len(self.completed_reviews),
            "average_priority": sum(c.priority.value for c in pending) / len(pending) if pending else 0,
            "pending_cases": [c.to_dict() for c in pending],
            "in_progress_cases": [c.to_dict() for c in in_progress]
        }

    def get_case_by_application_id(self, application_id: str) -> ManualReviewCase:
        """Find case by application ID."""
        for case in self.queue.values():
            if case.application_id == application_id:
                return case
        return None

_review_queue = None

def get_review_queue() -> ManualReviewQueue:
    """Get or create global review queue."""
    global _review_queue
    if _review_queue is None:
        _review_queue = ManualReviewQueue()
    return _review_queue

def should_escalate_to_manual_review(decision_result: Dict[str, Any]) -> bool:
    """Determine if a case should be escalated to manual review."""
    decision = decision_result.get("decision", "REVIEW")
    confidence = decision_result.get("confidence", 0)
    anomalies = decision_result.get("anomalies_detected", [])

    if decision == "REVIEW":
        return True

    if confidence < 75 and decision in ["APPROVED", "REJECTED"]:
        return True

    if anomalies and len(anomalies) > 1:
        return True

    return False

def get_escalation_reason(decision_result: Dict[str, Any]) -> str:
    """Generate reason for manual review escalation."""
    decision = decision_result.get("decision", "UNKNOWN")
    confidence = decision_result.get("confidence", 0)
    anomalies = decision_result.get("anomalies_detected", [])

    reasons = []

    if decision == "REVIEW":
        reasons.append("Decision requires manual review")

    if confidence < 75:
        reasons.append(f"Low confidence decision ({confidence:.0f}%)")

    if anomalies:
        reasons.append(f"Anomalies detected: {', '.join(anomalies)}")

    return " | ".join(reasons) if reasons else "Manual review required"
