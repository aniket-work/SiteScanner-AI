import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

class SiteOptimizer:
    """
    Analyzes candidate sites and ranks them based on proximity to demand
    and distance from competitors.
    """
    def __init__(self, candidates, competitors):
        self.candidates = candidates
        self.competitors = competitors

    def calculate_scores(self, weights=None):
        """
        Calculates a viability score for each candidate site.
        Score = (Income * w1) + (Traffic * w2) - (CompetitorPenalty * w3)
        """
        if weights is None:
            weights = {'income': 0.3, 'traffic': 0.5, 'competitor': 0.2}

        # Normalize features
        df = self.candidates.copy()
        df['norm_income'] = (df['avg_income'] - df['avg_income'].min()) / (df['avg_income'].max() - df['avg_income'].min())
        df['norm_traffic'] = (df['foot_traffic'] - df['foot_traffic'].min()) / (df['foot_traffic'].max() - df['foot_traffic'].min())

        # Competitor Penalty: inverse of distance to nearest competitor
        # We use a simple Euclidean distance as an approximation for Lat/Lon in small scale
        cand_coords = df[['latitude', 'longitude']].values
        comp_coords = self.competitors[['latitude', 'longitude']].values
        
        # Distance to nearest competitor
        distances = cdist(cand_coords, comp_coords)
        min_dist_to_comp = distances.min(axis=1)
        
        # Normalize penalty (closer = higher penalty)
        # We want sites far from competitors, so we use the normalized distance directly
        df['norm_dist_comp'] = (min_dist_to_comp - min_dist_to_comp.min()) / (min_dist_to_comp.max() - min_dist_to_comp.min())

        df['score'] = (df['norm_income'] * weights['income'] + 
                       df['norm_traffic'] * weights['traffic'] + 
                       df['norm_dist_comp'] * weights['competitor']) * 100
        
        return df.sort_values(by='score', ascending=False)

    def find_strategic_clusters(self, n_clusters=5):
        """Uses K-Means to identify target regions with high density of candidates."""
        coords = self.candidates[['latitude', 'longitude']].values
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        self.candidates['cluster'] = kmeans.fit_predict(coords)
        return self.candidates, kmeans.cluster_centers_
