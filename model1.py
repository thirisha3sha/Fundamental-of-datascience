"""Scenario: Your HR department has provided you with an employee dataset containing columns like EmployeeID, Department, Salary, and Hire Date. Utilize Pandas data frames to perform the following tasks:
   Question:
	- Determine the highest and lowest salaries in each department.
	- Calculate the average salary in the company.
   - Identify employees who were hired in a specific year different events.
"""
import pandas as pd
data = {
    'EmployeeID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Department': ['HR', 'Finance', 'IT', 'HR', 'IT', 'Finance', 'HR', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 75000, 52000, 80000, 62000, 55000, 63000, 78000, 51000],
    'HireDate': ['2018-03-01', '2019-06-15', '2020-07-20', '2017-08-25', '2021-01-10', '2018-11-05', '2016-12-23', '2020-09-17', '2019-10-30', '2017-05-18']
}
df=pd.DataFrame(data)
highest_salary=df.groupby('Department')['Salary'].max()
lowest_salary=df.groupby('Department')['Salary'].min()
print("\n highest salary:",highest_salary)
print("\n lowest salary:",lowest_salary)
df['HireDate']=pd.to_datetime(df['HireDate'])
specific_year=2019
employee_hired=df[df['HireDate'].dt.year==specific_year]
print(f"\n emplpoyee hired in {specific_year} is :\n",employee_hired)
avg_salary=df['Salary'].mean()
print("\naverage salarymin the company:",avg_salary)
