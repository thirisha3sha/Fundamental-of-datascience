"""cenario: You are working on a project that involves analyzing student performance data for a class of 10 students. The data is stored in a NumPy array named student_scores, where each row represents a student and each column represents a different subject. The subjects are arranged in the following order: Math, Science, English, and History. Your task is to calculate the average score for each subject and identify the subject with the highest average score.
Question: How would you use NumPy arrays to calculate the average score for each subject and determine the subject with the highest average score? Assume 4x4 matrix that stores marks of each student in given order.
 
"""
import numpy as np
import pandas as pd

# Sample student scores data (mock data)
# Assuming each row represents a student and each column represents a subject
student_scores = np.array([
    [75, 80, 85, 90],
    [70, 85, 75, 95],
    [65, 75, 80, 85],
    [80, 90, 95, 85]
])

# Print the student_scores array (optional)
print("Student Scores:")
print(student_scores)
print()

# Calculate average score for each subject
average_scores = np.mean(student_scores, axis=0)

# Print average scores (optional)
print("Average Scores for Each Subject:")
for i, subject in enumerate(['Math', 'Science', 'English', 'History']):
    print(f"{subject}: {average_scores[i]}")

# Identify subject with the highest average score
highest_average_subject = np.argmax(average_scores)
subject_names = ['Math', 'Science', 'English', 'History']
highest_average_subject_name = subject_names[highest_average_subject]

print()
print(f"Subject with the Highest Average Score: {highest_average_subject_name} ({average_scores[highest_average_subject]})")
