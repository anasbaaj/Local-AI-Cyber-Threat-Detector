# 🛡️ Local Threat Sentinel (AI-Powered)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Security](https://img.shields.io/badge/Security-Isolation_Forest-red?style=for-the-badge)

## 📌 Overview
**Local Threat Sentinel** is a privacy-first cybersecurity tool that uses **Unsupervised Machine Learning (Isolation Forest)** to detect network anomalies and potential intrusions. 

Unlike traditional rule-based IDS, this tool can identify unknown threats by analyzing statistical deviations in log patterns (Payload size, Port usage, Response times). **It runs 100% locally**, ensuring no sensitive logs are sent to the cloud.

## 🚀 Capabilities
- **Anomaly Detection:** Uses `Isolation Forest` algorithm to flag outliers.
- **Data Simulation:** Includes a generator for synthetic attack traffic (for testing).
- **Automated Reporting:** Exports detailed JSON reports of detected threats.
- **High Performance:** Built with `Pandas` and `NumPy` for fast data processing.

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/anasbaaj/Local-AI-Cyber-Threat-Detector.git](https://github.com/anasbaaj/Local-AI-Cyber-Threat-Detector.git)
   cd Local-AI-Cyber-Threat-Detector
