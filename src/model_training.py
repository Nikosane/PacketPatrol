import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

def train_model(X_train, y_train):
    """
    Trains a Random Forest Classifier on the provided training data.
    :param X_train: Training feature set
    :param y_train: Training labels
    :return: Trained model
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the model using accuracy, precision, and recall metrics.
    :param model: Trained model
    :param X_test: Test feature set
    :param y_test: Test labels
    :return: Dictionary with evaluation metrics
    """
    predictions = model.predict(X_test)
    return {
        'accuracy': accuracy_score(y_test, predictions),
        'precision': precision_score(y_test, predictions, average='weighted'),
        'recall': recall_score(y_test, predictions, average='weighted')
    }

if __name__ == "__main__":
    file_path = "../data/processed_traffic.csv"
    df = pd.read_csv(file_path)
    
    # Splitting features and labels
    X = df.drop(columns=['label'])
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Training the model
    model = train_model(X_train, y_train)

    # Evaluating the model
    metrics = evaluate_model(model, X_test, y_test)
    print(f"Model Metrics: {metrics}")
