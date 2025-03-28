import pandas as pd
def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    columns = ["student_id", "age"]
    df = pd.DataFrame(student_data, columns= columns)
    return df
############################################################################################
print(createDataframe(student_data=[[1, 15],
                                    [2, 11],
                                    [3, 11],
                                    [4, 20]
                                    ]))