import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Default dictionary of 15 values with attributes
data = {
    'symptom1': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'symptom2': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'symptom3': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'symptom4': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'symptom5': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'condition': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Split features and target
X = df.drop('condition', axis=1)
y = df['condition']

# User input for new patient's symptoms
new_symptoms = []
for i in range(5):
    new_symptom = int(input(f"Enter symptom {i+1} (0 or 1): "))
    new_symptoms.append(new_symptom)

# User input for number of neighbors (k)
k = int(input("Enter the number of neighbors (k): "))

# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors=k)

# Fit the classifier to the data
knn.fit(X, y)

# Predict the condition for the new patient
prediction = knn.predict([new_symptoms])

if prediction[0] == 1:
    print("The patient is predicted to have the medical condition.")
else:
    print("The patient is predicted to not have the medical condition.")
