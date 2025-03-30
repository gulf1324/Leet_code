"""
id to student_id
first to first_name
last to last_name
age to age_in_years
"""

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(columns={'id':'student_id',
                                        'first':'first_name',
                                        'last':'last_name',
                                        'age':'age_in_years'})
    return students

# def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
#     students.columns = ["student_id","first_name","last_name","age_in_years"]
#     return students
