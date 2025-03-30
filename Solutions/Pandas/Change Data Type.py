import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # 1 
    students = students.astype({'grade': int})

    # 2
    students['grade'] = students['grade'].astype(int)

    return students