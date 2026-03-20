import pandas as pd
import numpy as np
import random

class DataFactory:
    """
    Generates synthetic geospatial data for retail site selection analysis.
    Simulates a metropolitan area with demographic and competitor layers.
    """
    def __init__(self, city_name="Metropolis", center_lat=37.7749, center_lon=-122.4194, scale=0.1):
        self.city_name = city_name
        self.center_lat = center_lat
        self.center_lon = center_lon
        self.scale = scale

    def generate_candidate_sites(self, n=50):
        """Generates random candidate locations for new stores."""
        lats = self.center_lat + np.random.uniform(-self.scale, self.scale, n)
        lons = self.center_lon + np.random.uniform(-self.scale, self.scale, n)
        
        sites = pd.DataFrame({
            'site_id': [f"SITE_{i:03d}" for i in range(n)],
            'latitude': lats,
            'longitude': lons,
            'avg_income': np.random.normal(75000, 20000, n),
            'pop_density': np.random.normal(5000, 1500, n),
            'foot_traffic': np.random.randint(500, 5000, n)
        })
        return sites

    def generate_competitors(self, n=15):
        """Generates existing competitor locations."""
        lats = self.center_lat + np.random.uniform(-self.scale, self.scale, n)
        lons = self.center_lon + np.random.uniform(-self.scale, self.scale, n)
        
        competitors = pd.DataFrame({
            'comp_id': [f"COMP_{i:03d}" for i in range(n)],
            'latitude': lats,
            'longitude': lons,
            'brand': random.choice(['GlobalCoffee', 'UrbanBrew', 'CafeStandard'])
        })
        return competitors

    def generate_urban_clusters(self, n_points=1000):
        """Generates a dense cloud of points representing general population for heatmap."""
        lats = self.center_lat + np.random.normal(0, self.scale/2, n_points)
        lons = self.center_lon + np.random.normal(0, self.scale/2, n_points)
        return pd.DataFrame({'latitude': lats, 'longitude': lons})
