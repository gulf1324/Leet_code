import pandas as pd

data = {
    "city": ["Jacksonville", "Jacksonville", "Jacksonville", "Jacksonville", "Jacksonville",
             "ElPaso", "ElPaso", "ElPaso", "ElPaso", "ElPaso"],
    "month": ["January", "February", "March", "April", "May",
              "January", "February", "March", "April", "May"],
    "temperature": [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
}
weather = pd.DataFrame(data)
"""
+--------------+----------+-------------+
| city         | month    | temperature |
+--------------+----------+-------------+
| Jacksonville | January  | 13          |
| Jacksonville | February | 23          |
| Jacksonville | March    | 38          |
| Jacksonville | April    | 5           |
| Jacksonville | May      | 34          |
| ElPaso       | January  | 20          |
| ElPaso       | February | 6           |
| ElPaso       | March    | 26          |
| ElPaso       | April    | 2           |
| ElPaso       | May      | 43          |
+--------------+----------+-------------+
"""

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    weather = pd.pivot(weather, index='month', columns='city', values='temperature')
    return weather

print(pivotTable(weather))

"""
+----------+--------+--------------+
| month    | ElPaso | Jacksonville |
+----------+--------+--------------+
| April    | 2      | 5            |
| February | 6      | 23           |
| January  | 20     | 13           |
| March    | 26     | 38           |
| May      | 43     | 34           |
+----------+--------+--------------+
"""

################################################################################################
weather = pivotTable(weather)
month_order = ["January", "February", "March", "April", "May", "June", "July", "August", 
               "September", "October", "November", "December"]
sorted_months = [month for month in month_order if month in weather.index]

# 'month' became index, this doesn't work : 
#   weather["month"] = pd.Categorical(weather["month"], categories=month_order, ordered=True)
#   weather = weather.sort_values(by="month")

weather = weather.reindex(sorted_months)
print(weather)

"""
+----------+--------+--------------+
| month    | ElPaso | Jacksonville |
+----------+--------+--------------+
| January  | 20     | 13           |
| February | 6      | 23           |
| March    | 26     | 38           |
| April    | 2      | 5            |
| May      | 43     | 34           |
+----------+--------+--------------+
"""
