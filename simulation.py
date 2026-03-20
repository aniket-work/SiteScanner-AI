import random
import time
from typing import Dict, List

class SemiconductorSim:
    """Simulates a semiconductor fabrication sensor environment."""
    
    STATIONS = ["Lithography", "Etching", "Deposition", "Ion-Implantation"]
    
    def __init__(self):
        self.base_yield = 0.94
        
    def generate_telemetry(self) -> Dict:
        """Generates mock telemetry data with varying anomaly complexity."""
        station = random.choice(self.STATIONS)
        complexity = random.choice(["low", "medium", "high"])
        
        data = {
            "timestamp": time.time(),
            "station": station,
            "complexity_target": complexity,
            "sensors": {
                "temperature": random.uniform(20.0, 25.0),
                "pressure": random.uniform(100.0, 105.0),
                "gas_flow": random.uniform(50.0, 55.0),
                "plasma_intensity": random.uniform(0.8, 1.2)
            }
        }
        
        # Inject anomalies
        if complexity == "low":
            # Simple tool wear: slight temperature increase
            data["sensors"]["temperature"] += 5.0
            data["anomaly_hint"] = "Thermal Drift"
        elif complexity == "medium":
            # Temporal drift: oscillating pressure
            data["sensors"]["pressure"] += random.uniform(-10.0, 10.0)
            data["anomaly_hint"] = "Pressure Instability"
        else:
            # High: Complex correlation between plasma and gas flow
            data["sensors"]["plasma_intensity"] *= 0.5
            data["sensors"]["gas_flow"] *= 1.5
            data["anomaly_hint"] = "Chemical-Plasma Imbalance"
            
        return data

if __name__ == "__main__":
    sim = SemiconductorSim()
    print(sim.generate_telemetry())
