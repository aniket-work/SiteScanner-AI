import os
import json
import pandas as pd
from engine.data_factory import DataFactory
from engine.optimizer import SiteOptimizer
from engine.visualizer import SiteVisualizer

def run_experiment():
    print("--- [SiteScanner-AI] Starting Autonomous Site Analysis ---")
    
    # 1. Initialize City Simulation
    print("[1/5] Synthesizing urban geospatial layers...")
    factory = DataFactory(city_name="San Francisco", center_lat=37.7749, center_lon=-122.4194)
    candidates = factory.generate_candidate_sites(n=40)
    competitors = factory.generate_competitors(n=12)
    urban_mesh = factory.generate_urban_clusters(n_points=800)
    
    # 2. Optimization Engine
    print("[2/5] Running spatial optimization models...")
    optimizer = SiteOptimizer(candidates, competitors)
    ranked_sites = optimizer.calculate_scores()
    
    # 3. Clustering Insights
    print("[3/5] Identifying strategic high-density corridors...")
    clustered_df, centers = optimizer.find_strategic_clusters(n_clusters=4)
    
    # 4. Interactive Visualization
    print("[4/5] Generating interactive visualization engine...")
    viz = SiteVisualizer(center_lat=37.7749, center_lon=-122.4194)
    viz.add_heatmap(urban_mesh)
    viz.add_competitors(competitors)
    viz.add_candidate_recommendations(ranked_sites, top_n=5)
    
    output_map = "site_selection_analysis.html"
    viz.save_map(output_map)
    
    # 5. Output Summary
    print(f"[5/5] Analysis complete! Map saved to: {output_map}")
    print("\nTop 5 Recommended Locations:")
    print(ranked_sites[['site_id', 'score', 'avg_income', 'foot_traffic']].head(5).to_string(index=False))
    
    # Save statistics for the GIF/article
    stats = {
        "total_candidates": len(candidates),
        "total_competitors": len(competitors),
        "avg_score": ranked_sites['score'].mean(),
        "top_site_id": ranked_sites.iloc[0]['site_id'],
        "top_site_score": float(ranked_sites.iloc[0]['score'])
    }
    with open("analysis_stats.json", "w") as f:
        json.dump(stats, f)

if __name__ == "__main__":
    run_experiment()
