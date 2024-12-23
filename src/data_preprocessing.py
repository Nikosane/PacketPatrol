import pandas as pd

def load_data(file_path):
    """
    Loads the network traffic data from a CSV file.
    :param file_path: Path to the CSV file
    :return: DataFrame containing the data
    """
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Cleans the network traffic data by handling missing values and removing duplicates.
    :param df: Input DataFrame
    :return: Cleaned DataFrame
    """
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def preprocess_data(df):
    """
    Preprocess the network traffic data for feature extraction.
    :param df: Input DataFrame
    :return: Preprocessed DataFrame
    """
    # Example preprocessing: Convert timestamps to datetime
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

if __name__ == "__main__":
    file_path = "../data/raw_traffic.csv"
    data = load_data(file_path)
    cleaned_data = clean_data(data)
    preprocessed_data = preprocess_data(cleaned_data)
    preprocessed_data.to_csv("../data/labeled_traffic.csv", index=False)
