import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data_distribution(df, column):
    """
    Plots the distribution of a specific column in the DataFrame.
    :param df: Input DataFrame
    :param column: Column name to visualize
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, bins=30)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def plot_correlation_matrix(df):
    """
    Plots the correlation matrix of the DataFrame features.
    :param df: Input DataFrame
    """
    plt.figure(figsize=(12, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()

if __name__ == "__main__":
    file_path = "../data/processed_traffic.csv"
    df = pd.read_csv(file_path)
    visualize_data_distribution(df, "packet_size_mean")
    plot_correlation_matrix(df)
