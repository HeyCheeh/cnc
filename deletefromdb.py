# Сначала нужно импортировать переменные conn и cur из файла database.py. Через эти переменные будет идти общение с бд.
from database import conn, cur

# Предположим, нам н адо удалить юзера с фамилией Фамилия3
# скрипт для удаления
cur.execute("DELETE FROM users WHERE lname='Фамилия3';")
conn.commit()
print('Данные удалены')


# Если затем сделать следующей запрос:
cur.execute("select * from users where lname='Фамилия3'")
print(cur.fetchall())
# Будет выведен пустой список, подтверждающий, что запись удалена.