# SiteScanner-AI: Autonomous Retail Location Intelligence Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/release/python-3120/)

## How I Automated Retail Expansion Strategy with Geospatial AI and Spatial Clustering

![SiteScanner-AI Animation](https://raw.githubusercontent.com/aniket-work/SiteScanner-AI/main/images/title-animation.gif)

SiteScanner-AI is an experimental PoC designed to solve the complex business problem of retail site selection. By synthesizing urban demographic layers, foot traffic simulations, and competitor proximity data, this engine identifies the "hottest" underserved spots for franchise expansion.

> **Note:** This is an experimental project and part of my personal research into autonomous geospatial agents.

---

## 🏗️ System Architecture

![Architecture](https://raw.githubusercontent.com/aniket-work/SiteScanner-AI/main/images/architecture-diagram.png)

The system is built on a modular three-tier architecture:
1.  **Data Layer**: Generates high-fidelity synthetic urban environments with demographic and competitive features.
2.  **Compute Layer**: A weighted ROI optimizer that ranks sites based on customized business drivers.
3.  **Visualization Layer**: An interactive Folium-based engine that renders decision-grade geospatial reports.

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/aniket-work/SiteScanner-AI.git
cd SiteScanner-AI
```

### 2. Setup Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run Analysis
```bash
python3 main.py
```

---

## 📊 Logic Flow

![Workflow](https://raw.githubusercontent.com/aniket-work/SiteScanner-AI/main/images/flow-diagram.png)

The engine follows a rigorous pipeline:
- **Synthetic Synthesis**: Creating a digital twin of urban activity.
- **Competitor Cannibalization Audit**: Calculating penalty scores for proximity to existing brands.
- **ROI Scoring**: Applying weighted importance to foot traffic vs. household income.
- **Spatial Clustering**: Using K-Means to identify target investment corridors.

---

## 🛠️ Tech Stack
- **Language**: Python 3.12
- **Geospatial**: Folium, Branca
- **Analysis**: Pandas, NumPy, Scikit-learn
- **Viz Assets**: PIL (Pillow), Mermaid.js

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙋‍♂️ Author
**Aniket** - [GitHub](https://github.com/aniket-work)
**Experimental PoC Article**: [Read the full story on Dev.to](https://dev.to/aniketwork/location-intelligence-building-an-autonomous-site-selection-engine-with-geospatial-ai-1m8k)
