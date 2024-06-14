"""You are a teacher who wants to keep track of your students’ exam scores for different subjects. You have collected the following data:
Each student is identified by a unique student ID.
For each student, you have their scores in three subjects: Math, Science, and English.
Write a program that creates a DataFrame that displays each student’s scores with the student IDs as index labels as follows
          Math  Science  English
Student1    85   	92   	78
Student2    90   	88   	85
Student3    75   	95   	80
"""
import pandas as pd

# Sample data
data = {
    'Math': [85, 90, 75],
    'Science': [92, 88, 95],
    'English': [78, 85, 80]
}

# Define student IDs
student_ids = ['Student1', 'Student2', 'Student3']

# Create DataFrame
df = pd.DataFrame(data, index=student_ids)

# Display the DataFrame
print(df)
