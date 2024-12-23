import pandas as pd
import numpy as np

def calculate_ip_entropy(df):
    """
    Calculates IP entropy to detect irregularities in network traffic.
    :param df: Input DataFrame
    :return: Array of IP entropy values
    """
    ip_counts = df['src_ip'].value_counts()
    probabilities = ip_counts / ip_counts.sum()
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

def extract_packet_features(df):
    """
    Extracts packet-level features such as packet size statistics.
    :param df: Input DataFrame
    :return: DataFrame with additional features
    """
    df['packet_size_mean'] = df['packet_size'].mean()
    df['packet_size_std'] = df['packet_size'].std()
    return df

if __name__ == "__main__":
    file_path = "../data/labeled_traffic.csv"
    df = pd.read_csv(file_path)
    df = extract_packet_features(df)
    ip_entropy = calculate_ip_entropy(df)
    print(f"IP Entropy: {ip_entropy}")
    df.to_csv("../data/processed_traffic.csv", index=False)
