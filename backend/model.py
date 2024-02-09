import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from data import merged_df  # Importing merged_df from data.py

# Define features and target variable
features = ['page_views', 'time_spent', 'price', 'ratings']  # Assuming these are your features
target = 'product_id'  # Assuming this is your target variable

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(merged_df[features], merged_df[target], test_size=0.2, random_state=42)

# Initialize Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_classifier.fit(X_train, y_train)

# Make predictions
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Generate classification report
print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=1))
