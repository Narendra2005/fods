import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Generate sample data
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M'],
    'BloodPressure': [120, 130, 125, 135, 140, 130, 135, 145, 150, 140, 130, 135, 125, 130, 135],
    'Cholesterol': [200, 220, 240, 210, 230, 250, 220, 240, 260, 230, 210, 250, 240, 220, 200],
    'Response': ['Good', 'Bad', 'Good', 'Good', 'Good', 'Good', 'Bad', 'Good', 'Good', 'Good', 'Bad', 'Good', 'Good', 'Good', 'Bad']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# One-hot encode 'Gender' column
df = pd.get_dummies(df, columns=['Gender'], drop_first=True)

# Splitting the data into features and target variable
X = df.drop('Response', axis=1)
y = df['Response']

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
# Not necessary for KNN but can improve performance
# Here we'll skip it since our data doesn't require scaling

# Fitting KNN classifier to the Training set
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predicting the Test set results
y_pred = knn.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='Good')
recall = recall_score(y_test, y_pred, pos_label='Good')
f1 = f1_score(y_test, y_pred, pos_label='Good')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
