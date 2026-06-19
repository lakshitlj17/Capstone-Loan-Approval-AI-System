"""
Audit logging for compliance and decision tracking.
Records all decisions and reasoning for regulatory compliance.
"""
import json
import os
from datetime import datetime
from typing import Any, Dict, List
import uuid

class AuditLogger:
    """Centralized audit trail management."""

    def __init__(self, log_dir: str = "audit_logs"):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)

    def log_application(self, application_id: str, application_data: Dict[str, Any]) -> None:
        """Log incoming application."""
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": "APPLICATION_RECEIVED",
            "application_id": application_id,
            "data": application_data
        }
        self._write_entry(application_id, entry)

    def log_agent_execution(
        self,
        application_id: str,
        agent_name: str,
        input_data: Dict[str, Any],
        output_data: Dict[str, Any],
        reasoning: str = ""
    ) -> None:
        """Log agent execution with reasoning."""
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": "AGENT_EXECUTION",
            "agent": agent_name,
            "input_summary": self._truncate_summary(input_data),
            "output": output_data,
            "reasoning": reasoning
        }
        self._write_entry(application_id, entry)

    def log_decision(
        self,
        application_id: str,
        decision: str,
        confidence: float,
        reasoning: str,
        factors: List[Dict[str, Any]]
    ) -> None:
        """Log final decision with confidence and factors."""
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": "DECISION_MADE",
            "decision": decision,
            "confidence": confidence,
            "reasoning": reasoning,
            "decision_factors": factors
        }
        self._write_entry(application_id, entry)

    def log_compliance_check(
        self,
        application_id: str,
        checks_passed: List[str],
        checks_failed: List[str],
        case_id: str
    ) -> None:
        """Log compliance validation results."""
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": "COMPLIANCE_CHECK",
            "case_id": case_id,
            "checks_passed": checks_passed,
            "checks_failed": checks_failed,
            "status": "PASSED" if not checks_failed else "FAILED_REVIEW"
        }
        self._write_entry(application_id, entry)

    def log_manual_review_escalation(
        self,
        application_id: str,
        reason: str,
        confidence: float
    ) -> None:
        """Log escalation to manual review."""
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": "MANUAL_REVIEW_ESCALATION",
            "reason": reason,
            "confidence": confidence,
            "status": "ESCALATED"
        }
        self._write_entry(application_id, entry)

    def get_audit_trail(self, application_id: str) -> List[Dict[str, Any]]:
        """Retrieve complete audit trail for an application."""
        log_file = os.path.join(self.log_dir, f"{application_id}.jsonl")
        entries = []

        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                for line in f:
                    if line.strip():
                        entries.append(json.loads(line))

        return entries

    def generate_compliance_report(self, application_id: str) -> Dict[str, Any]:
        """Generate compliance report from audit trail."""
        audit_trail = self.get_audit_trail(application_id)

        decision_entry = next((e for e in audit_trail if e.get("event") == "DECISION_MADE"), None)
        compliance_entry = next((e for e in audit_trail if e.get("event") == "COMPLIANCE_CHECK"), None)

        report = {
            "application_id": application_id,
            "generated_at": datetime.utcnow().isoformat(),
            "final_decision": decision_entry.get("decision", "PENDING") if decision_entry else "PENDING",
            "decision_confidence": decision_entry.get("confidence", 0) if decision_entry else 0,
            "compliance_status": compliance_entry.get("status", "UNKNOWN") if compliance_entry else "UNKNOWN",
            "total_events": len(audit_trail),
            "audit_trail_summary": [
                {
                    "timestamp": e.get("timestamp"),
                    "event": e.get("event"),
                    "agent": e.get("agent", "N/A")
                }
                for e in audit_trail
            ]
        }

        return report

    def export_audit_trail(self, application_id: str, format: str = "json") -> str:
        """Export audit trail in specified format."""
        audit_trail = self.get_audit_trail(application_id)

        if format == "json":
            return json.dumps(audit_trail, indent=2)
        elif format == "csv":
            import csv
            from io import StringIO

            output = StringIO()
            if not audit_trail:
                return ""

            writer = csv.DictWriter(output, fieldnames=audit_trail[0].keys())
            writer.writeheader()
            writer.writerows(audit_trail)
            return output.getvalue()

        return json.dumps(audit_trail, indent=2)

    def _write_entry(self, application_id: str, entry: Dict[str, Any]) -> None:
        """Write audit entry to log file."""
        log_file = os.path.join(self.log_dir, f"{application_id}.jsonl")
        with open(log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")

    @staticmethod
    def _truncate_summary(data: Any, max_length: int = 100) -> str:
        """Create truncated summary of data."""
        summary = str(data)[:max_length]
        if len(str(data)) > max_length:
            summary += "..."
        return summary

_audit_logger = None

def get_audit_logger() -> AuditLogger:
    """Get or create global audit logger."""
    global _audit_logger
    if _audit_logger is None:
        _audit_logger = AuditLogger()
    return _audit_logger

def generate_application_id() -> str:
    """Generate unique application ID."""
    return f"LOAN-{uuid.uuid4().hex[:12].upper()}"
