import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

def predict_lifestyle(
    anxiety_level, mental_health_history, depression, headache,
    sleep_quality, safety, academic_performance, future_career_concerns,
    social_support, peer_pressure, extracurricular_activities, bullying
):
    try:
        # Load the dataset
        dataset = pd.read_csv(r'C:\Users\Admin\Desktop\PyHack24-Dominators-15\mentalHealth\student_dataset.csv')

        # Define feature names based on the user-provided input
        feature_names = [
            "anxiety_level", "mental_health_history", "depression", "headache",
            "sleep_quality", "safety", "academic_performance", "future_career_concerns",
            "social_support", "peer_pressure", "extracurricular_activities", "bullying"
        ]

        # Extract features and target from the dataset
        X = dataset[feature_names].values
        y = dataset["Target"].values

        # Split the dataset into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

        # Feature scaling
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)

        # Train the KNN classifier
        classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
        classifier.fit(X_train, y_train)

        # Evaluate the classifier
        y_pred = classifier.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        accuracy = accuracy_score(y_test, y_pred)
        print("Confusion Matrix:")
        print(cm)
        print("Accuracy Score:", accuracy)

        # Collect user input for the features
        user_input = [
            anxiety_level, mental_health_history, depression, headache,
            sleep_quality, safety, academic_performance, future_career_concerns,
            social_support, peer_pressure, extracurricular_activities, bullying
        ]

        # Convert the user input to a numpy array and reshape for a single sample
        user_input = np.array(user_input).reshape(1, -1)

        # Preprocess the user input (apply the same scaling as the training data)
        user_input = sc.transform(user_input)

        # Predict the outcome
        prediction = classifier.predict(user_input)

        # Interpretation of the prediction
        if prediction[0] == 0:
            print("Perfect lifestyle")
        elif prediction[0] == 1:
            print("Lifestyle change needed")
        elif prediction[0] == 2:
            print("Therapy needed")

        return prediction[0]
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


result = predict_lifestyle(1,2,4,1,3,1,2,4,2,3,18,14)
print(result)