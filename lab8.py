"""Scenario: You are working on a project that involves analyzing student performance data for a class of 10 students. The data is stored in a NumPy array named student_scores, where each row represents a student and each column represents a different subject. The subjects are arranged in the following order: Math, Science, English, and History. Your task is to calculate the average score for each subject and identify the subject with the highest average score.
Question: How would you use NumPy arrays to calculate the average score for each subject and determine the subject with the highest average score? Assume 4x4 matrix that stores marks of each student in given order.
"""
import numpy as np
np.random.seed
student_scores=np.random.randint(50,100,size=(10,4))
avg_scores=student_scores.mean(axis=0)
subjects=['Maths,Science','Social','English']
highest_avg_sub_index=np.argmax(avg_scores)
highest_avg_subject=subjects[highest_avg_sub_index]
print("student scores:\n",student_scores)
print("\n Average scores for each subject:",avg_scores)
print(f"The subject with the highest average score is {highest_avg_subject} with an average score of {avg_scores[highest_avg_sub_index]:.2f}")
