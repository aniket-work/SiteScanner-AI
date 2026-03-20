import base64
import requests
import os

def generate_mermaid_diagrams():
    diagrams = {
        "title_diagram": """
graph TD
    A[Raw Sensor Data] --> B{Meta-Cognition}
    B -- Low Complexity --> C[Shallow Reasoning]
    B -- Medium Complexity --> D[Moderate Reasoning]
    B -- High Complexity --> E[Deep RCA]
    C --> F[Yield Report]
    D --> F
    E --> F
    style B fill:#f9f,stroke:#333,stroke-width:4px
    style E fill:#f66,stroke:#333,stroke-width:2px
""",
        "architecture_diagram": """
graph LR
    subgraph Edge
        S[Semiconductor Sensors] --> T[Telemetry Stream]
    end
    subgraph YieldArch-AI
        T --> R{Cognitive Router}
        R --> L1[Level 1: Heuristic]
        R --> L2[Level 2: Statistical]
        R --> L3[Level 3: Multi-modal]
    end
    L1 --> O[Optimization Output]
    L2 --> O
    L3 --> O
""",
        "sequence_diagram": """
sequenceDiagram
    participant S as Station Sensor
    participant R as Meta-Cognitive Router
    participant A as Reasoning Engine
    participant R as Result Database
    
    S->>R: Send Telemetry
    R->>R: Analyze Complexity
    alt High Complexity
        R->>A: Invoke Deep RCA (Level 3)
    else Low Complexity
        R->>A: Invoke Shallow Fix (Level 1)
    end
    A-->>R: Final Action/Diagnosis
    R->>R: Log Optimization
""",
        "flow_diagram": """
flowchart TD
    Start([Receive Sensor Data]) --> Check{Is Drift Linear?}
    Check -- Yes --> Fix[Apply Thermal Calibration]
    Check -- No --> Examine[Perform Cross-Sensor Correlation]
    Examine --> Valid{Root Cause Found?}
    Valid -- No --> Deep[Trigger Level 3 Meta-Cognitive Analysis]
    Valid -- Yes --> Apply[Apply Precision Adjustment]
    Deep --> End([Yield Optimized])
    Apply --> End
"""
    }

    os.makedirs("images", exist_ok=True)
    
    for name, code in diagrams.items():
        print(f"Generating {name}...")
        encoded = base64.urlsafe_b64encode(code.encode()).decode()
        url = f"https://mermaid.ink/img/{encoded}"
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"images/{name}.png", 'wb') as f:
                f.write(response.content)
            print(f"Successfully saved images/{name}.png")
        else:
            print(f"Failed to generate {name}: {response.status_code}")

if __name__ == "__main__":
    generate_mermaid_diagrams()
