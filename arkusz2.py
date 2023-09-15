import pandas
import pandas as pd

data = pandas.read_excel('Courses.xlsx')

# df = pd.DataFrame(data)
df = pd.DataFrame(data, columns=['Courses', 'Fee'])
print(df)
#    Unnamed: 0 Courses    Fee Duration  Discount
# 0           0   Spark  25000  50 Days      2000
# 1           1  Pandas  20000  35 Days      1000
# 2           2  Python  15000      NaN       800
# 3           3     PHP  18000  30 Days       500
#   Courses    Fee
# 0   Spark  25000
# 1  Pandas  20000
# 2  Python  15000
# 3     PHP  18000

print(df.columns[0])
print(df.values[0])