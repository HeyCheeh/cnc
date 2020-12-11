# Сначала нужно импортировать переменные conn и cur из файла database.py. Через эти переменные будет идти общение с бд.
from database import conn, cur

allertmesssage = 'Делаем запрос в базу данных'

# Использование fetchone()
# Начнем с использования функции fetchone(). Создадим переменную one_result для получения только одного результата:
# cur.execute("SELECT * FROM users;")
# one_result = cur.fetchone()
# print(allertmesssage)
# print(one_result)
# в итоге программа вернет данные о первом юзере

# Использование fetchmany()
# Если же нужно получить много данных, то используется функция fetchmany().
# Выполним другой скрипт для генерации 3 результатов:
# cur.execute("SELECT * FROM users;")
# three_results = cur.fetchmany(3) # Аргумент 3 показывает количество резальтатов в запросе
# print(allertmesssage)
# print(three_results)
# В итоге программа выведет три первых юзера

# Использование fetchall()
# Функцию fetchall() можно использовать для получения всех результатов. Вот что будет, если запустить скрипт:
cur.execute("SELECT * FROM vehicles;")
all_results = cur.fetchall()
print(allertmesssage)
print(all_results)

