# Сначала нужно импортировать переменные conn и cur из файла database.py. Через эти переменные будет идти общение с бд.
from database import conn, cur
from  Pandas_Table1 import excel, con
import pandas as pd

# создадим техническое уведомление, которое будем выводить в терминал, когда отработает функция
dataexecuted = 'Данные успешно записаны в базу'
#
# # далее попробуем добавить одного юзера
# cur.execute("""INSERT INTO users(userid, fname, lname, gender, usertype)
#     VALUES('00001', 'Yuri', 'Borisov', 'male', 'admin');""")
# conn.commit()
# print(dataexecuted) # когда юзер добавлен, выводим уведомление в консоль

# также мы можем сначала создать кортеж с информацией о юзере, а потом загрузить его в бд
# создаем кортеж
#new_vehicle = ('inv_key', 'inv_name', 'inv_type', 'value', 'date', 'version_date', 'version_name')
# new_vehicle = df.values
# print(new_vehicle)
# print(excel)
# а теперь добавим юзера в таблицу users
# cur.executemany("INSERT INTO vehicles VALUES(?, ?, ?, ?, ?, ?, ?);", excel)
# conn.commit()
# В данном случае все значения заменены на '?' и добавлен параметр, содержащий значения, которые нужно добавить.
#print(dataexecuted) # когда юзер добавлен, выводим уведомление в консоль
#
# # Также мы можем создать переменную с набором кортежей, содержащщих информацию о юзере.
# # В таком случае мы сможем добавить в бд сразу несколько юзеров за раз
# several_users_to_db = [('00003', 'Имя1', 'Фамилия1', 'male', 'manager'),
#                        ('00004', 'Имя2', 'Фамилия2', 'female', 'manager'),
#                        ('00005', 'Имя3', 'Фамилия3', 'female', 'manager')]
# # А теперь пишем кортеж с данными в БД (используем не execute, а executemany)
# cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?);", several_users_to_db)
# conn.commit()
# print(dataexecuted) # когда юзер добавлен, выводим уведомление в консоль
# # Также стоит помнить, что способ с ? помогает логически противостоять разным SQL-инъекциям
# for df in excel.items():
#     df.to_sql(tab, conn, index=False, if_exists='replace')
inv_key = excel['inv_key']
inv_name = excel['inv_name']
inv_type = excel['inv_type']
value = excel['value']
date = excel['date']
version_date = excel['version_date']
version_name = excel['version_name']
newpd = pd.concat([inv_key, inv_name, inv_type, value, date, version_date, version_name], axis=1)
newpd.to_sql('vehicles', con,if_exists='append',index=False)


# cur.executemany("INSERT INTO vehicles VALUES(?, ?, ?, ?, ?, ?, ?);", newpd)
# conn.commit()
# import pandas as pd
# import sqlite3
#
# fn = r'D:\temp\test.xlsx'
#
# # read & parse all excel sheets into a dictionary (keys - sheet names, values - pandas DataFrames)
# dfs = pd.read_excel(fn, sheet_name=None)
#
# conn = sqlite3.connect(r'D:\temp\output.sqlite')
#
# # save DataFrames as SQLite tables
# for tab, df in dfs.items():
#     df.to_sql(tab, conn, index=False, if_exists='replace')