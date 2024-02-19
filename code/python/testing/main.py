import sqlite3 as sql3

class first_in:
    def __init__(self):
        self.command = None
        self.listner_commands = [["music", " - print all music."], 
                            ["exit", " - exit programm."], 
                            ["view_my_music", " - print your music."], 
                            ["music_add ", " - add to your music by number."], 
                            ["music_add_kompozitor ", " - add to your music by kompozitor."]]
        self.kompozitor_commands = [["create_music", " - create your new music."],
                                    ["view_my_music_kompozitor", " - print your music (kompozitor)."],
                                    ["del_your_music_kompozitor", " - delete your music."]]
        self.administrator_commands = [["changing_users", " - changing users."],
                                       ["view_all_users", " - show all users."],
                                       ["del_music", " - delete music."]]
    
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
                        print("\nAll listner commands: ")
                        for i in self.listner_commands:
                            print(f"{i[0]}{i[1]}")
                        listner1.in_system()
                        break
                    else:
                        print("Try again")
    
    def sign_in(self):
        while True:
            temp_login = str(input("Enter your login >> "))
            cursor.execute("SELECT COUNT(*) FROM users WHERE login = ?", (temp_login,))
            row_count = cursor.fetchone()[0]
            if temp_login == "exit":
                break
            elif row_count > 0:
                temp_password = str(input("Enter your password >> "))
                cursor.execute("SELECT * FROM users WHERE login = ?", (str(temp_login),))
                temp = cursor.fetchall()
                if temp_password == temp[0][3]:
                    match temp[0][1]:
                        case "listner":
                            print("\nAll listner commands: ")
                            for i in self.listner_commands:
                                print(f"{i[0]}{i[1]}")
                            print("")
                            listner1 = listner(temp_login)
                            listner1.in_system()
                        case "kompozitor":
                            print("\nAll listner commands: ")
                            for i in self.listner_commands:
                                print(f"{i[0]}{i[1]}")
                            print("")
                            print("All kompozitor commands: ")
                            for i in self.kompozitor_commands:
                                print(f"{i[0]}{i[1]}")
                            print("")
                            kompozitor1 = kompozitor(temp_login)
                            kompozitor1.in_system()
                        case "administrator":
                            print("\nAll listner commands: ")
                            for i in self.listner_commands:
                                print(f"{i[0]}{i[1]}")
                            print("")
                            print("All kompozitor commands: ")
                            for i in self.kompozitor_commands:
                                print(f"{i[0]}{i[1]}")
                            print("")
                            print("All administrator commands: ")
                            for i in self.administrator_commands:
                                print(f"{i[0]}{i[1]}")
                            print("")
                            administrator1 = administrator(temp_login)
                            administrator1.in_system()
                    break
                else:
                    print("Password or login incorrect, try again")                
            
    def login(self):
        while True:
            self.command = (input('Hello, login_in/sign_in >> '))
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
        
    def print_music(self):
        cursor.execute("SELECT * FROM music")
        def print10rows():
            rows = cursor.fetchmany(10)
            for row in rows:
                print(f"{row[0]}. {row[1]} ({row[3]})")
        print10rows()
        while True:
            self.command = (input('Enter next/exit >> '))
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
            self.command = (input('Enter next/exit >> '))
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
   
    def in_system(self):
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
        self.command = None

    def create_music(self):
        while True:
            temp_name_newmusic = input("Enter name your new music >> ")
            if temp_name_newmusic == "exit":
                break
            else:
                cursor.execute("SELECT COUNT(*) FROM music WHERE name = ?", (temp_name_newmusic,)) 
                row = cursor.fetchone()
                if row[0] > 0:
                    print("This name is already in use")
                else:
                    temp_time_newmusic = input("Enter the duration of your music >> ")
                    cursor.execute("INSERT INTO music (name, time, kompozitor) VALUES (?, ?, ?)", (temp_name_newmusic, temp_time_newmusic, self.login))
                    break

    def view_my_music_kompozitor(self):
        cursor.execute("SELECT * FROM music WHERE kompozitor = ?", (self.login,)) 
        rows = cursor.fetchall()
        print("")
        for row in rows:
            print("ID: ", row[0])
            print("Name music: ", row[1])
            print("Time: ", str(row[2] // 60) + ":" + str(row[2] % 60))
            print("Kompozitor: ", row[3], end="\n\n")
    
    def del_your_music_kompozitor(self):
        while True:
            temp = input("Enter name your music for delete >> ")
            if temp != "exit":
                cursor.execute("SELECT * FROM music WHERE name = ?", (temp,))
                row = cursor.fetchone()
                if row is not None:
                    if row[3] == self.login:
                        cursor.execute("DELETE FROM music WHERE id = ?", (row[0],))
                        break
                    else:
                        print("You cant delete this music.")
                else:
                    print("This name is not found.")
            else:
                break
   
    def in_system(self):
        while self.exit:
            self.command = (input('Enter command >> '))
            match self.command:
                case "music":
                    self.print_music()
                case "exit":
                    self.exit = 0
                case "view_my_music":
                    self.view_my_music()
                case "create_music":
                    self.create_music()
                case "view_my_music_kompozitor":
                    self.view_my_music_kompozitor()
                case "del_your_music_kompozitor":
                    self.del_your_music_kompozitor()
                case _:
                    self.music_add()
                    self.music_add_kompozitor()

class administrator(kompozitor, listner):
    def __init__(self, login): 
        self.login = login
        self.command = None

    def changing_users(self):
        while True:
            temp = input("Enter what you know about the user, login/ID >> ")
            match temp:
                case "exit":
                    break
                case "ID":
                    temp_ID = str(input("ENter ID >> "))
                    temp = input("Which parameter do you want to change >> ")
                    temp_value = input("Enter what you want to replace it with >> ")
                    cursor.execute("UPDATE users SET " + temp + " = ? WHERE id = ?", (temp_value,temp_ID))
                case "login":
                    temp_login = str(input("ENter login >> "))
                    temp = input("Which parameter do you want to change >> ")
                    temp_value = input("Enter what you want to replace it with >> ")
                    cursor.execute("UPDATE users SET " + temp + " = ? WHERE login = ?", (temp_value,temp_login))
    
    def view_all_users(self):
        cursor.execute("SELECT * FROM users")
        def print10rows():
            rows = cursor.fetchmany(10)
            for row in rows:
                print("")
                print("ID: ", row[0])
                print("Rights: ", row[1])
                print("Login: " , row[2])
                print("Password: ", row[3], end="\n\n")
        print10rows()
        while True:
            self.command = (input('Enter next/exit >> '))
            match self.command:
                case "exit":
                    break
                case "next":
                    print10rows()

    def del_music(self):
        while True:
            temp = input("Enter the parameter by which you want to delete the music id/name/kompozitor >> ")
            if temp != "exit":
                temp2 = input("Enter parameter >> ")
                if temp2 != "exit":
                    match temp:
                        case "id":
                            cursor.execute("DELETE FROM music WHERE id = ?", (temp2,))
                        case "name":
                            cursor.execute("DELETE FROM music WHERE name = ?", (temp2,))
                        case "kompozitor":
                            cursor.execute("DELETE FROM music WHERE kompozitor = ?", (temp2,))

            else:
                break
    
    def in_system(self):
        while self.exit:
            self.command = (input('Enter command >> '))
            match self.command:
                case "music":
                    self.print_music()
                case "exit":
                    self.exit = 0
                case "view_my_music":
                    self.view_my_music()
                case "create_music":
                    self.create_music()
                case "view_my_music_kompozitor":
                    self.view_my_music_kompozitor()
                case "del_your_music_kompozitor":
                    self.del_your_music_kompozitor()
                case "changing_users":
                    self.changing_users()
                case "view_all_users":
                    self.view_all_users()
                case "del_music":
                    self.del_music()
                case _:
                    self.music_add()
                    self.music_add_kompozitor()
                            
if __name__ == '__main__':
    
    conn = sql3.connect('example.db')
    cursor = conn.cursor()

    start = first_in()
    start.login()

    conn.commit()
    conn.close() # close connect with database 