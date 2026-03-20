import base64
import requests
import os
import time

def generate_mermaid_diagrams():
    diagrams = {
        "title-diagram": """
graph TD
    A[Consumer Demographics] --> E[SiteScanner-AI Engine]
    B[Urban Mobility Data] --> E
    C[Competitor Locations] --> E
    D[Candidate Sites] --> E
    E --> F[Weighted ROI Scoring]
    E --> G[Spatial Clustering]
    F --> H[Optimal Site Recommendations]
    G --> H
    style E fill:#f9f,stroke:#333,stroke-width:4px
    style H fill:#00ff00,stroke:#333,stroke-width:2px
""",
        "architecture-diagram": """
graph LR
    subgraph "Data Layer"
        DF[Data Factory]
        DB[(Synthetic GeoDB)]
    end
    subgraph "Compute Layer"
        OP[Site Optimizer]
        SC[Scoring Model]
        CL[Clustering Unit]
    end
    subgraph "Presentation Layer"
        VZ[Folium Visualizer]
        UI[Interactive HTML Map]
    end
    DF --> DB
    DB --> OP
    OP --> SC
    OP --> CL
    SC --> VZ
    CL --> VZ
    VZ --> UI
""",
        "sequence-diagram": """
sequenceDiagram
    participant U as User/Business
    participant E as SiteScanner Engine
    participant D as Data Layer
    participant O as Optimizer
    participant V as Visualizer

    U->>E: Start Analysis
    E->>D: Fetch/Generate Urban Layers
    D-->>E: Candidate & Competitor Data
    E->>O: Rank Candidates
    O-->>E: Weighted Scores
    E->>O: Identitfy Spatial Clusters
    O-->>E: Cluster Centers
    E->>V: Map Data Points
    V-->>U: Interactive Site Map
""",
        "flow-diagram": """
flowchart TD
    Start([Start Experiment]) --> GenData[Generate Synthetic Urban Data]
    GenData --> ProcessParams[Process Demographic Weights]
    ProcessParams --> CalcDist[Calculate Competitor Proximity]
    CalcDist --> CalcScore[Compute Final ROI Score]
    CalcScore --> Cluster[Run K-Means Clustering]
    Cluster --> Render[Render Folium Layers]
    Render --> Export[Export HTML Report]
    Export --> End([End])
"""
    }

    os.makedirs("images", exist_ok=True)
    
    print("Generating Mermaid diagrams...")
    for name, code in diagrams.items():
        encoded = base64.b64encode(code.encode()).decode()
        url = f"https://mermaid.ink/img/{encoded}"
        
        try:
            print(f"Requesting: {name}...")
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                with open(f"images/{name}.png", 'wb') as f:
                    f.write(response.content)
                print(f"✅ Saved images/{name}.png")
            else:
                print(f"❌ Failed to generate {name}: {response.status_code}")
        except Exception as e:
            print(f"❌ Error generating {name}: {str(e)}")
        
        # Small delay to avoid rate limiting
        time.sleep(1)

if __name__ == "__main__":
    generate_mermaid_diagrams()
    # Verify files
    expected = ["title-diagram.png", "architecture-diagram.png", "sequence-diagram.png", "flow-diagram.png"]
    found = os.listdir("images")
    for exp in expected:
        if exp not in found:
            print(f"CRITICAL: {exp} missing!")
        else:
            print(f"Verified: {exp}")
