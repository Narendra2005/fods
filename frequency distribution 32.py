import pandas as pd

# Create a DataFrame from the provided dataset
data = {
    'DISEASE_NAME': ['Common Cold', 'Diabetes', 'Bronchitis', 'Influenza', 'Kidney Stones'],
    'DIAGNOSED_PATIENTS': [320, 120, 100, 150, 60]
}

df = pd.DataFrame(data)

# Sort the DataFrame by the number of diagnosed patients in descending order
df_sorted = df.sort_values(by='DIAGNOSED_PATIENTS', ascending=False)

# Print the most common disease
most_common_disease = df_sorted.iloc[0]['DISEASE_NAME']
print("Most Common Disease:", most_common_disease)

# Print the frequency distribution of diseases
print("\nFrequency Distribution:")
print(df_sorted)
