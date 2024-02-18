import sqlite3 as sql3

conn = sql3.connect('example.db')
cursor = conn.cursor()

# Выполняем запрос на удаление таблицы
cursor.execute("DROP TABLE IF EXISTS SoVa")

# Выполняем запрос на удаление строки из таблицы
cursor.execute("DELETE FROM users WHERE id = 1")

# Сохраняем изменения
conn.commit()

# Закрываем соединение с базой данных
conn.close()