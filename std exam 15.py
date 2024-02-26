import pandas as pd

# Creating a dictionary with student IDs as keys and their scores as values
student_scores = {
    'Student1': {'Math': 85, 'Science': 92, 'English': 78},
    'Student2': {'Math': 90, 'Science': 88, 'English': 85},
    'Student3': {'Math': 75, 'Science': 95, 'English': 80}
}

# Creating the DataFrame
df = pd.DataFrame(student_scores)

# Transposing the DataFrame to have students as rows and subjects as columns
df = df.T

# Displaying the DataFrame
print(df)