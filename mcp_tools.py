"""
MCP Tool definitions for agent communication.
Defines standardized schemas and tool signatures for agent interoperability.
"""
from typing import Any, Dict

# Tool schemas for MCP protocol
PROFILE_AGENT_TOOL = {
    "name": "profile_analysis",
    "description": "Analyze applicant profile for income stability, employment risk, and application completeness",
    "inputSchema": {
        "type": "object",
        "properties": {
            "age": {
                "type": "integer",
                "description": "Applicant's age"
            },
            "income": {
                "type": "number",
                "description": "Annual income in dollars"
            },
            "employment": {
                "type": "string",
                "enum": ["Full-time", "Self-employed"],
                "description": "Employment type"
            },
            "credit_score": {
                "type": "integer",
                "description": "Credit score (300-850)"
            }
        },
        "required": ["age", "income", "employment"]
    }
}

RISK_ANALYSIS_TOOL = {
    "name": "risk_analysis",
    "description": "Assess financial risk using multi-factor scoring and anomaly detection",
    "inputSchema": {
        "type": "object",
        "properties": {
            "income": {
                "type": "number",
                "description": "Annual income in dollars"
            },
            "loan_amount": {
                "type": "number",
                "description": "Requested loan amount in dollars"
            },
            "employment_risk": {
                "type": "string",
                "enum": ["Low", "Medium", "High"],
                "description": "Employment risk level from profile analysis"
            },
            "credit_profile": {
                "type": "string",
                "enum": ["Excellent", "Good", "Fair", "Poor"],
                "description": "Credit profile classification from profile analysis"
            }
        },
        "required": ["income", "loan_amount"]
    }
}

DECISION_MAKING_TOOL = {
    "name": "loan_decision",
    "description": "Make loan approval/rejection/review decision with confidence and reasoning",
    "inputSchema": {
        "type": "object",
        "properties": {
            "profile": {
                "type": "object",
                "description": "Profile analysis output from profile_agent",
                "properties": {
                    "income_stability": {"type": "string"},
                    "employment_risk": {"type": "string"},
                    "credit_profile": {"type": "string"},
                    "application_completeness": {"type": "string"},
                    "profile_score": {"type": "number"}
                }
            },
            "risk": {
                "type": "object",
                "description": "Risk analysis output from risk_agent",
                "properties": {
                    "dti": {"type": "number"},
                    "lti": {"type": "number"},
                    "risk_score": {"type": "number"},
                    "risk_level": {"type": "string"},
                    "anomalies_detected": {"type": "array"}
                }
            }
        },
        "required": ["profile", "risk"]
    }
}

COMPLIANCE_FINALIZATION_TOOL = {
    "name": "compliance_finalization",
    "description": "Finalize decision with audit trail, case ID, and compliance status",
    "inputSchema": {
        "type": "object",
        "properties": {
            "decision_result": {
                "type": "object",
                "description": "Decision result from decision_agent",
                "properties": {
                    "decision": {"type": "string"},
                    "confidence": {"type": "number"},
                    "reasoning": {"type": "string"},
                    "risk_summary": {"type": "string"},
                    "decision_factors": {"type": "array"}
                }
            }
        },
        "required": ["decision_result"]
    }
}

# Tool wrapper signatures for MCP client
class MCPToolWrapper:
    """Wraps agents as MCP-compliant tools."""

    @staticmethod
    def profile_analysis(data: Dict[str, Any]) -> Dict[str, Any]:
        """Call profile agent via MCP protocol."""
        from Agents.profile_agent import profile_agent
        return profile_agent(data)

    @staticmethod
    def risk_analysis(data: Dict[str, Any]) -> Dict[str, Any]:
        """Call risk agent via MCP protocol."""
        from Agents.risk_agent import risk_agent
        return risk_agent(data)

    @staticmethod
    def loan_decision(data: Dict[str, Any]) -> Dict[str, Any]:
        """Call decision agent via MCP protocol."""
        from Agents.decision_agent import decision_agent
        profile = data.get("profile", {})
        risk = data.get("risk", {})
        return decision_agent(profile, risk)

    @staticmethod
    def compliance_finalization(data: Dict[str, Any]) -> Dict[str, Any]:
        """Call compliance agent via MCP protocol."""
        from Agents.compliance_agent import compliance_agent
        decision_result = data.get("decision_result", {})
        return compliance_agent(decision_result)

# MCP Tool Registry
MCP_TOOLS = {
    "profile_analysis": {
        "schema": PROFILE_AGENT_TOOL,
        "handler": MCPToolWrapper.profile_analysis
    },
    "risk_analysis": {
        "schema": RISK_ANALYSIS_TOOL,
        "handler": MCPToolWrapper.risk_analysis
    },
    "loan_decision": {
        "schema": DECISION_MAKING_TOOL,
        "handler": MCPToolWrapper.loan_decision
    },
    "compliance_finalization": {
        "schema": COMPLIANCE_FINALIZATION_TOOL,
        "handler": MCPToolWrapper.compliance_finalization
    }
}

def validate_tool_input(tool_name: str, input_data: Dict[str, Any]) -> bool:
    """Validate input against tool schema."""
    if tool_name not in MCP_TOOLS:
        return False
    schema = MCP_TOOLS[tool_name]["schema"]
    required_fields = schema["inputSchema"].get("required", [])
    for field in required_fields:
        if field not in input_data:
            return False
    return True

def call_mcp_tool(tool_name: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
    """Call an MCP tool with input validation."""
    if not validate_tool_input(tool_name, input_data):
        return {
            "status": "error",
            "error": f"Invalid input for tool '{tool_name}'"
        }

    if tool_name not in MCP_TOOLS:
        return {
            "status": "error",
            "error": f"Tool '{tool_name}' not found"
        }

    try:
        handler = MCP_TOOLS[tool_name]["handler"]
        result = handler(input_data)
        return {
            "status": "success",
            "tool": tool_name,
            "result": result
        }
    except Exception as e:
        return {
            "status": "error",
            "tool": tool_name,
            "error": str(e)
        }
