import sqlite3 as sql3

conn = sql3.connect('example.db')
cursor = conn.cursor()

#cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, rights TEXT, name TEXT, password TEXT, my_music TEXT)")     "10 20 35 1".split(" ") [10,20,35,1]


cursor.execute("SELECT * FROM music")
rows1 = cursor.fetchall()
for row in rows1:
    print(row)

cursor.execute("SELECT * FROM music WHERE kompozitor = ?", ("10AGE",))

rows = cursor.fetchall()

for row in rows:
    print("ID:", row[0])
    print("Название песни:", row[1])
    print("Продолжительность:", str(row[2] // 60) + ":" + str(row[2] % 60))
    print("Исполнитель:", row[3], end="\n\n")

conn.close() # close connect with data base 



'''
---------------------------------
writing to the database (music)
---------------------------------
cursor.execute("INSERT INTO music (name, time, kompozitor) VALUES (?, ?, ?)", ('Отпускай', 127, 'Апология'))
cursor.execute("INSERT INTO music (name, time, kompozitor) VALUES (?, ?, ?)", ('Так не интересно', 138, 'Aikko'))
cursor.execute("INSERT INTO music (name, time, kompozitor) VALUES (?, ?, ?)", ('Пушка', 203, '10AGE'))
cursor.execute("INSERT INTO music (name, time, kompozitor) VALUES (?, ?, ?)", ('Перезвоню', 188, 'ATRLLWULF'))
cursor.execute("INSERT INTO music (name, time, kompozitor) VALUES (?, ?, ?)", ('Дофамин', 113, 'Marvin'))
cursor.execute("INSERT INTO music (name, time, kompozitor) VALUES (?, ?, ?)", ('Пустота', 210, 'МУККА'))
cursor.execute("INSERT INTO music (name, time, kompozitor) VALUES (?, ?, ?)", ('Эйя', 171, 'Канги'))
cursor.execute("INSERT INTO music (name, time, kompozitor) VALUES (?, ?, ?)", ('Каждый кто делал тебе больно', 213, 'забей, лерочка'))
cursor.execute("INSERT INTO music (name, time, kompozitor) VALUES (?, ?, ?)", ('Позови мен с собой 2.0', 81, 'KARUM'))
cursor.execute("INSERT INTO music (name, time, kompozitor) VALUES (?, ?, ?)", ('Зоопарк', 180, '10AGE'))
cursor.execute("INSERT INTO music (name, time, kompozitor) VALUES (?, ?, ?)", ('Ау', 180, '10AGE'))
cursor.execute("INSERT INTO music (name, time, kompozitor) VALUES (?, ?, ?)", ('Равнодушие', 183, 'Мальбэк feat. Сюзанна'))
'''

'''
---------------------------------
writing to the database
---------------------------------
cursor.execute("SELECT * FROM music")
rows = cursor.fetchall()
for row in rows:
    print(row)
'''

'''
for i, elem in enumerate(BD):
    print(f"{i + 1}. {elem.name} ({elem.kompozitor})")
'''

'''
import sys
import sqlite3

# Устанавливаем соединение с базой данных
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Выполняем запрос к базе данных
cursor.execute("SELECT * FROM music")

# Получаем первые 10 строк результата запроса
rows = cursor.fetchmany(10)

# Выводим полученные строки
for row in rows:
    print(row)
print(len(rows))

rows = cursor.fetchmany(10)

for row in rows:
    print(row)
print(len(rows))

# Закрываем соединение с базой данных
conn.close()

'''