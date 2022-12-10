'''
Marian Remoroza
Data Science
Task 1
'''
import pandas as pd
import sqlite3 as sql
import numpy as np

scores = pd.read_csv('scores.csv')  # uploading scores.csv
#scores['Max Point'] = pd.Series([100 for x in range(len(scores.index))])
scores = scores.fillna(0)
print(scores)
weightings = pd.Series(
    {
        "Test 1": .2,
        "Test 2": .2,
        "Test 3": .2,
        "Project": .4, }
)
grades = {
    90: "A",
    80: "B",
    70: "C",
}


def grade_mapping(value):
    for key, letter in grades.items():
        if value >= key:
            return letter


'''
n_exams = 3
for n in range(1, n_exams + 1):
    scores[f"Test {n} Score"] = (
        scores[f"Test {n}"]/scores[f"Test {n} - Max Point"])
'''
scores["Grade"] = (scores[weightings.index]*weightings).sum(axis=1)
scores['Max Score'] = np.ceil(scores['Grade'])
letter_grade = scores["Max Score"].map(grade_mapping)
scores["Grade"] = pd.Categorical(
    letter_grade, categories=grades.values(), ordered=True)

print(scores)
