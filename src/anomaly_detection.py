import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(df, feature_columns):
    """
    Detects anomalies in network traffic data using Isolation Forest.
    :param df: Input DataFrame
    :param feature_columns: List of feature column names to use for detection
    :return: DataFrame with an additional 'anomaly' column
    """
    model = IsolationForest(contamination=0.01, random_state=42)
    df['anomaly'] = model.fit_predict(df[feature_columns])
    df['anomaly'] = df['anomaly'].apply(lambda x: 1 if x == -1 else 0)  # Mark anomalies as 1
    return df

if __name__ == "__main__":
    import pandas as pd

    file_path = "../data/processed_traffic.csv"
    df = pd.read_csv(file_path)
    feature_columns = ['packet_size_mean', 'packet_size_std']
    df = detect_anomalies(df, feature_columns)
    df.to_csv("../data/traffic_with_anomalies.csv", index=False)

