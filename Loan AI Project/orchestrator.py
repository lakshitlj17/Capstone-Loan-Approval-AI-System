import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from langgraph.graph import StateGraph, START, END # pyright: ignore[reportMissingImports]
from typing import TypedDict

from Agents.profile_agent import profile_agent # pyright: ignore[reportMissingImports]
from Agents.risk_agent import risk_agent # pyright: ignore[reportMissingImports]
from Agents.decision_agent import decision_agent # pyright: ignore[reportMissingImports]
from Agents.compliance_agent import compliance_agent # pyright: ignore[reportMissingImports]

# ✅ STATE
class LoanState(TypedDict):
    input: dict
    profile: dict
    risk: dict
    decision: str
    final: dict

# ✅ NODES
def profile_node(state):
    return {"profile": profile_agent(state["input"])}

def risk_node(state):
    return {"risk": risk_agent(state["input"])}

def decision_node(state):
    return {"decision": decision_agent(state["profile"], state["risk"])}

def compliance_node(state):
    return {"final": compliance_agent(state["decision"])}

# ✅ GRAPH
builder = StateGraph(LoanState)

builder.add_node("profile", profile_node)
builder.add_node("risk", risk_node)
builder.add_node("decision", decision_node)
builder.add_node("compliance", compliance_node)

builder.add_edge(START, "profile")
builder.add_edge("profile", "risk")
builder.add_edge("risk", "decision")
builder.add_edge("decision", "compliance")
builder.add_edge("compliance", END)

graph = builder.compile()

# ✅ FUNCTION
def run_pipeline(data):
    return graph.invoke({
        "input": data,
        "profile": {},
        "risk": {},
        "decision": "",
        "final": {}
    })