import sqlite3
import pandas as pd

con = sqlite3.connect('testdb.db')
df = pd.read_sql("SELECT * from vehicles", con)
#df.to_excel('xxl.xls', index = False)
# excel = pd.read_excel('xxl.xls')
print(df)
# print(excel[''])
# for x in df.values:
#     print(x)

