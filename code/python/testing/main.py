import sys
import sqlite3 as sql3

class first_in:
    def __init__(self):
        self.command = None
    
    def login_in(self):
        while True:
            temp_login = str(input("Enter your login >> "))
            if temp_login == "exit":
                break
            else:
                cursor.execute("SELECT COUNT(*) FROM users WHERE login = ?", (temp_login,))
                row = cursor.fetchone()
                if row[0] > 0:
                    print("This login already exists")
                else:
                    temp_password = str(input("Enter your password >> "))
                    temp_password_repeat = str(input("Enter your password again >> "))
                    if temp_password == temp_password_repeat:
                        cursor.execute("INSERT INTO users (rights, login, password) VALUES (?, ?, ?)", ("listner", str(temp_login), str(temp_password)))
                        cursor.execute("CREATE TABLE " + str(temp_login) + " (id INTEGER PRIMARY KEY, id_music INTEGER, name TEXT, time INTEGER, kompozitor TEXT)")
                        listner1 = listner(temp_login)
                        listner1.listner_in_system()
                        break
                    else:
                        print("Try again")
    
    def sign_in(self):
        while True:
            temp_login = str(input("Enter your login >> "))
            if temp_login == "exit":
                break
            else:
                temp_password = str(input("Enter your password >> "))
                cursor.execute("SELECT * FROM users WHERE login = ?", (str(temp_login),))
                temp = cursor.fetchall()
                if temp_password == temp[0][3]:
                    if temp[0][1] == "listner":
                        listner1 = listner(temp_login)
                        listner1.listner_in_system()
                        break
                else:
                    print("Password incorrect, try again")                
            
    def login(self):
        while True:
            self.command = (input('Hello, enter command >> '))
            match self.command:
                case "login_in":
                    self.login_in()
                    break
                case "sign_in":
                    self.sign_in()
                    break
                case "exit":
                    break

class listner:
    exit = False
    def __init__(self, login): 
        self.login = login
        self.command = None
        self.my_music = []
        
    def print_music(self):
        cursor.execute("SELECT * FROM music")
        def print10rows():
            rows = cursor.fetchmany(10)
            for row in rows:
                print(f"{row[0]}. {row[1]} ({row[3]})")
        print10rows()
        while True:
            self.command = (input('Enter next >> '))
            match self.command:
                case "exit":
                    break
                case "next":
                    print10rows()

    def view_my_music(self):
        cursor.execute("SELECT * FROM " + str(self.login))
        def print10rows():
            rows = cursor.fetchmany(10)
            for row in rows:
                print(f"{row[0]}. {row[2]} ({row[4]})")
        print10rows()
        while True:
            self.command = (input('Enter next >> '))
            match self.command:
                case "exit":
                    break
                case "next":
                    print10rows()

    def exit(self):
        if self.command == "exit":
            self.exit = True

    def music_add(self):
        if self.command.startswith("music_add "):
            cursor.execute("SELECT * FROM music WHERE id = ?", ((int(self.command[len("music_add "):])),))
            temp = cursor.fetchall()
            cursor.execute("SELECT * FROM " + self.login + " WHERE id_music = ?", ((int(self.command[len("music_add "):])),))
            row = cursor.fetchone()
            if row is None:
                cursor.execute("INSERT INTO " + self.login + " (id_music, name, time, kompozitor) VALUES (?, ?, ?, ?)", (temp[0][0], temp[0][1], temp[0][2], temp[0][3]))
            else:
                print("Do you have this song in your music")

    def music_add_kompozitor(self):
        if self.command.startswith("music_add_kompozitor "):
            cursor.execute("SELECT * FROM music WHERE kompozitor = ?", ((str(self.command[len("music_add_kompozitor "):])),))
            temp = cursor.fetchall()
            for i in temp:
                cursor.execute("SELECT * FROM " + self.login + " WHERE id_music = ?", (str(i[0]),))
                row = cursor.fetchone()
                if row is None:
                    cursor.execute("INSERT INTO " + self.login + " (id_music, name, time, kompozitor) VALUES (?, ?, ?, ?)", (i[0], i[1], i[2], i[3]))

    def listner_in_system(self):
        while self.exit:
            self.command = (input('Enter command >> '))
            match self.command:
                case "music":
                    self.print_music()
                case "exit":
                    self.exit = 0
                case "view_my_music":
                    self.view_my_music()
                case _:
                    self.music_add()
                    self.music_add_kompozitor()

class kompozitor(listner):
    def __init__(self, login): 
        self.login = login
                            
if __name__ == '__main__':
    
    conn = sql3.connect('example.db')
    cursor = conn.cursor()

    start = first_in()
    start.login()

    conn.commit()
    conn.close() # close connect with database 