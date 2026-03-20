import folium
from folium.plugins import HeatMap, MarkerCluster
import os

class SiteVisualizer:
    """
    Creates an interactive HTML map for site selection analysis.
    """
    def __init__(self, center_lat, center_lon):
        self.center = [center_lat, center_lon]
        self.m = folium.Map(location=self.center, zoom_start=13, tiles='CartoDB dark_matter')

    def add_heatmap(self, urban_data):
        """Adds a heatmap representing general urban activity/demand."""
        heat_data = [[row['latitude'], row['longitude']] for index, row in urban_data.iterrows()]
        HeatMap(heat_data, radius=10, blur=15, gradient={0.4: 'blue', 0.65: 'lime', 1: 'yellow'}).add_to(self.m)

    def add_competitors(self, competitors):
        """Adds markers for existing competitors."""
        comp_group = folium.FeatureGroup(name='Competitors').add_to(self.m)
        for _, row in competitors.iterrows():
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=5,
                color='red',
                fill=True,
                fill_color='red',
                popup=f"Competitor: {row['brand']}",
                tooltip=row['brand']
            ).add_to(comp_group)

    def add_candidate_recommendations(self, candidates, top_n=5):
        """Adds markers for candidate sites with special icons for top recommendations."""
        marker_cluster = MarkerCluster(name='Candidate Sites').add_to(self.m)
        
        # Identify top N sites
        top_sites_ids = candidates.head(top_n)['site_id'].values
        
        for _, row in candidates.iterrows():
            is_top = row['site_id'] in top_sites_ids
            color = 'gold' if is_top else 'lightblue'
            icon = 'star' if is_top else 'info-sign'
            
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                icon=folium.Icon(color=('orange' if is_top else 'blue'), icon=icon),
                popup=(f"<b>Site ID: {row['site_id']}</b><br>"
                       f"Rank Score: {row['score']:.2f}<br>"
                       f"Income: ${row['avg_income']:.0f}<br>"
                       f"Daily Traffic: {row['foot_traffic']}"),
                tooltip=f"Score: {row['score']:.1f}"
            ).add_to(marker_cluster)

    def save_map(self, filename="results_map.html"):
        """Saves the map to an HTML file."""
        folium.LayerControl().add_to(self.m)
        self.m.save(filename)
        return filename
