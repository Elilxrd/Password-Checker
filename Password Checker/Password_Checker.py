# password_checker_full.py
import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def load_ml_model():
    # Check if dataset exists
    if not os.path.exists("passwords.csv"):
        print("ML dataset not found (passwords.csv). Skipping ML prediction.")
        return None, None, None

    df = pd.read_csv("passwords.csv")

    # Feature extraction
    def extract_features(p):
        return pd.Series({
            "length": len(p),
            "digits": len(re.findall(r"[0-9]", p)),
            "uppercase": len(re.findall(r"[A-Z]", p)),
            "special": len(re.findall(r"[^A-Za-z0-9]", p))
        })

    X = df['password'].apply(extract_features)
    y = df['label']  # weak or strong

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    # Evaluate accuracy
    y_pred = clf.predict(X_test)
    print("ML model accuracy on test set:", accuracy_score(y_test, y_pred))

    return clf, extract_features


def main():
    print("=== Password Strength Checker ===")
    password = input("Enter password: ")

    # Part 1: Basic strength
    basic_result = check_strength(password)
    print(f"[Basic Checker] Password strength: {basic_result}")

    # Part 2: ML prediction
    clf, feature_func = load_ml_model()
    if clf and feature_func:
        features = feature_func(password).values.reshape(1, -1)
        ml_result = clf.predict(features)[0]
        print(f"[ML Prediction] Password strength: {ml_result}")

if __name__ == "__main__":
    main()