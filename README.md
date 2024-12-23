# PacketPatrol

This project aims to develop a machine learning model that can detect botnet activity in network traffic by analyzing patterns and anomalies.

## Objective
The goal is to identify botnet attacks by analyzing network traffic using machine learning algorithms. This will help in real-time detection and prevention of botnet-related security threats.

## Tech Stack
- **Python**: The primary programming language.
- **PyTorch**: For machine learning model training.
- **Scapy**: For packet parsing and network traffic analysis.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib, Seaborn**: For data visualization.


### Dependencies
Create a virtual environment and install the dependencies listed in the `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

1. Preprocess the network traffic data:
```
python src/data_preprocessing.py
```
2. Train the botnet detection model:
```
python src/model_training.py
```
3. Perform anomaly detection:
```
python src/anomaly_detection.py
```
4. Visualize and analyze results:
```
python src/exploratory_analysis.ipynb
```
