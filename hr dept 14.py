import pandas as pd

# Create a dictionary with employee data
employee_data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'HR'],
    'Salary': [60000, 70000, 80000, 75000, 65000],
    'JoiningDate': ['2020-01-15', '2019-05-20', '2021-03-10', '2018-11-28', '2020-08-12']
}
# Convert dictionary to DataFrame
employee_df = pd.DataFrame(employee_data)

highest_salaries = employee_df.groupby('Department')['Salary'].max()
lowest_salaries = employee_df.groupby('Department')['Salary'].min()
print("Highest Salaries:\n", highest_salaries)
print("\nLowest Salaries:\n", lowest_salaries)

# Convert JoiningDate to datetime
employee_df['JoiningDate'] = pd.to_datetime(employee_df['JoiningDate'])

# Calculate tenure (in days) by subtracting JoiningDate from current date
employee_df['Tenure'] = (pd.Timestamp.now() - employee_df['JoiningDate']).dt.days
print(employee_df)
# Calculate average tenure
average_tenure = employee_df['Tenure'].mean()
print("\nAverage Tenure (in days):", average_tenure)

specific_date = '2020-01-01'
employees_before_date = employee_df[employee_df['JoiningDate'] < specific_date]
print("\nEmployees who joined before", specific_date, ":\n", employees_before_date)



#.dt.days: This accessor extracts the number of days from each Timedelta object in the series. 
#It converts the Timedelta objects into integers representing the number of days. 
#This operation allows us to represent tenure in terms of days.

