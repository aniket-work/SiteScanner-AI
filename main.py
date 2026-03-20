import os
import json
from typing import TypedDict, List, Dict, Annotated
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage
from simulation import SemiconductorSim

# Define the state for our meta-cognitive agent
class AgentState(TypedDict):
    telemetry: Dict
    analysis_depth: str
    insights: List[str]
    root_cause: str
    recommended_action: str
    reasoning_path: List[str]

class YieldArchAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)
        self.sim = SemiconductorSim()
        self._build_graph()

    def meta_cognitive_router(self, state: AgentState) -> str:
        """Decides the reasoning depth based on telemetry complexity."""
        sensors = state["telemetry"]["sensors"]
        # Logic to decide depth
        temp = sensors["temperature"]
        plasma = sensors["plasma_intensity"]
        
        if temp > 28.0 and plasma > 0.7:
            return "shallow_fix"
        elif 0.4 < plasma < 0.6:
            return "deep_diagnosis"
        else:
            return "moderate_analysis"

    def shallow_fix(self, state: AgentState) -> AgentState:
        """Level 1: Quick rule-based resolution for known patterns."""
        state["reasoning_path"].append("Level 1: Rule-based heuristic triggered.")
        state["analysis_depth"] = "Shallow"
        state["root_cause"] = "Standard Thermal Drift"
        state["recommended_action"] = "Recalibrate heat exchangers in station: " + state["telemetry"]["station"]
        return state

    def moderate_analysis(self, state: AgentState) -> AgentState:
        """Level 2: Statistical drift analysis."""
        state["reasoning_path"].append("Level 2: Statistical correlation analysis.")
        state["analysis_depth"] = "Moderate"
        state["root_cause"] = "Pressure Sub-assembly Instability"
        state["recommended_action"] = "Schedule preventive maintenance for pressure valves."
        return state

    def deep_diagnosis(self, state: AgentState) -> AgentState:
        """Level 3: Deep Meta-Cognitive Root Cause Analysis."""
        state["reasoning_path"].append("Level 3: Multi-modal Deep RCA triggered due to complex cross-sensor anomalies.")
        state["analysis_depth"] = "Deep"
        state["root_cause"] = "Chemical-Plasma Synergistic Imbalance affecting wafer deposition layer."
        state["recommended_action"] = "Immediate halt of line. Inspect gas delivery manifold and plasma chamber RF generator."
        return state

    def _build_graph(self):
        workflow = StateGraph(AgentState)
        
        workflow.add_node("shallow_fix", self.shallow_fix)
        workflow.add_node("moderate_analysis", self.moderate_analysis)
        workflow.add_node("deep_diagnosis", self.deep_diagnosis)
        
        workflow.set_conditional_entry_point(
            self.meta_cognitive_router,
            {
                "shallow_fix": "shallow_fix",
                "moderate_analysis": "moderate_analysis",
                "deep_diagnosis": "deep_diagnosis"
            }
        )
        
        workflow.add_edge("shallow_fix", END)
        workflow.add_edge("moderate_analysis", END)
        workflow.add_edge("deep_diagnosis", END)
        
        self.app = workflow.compile()

    def run(self):
        telemetry = self.sim.generate_telemetry()
        print(f"--- Incoming Telemetry from {telemetry['station']} ---")
        print(json.dumps(telemetry, indent=2))
        
        initial_state = {
            "telemetry": telemetry,
            "analysis_depth": "",
            "insights": [],
            "root_cause": "",
            "recommended_action": "",
            "reasoning_path": []
        }
        
        final_state = self.app.invoke(initial_state)
        
        print("\n--- YieldArch-AI Final Report ---")
        print(f"Depth: {final_state['analysis_depth']}")
        print(f"Reasoning Path: {' -> '.join(final_state['reasoning_path'])}")
        print(f"Root Cause: {final_state['root_cause']}")
        print(f"Action: {final_state['recommended_action']}")
        return final_state

if __name__ == "__main__":
    agent = YieldArchAgent()
    agent.run()
