import os
import re
import json
import random
import datetime
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from colorama import Fore, Style, init

# Initialize colorama for terminal output
init(autoreset=True)

class LocalThreatSentinel:
    """
    A local, privacy-focused threat detection engine using Unsupervised Learning (Isolation Forest).
    It analyzes system logs for anomalous patterns without sending data to the cloud.
    """

    def __init__(self, contamination_level=0.05):
        """
        Initialize the detector model.
        :param contamination_level: Expected proportion of outliers in the dataset.
        """
        self.model = IsolationForest(n_estimators=100, contamination=contamination_level, random_state=42)
        self.scaler = StandardScaler()
        self.data_frame = pd.DataFrame()
        print(f"{Fore.CYAN}[INFO] Sentinel Engine Initialized (Local Mode).")

    def generate_dummy_logs(self, num_records=1000):
        """
        Generates synthetic server logs for demonstration purposes.
        In production, this would be replaced by a file reader.
        """
        print(f"{Fore.YELLOW}[PROCESS] Generating {num_records} synthetic log entries...")
        
        data = []
        base_time = datetime.datetime.now()

        for _ in range(num_records):
            # Simulate normal traffic (95%) vs Attack traffic (5%)
            is_attack = random.random() < 0.05
            
            if is_attack:
                # Attack pattern: High payload size, unusual ports, rapid requests
                payload_size = random.randint(5000, 15000)
                port = random.choice([22, 23, 445, 3389]) # Sensitive ports
                response_time = random.uniform(0.1, 0.5)
                status_code = random.choice([401, 403, 500])
            else:
                # Normal pattern
                payload_size = random.randint(100, 2000)
                port = random.choice([80, 443, 8080])
                response_time = random.uniform(0.05, 1.2)
                status_code = 200

            data.append({
                'timestamp': base_time - datetime.timedelta(seconds=random.randint(0, 86400)),
                'payload_size': payload_size,
                'port': port,
                'response_time': response_time,
                'status_code': status_code
            })

        self.data_frame = pd.DataFrame(data)
        print(f"{Fore.GREEN}[SUCCESS] Data loaded successfully. Shape: {self.data_frame.shape}")

    def train_and_detect(self):
        """
        Trains the Isolation Forest model on the loaded data and detects anomalies.
        """
        if self.data_frame.empty:
            print(f"{Fore.RED}[ERROR] No data to process.")
            return

        print(f"{Fore.YELLOW}[AI TASK] Training Isolation Forest model on local CPU...")
        
        # Feature selection for the model
        features = ['payload_size', 'port', 'response_time', 'status_code']
        X = self.data_frame[features]

        # Normalization
        X_scaled = self.scaler.fit_transform(X)

        # Training
        self.model.fit(X_scaled)

        # Prediction (-1 for outlier/anomaly, 1 for inlier/normal)
        self.data_frame['anomaly_score'] = self.model.decision_function(X_scaled)
        self.data_frame['is_anomaly'] = self.model.predict(X_scaled)

        anomalies = self.data_frame[self.data_frame['is_anomaly'] == -1]
        
        self._export_report(anomalies)

    def _export_report(self, anomalies):
        """
        Exports the detected threats to a secure JSON file.
        """
        count = len(anomalies)
        if count > 0:
            print(f"{Fore.RED}[ALERT] Detected {count} potential threats!")
            
            report_filename = f"security_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            # Convert timestamp to string for JSON serialization
            anomalies['timestamp'] = anomalies['timestamp'].astype(str)
            
            report_data = {
                "scan_time": str(datetime.datetime.now()),
                "total_scanned": len(self.data_frame),
                "threats_detected": count,
                "threat_details": anomalies.to_dict(orient='records')
            }

            with open(report_filename, 'w') as f:
                json.dump(report_data, f, indent=4)

            print(f"{Fore.GREEN}[REPORT] Detailed report saved to: {report_filename}")
        else:
            print(f"{Fore.GREEN}[SECURE] No anomalies detected in the current batch.")

if __name__ == "__main__":
    # Simulate the pipeline
    sentinel = LocalThreatSentinel(contamination_level=0.04)
    sentinel.generate_dummy_logs(num_records=2000)
    sentinel.train_and_detect()