"""A school wants to evaluate the performance of its students based on their scores in a recent exam. The exam scores (out of 100) for a sample of students are as follows: [65, 70, 72, 75, 80, 85, 90, 95, 100]. Calculate the 25th and 75th percentiles of the exam scores."""
import pandas as pd
import numpy as np

# Exam scores data
exam_scores = [65, 70, 72, 75, 80, 85, 90, 95, 100]

# Create a DataFrame
df = pd.DataFrame({'Exam Scores': exam_scores})

# Calculate percentiles
percentile_25 = np.percentile(exam_scores, 25)
percentile_75 = np.percentile(exam_scores, 75)

print(f'25th percentile: {percentile_25}')
print(f'75th percentile: {percentile_75}')
