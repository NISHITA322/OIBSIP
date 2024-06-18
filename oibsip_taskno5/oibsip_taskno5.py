# NISHITA KADIYA

                # Oasis infobyte
            # Task 5 : Chat Application

import tornado.ioloop
import tornado.web
import tornado.escape
import tornado.websocket
import sqlite3
import os

#  for database connectivity
def get_conn1():
    print("connecting")
    db_conn = sqlite3.connect('stu1.db')
    return db_conn

#  for database setup
def setup1():
    if not os.path.exists('stu1.db'):
        db_conn = get_conn1()
        connection = db_conn.cursor()
        connection.execute('''
                create table if not exists stu1(
                           stuid INTEGER PRIMARY KEY AUTOINCREMENT,
                           name1 TEXT unique NOT NULL,
                           pwd1 TEXT NOT NULL)
        ''')
        db_conn.commit()
        db_conn.close()

# empty list that stores users name
client_list = []

# Registration
class Main1(tornado.web.RequestHandler):
    def get(self):
        print("getting register page")
        self.render("register.html")

    def post(self):
        print("post request working")
        uname1 = self.get_argument("uname1")
        pwd1 = self.get_argument("pwd1")
        db_conn = get_conn1()
        connection = db_conn.cursor()

        try:
            connection.execute('INSERT INTO stu1 (name1, pwd1) VALUES (?, ?)',(uname1,pwd1))
            db_conn.commit()
            self.render("login.html")
        except sqlite3.IntegrityError:
            self.render("register.html")
        finally:
            db_conn.close() 

# login
class Login1(tornado.web.RequestHandler):
    def get(self):
        print("getting login page")
        self.render("login.html")

    def post(self):
        print("post request working")
        uname1 = self.get_argument("uname1")
        pwd1 = self.get_argument("pwd1")

        db_conn = get_conn1()
        connection = db_conn.cursor()
        connection.execute('SELECT * FROM stu1 WHERE name1 = ? AND pwd1 = ?',(uname1,pwd1))
        user1 = connection.fetchone()
        #connection.close()
        db_conn.close()

        if user1:
            print("user found")
            self.set_secure_cookie("user",uname1)
            self.render("chatt.html")
        else:
            print("user not found")
            self.render("login.html")

# logout
class Logout1(tornado.web.RequestHandler):
    def get(self):
        print("logout the user by cookie value")
        self.clear_cookie("user")
        self.redirect("/")

# chat message 
class Chat1(tornado.websocket.WebSocketHandler):
    def open(self):
        if not self.get_secure_cookie("user"):
            self.close()
        else:
            client_list.append(self)

    def on_message(self, message):
        get_user = self.get_secure_cookie("user").decode()
        for client in client_list:
            client.write_message(f"{get_user} : {message}")

    def on_close(self):
        client_list.remove(self)

# chat_page render
class chat_page1(tornado.web.RequestHandler):
    def get(self):
        print("chat page")
        if not self.get_secure_cookie("uname1"):
            self.render("login.html")
        else:
            self.render("chatt.html")

# main function that call chat app
def app1():
    return tornado.web.Application([
        (r"/",Main1),
        (r"/login",Login1),
        (r"/page",chat_page1),
        (r"/ws",Chat1),
        (r"/logout",Logout1),
    ], cookie_secret="YOUR_SECRET_KEY")

if __name__ == "__main__":
    setup1()
    app = app1()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()









            
