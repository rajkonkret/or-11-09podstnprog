import pandas as pd
# pip install pandas
# python.exe -m pip install --upgrade pip

data = pd.read_csv('records.csv', delimiter='^')
print(data)
#     name branch  year  cgpa
# 0  Tomek    COE     3   9.1
# 1  Tomek    COE     2   9.0
# 2  Tomek    COE     1   8.1
# 3  radek    coe     3   9.1

print(data.columns)
print(data.values)
# Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
# [['Tomek' 'COE' 3 9.1]
#  ['Tomek' 'COE' 2 9.0]
#  ['Tomek' 'COE' 1 8.1]
#  ['radek' 'coe' 3 9.1]]