import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students["student_id"]==101].filter(items=["name","age"])
    
    # loc
    return students.loc[students["student_id"] == 101, ["name", "age"]]
    
    # pd.DataFrame[][]
    return students[students["student_id"]==101][["name","age"]]

print(selectData(pd.DataFrame([[101,"Ulysses","13"]],columns=["student_id","name","age"])))