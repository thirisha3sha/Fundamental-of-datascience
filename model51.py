"""Scenario: You are working on a project that involves analyzing student performance data
for a class of 10 students. The data is stored in a NumPy array named student_scores,
where each row represents a student and each column represents a different subject. The
subjects are arranged in the following order: Math, Science, English, and History. Your task is
to calculate the average score for each subject and identify the subject with the highest
average score.
Question: How would you use NumPy arrays to calculate the average score for each subject
and determine the subject with the highest average score? Assume 4x4 matrix that stores
marks of each student in given order."""
import numpy as np
import pandas as pd

# Sample data: student scores in the subjects Math, Science, English, and History
student_scores = np.array([
    [85, 90, 78, 92],
    [88, 85, 90, 80],
    [70, 78, 85, 88],
    [92, 88, 82, 90],
    [85, 95, 80, 85],
    [78, 80, 88, 82],
    [90, 85, 85, 88],
    [88, 92, 84, 86],
    [82, 80, 90, 92],
    [85, 88, 78, 84]
])

# Convert the NumPy array to a Pandas DataFrame
subjects = ['Math', 'Science', 'English', 'History']
df = pd.DataFrame(student_scores, columns=subjects)

# Calculate the average score for each subject
average_scores = df.mean()

# Identify the subject with the highest average score
highest_avg_subject = average_scores.idxmax()
highest_avg_score = average_scores.max()

# Output the results
print("Average scores for each subject:")
print(average_scores)
print(f"\nThe subject with the highest average score is {highest_avg_subject} with an average score of {highest_avg_score:.2f}")
