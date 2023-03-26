"""
The Single Responsibility Principle (SRP)
The idea behind the SRP is that every class, module, or function in a program should have one responsibility/purpose in a program
example:
user register to data base and if any error save in system log .
if user is created send eamil to user .
"""
import sqlite3 
import syslog

class User:
    con = sqlite3.connect("./userdb.db")
    def register(self,username,email,pwd):
        # self.__create_table_if_exist()
        sql = f"""INSERT INTO user (username,email,password) VALUES('{username}','{email}','{pwd}')"""
        self.con.execute(sql)
        self.con.commit()

    # def __create_table_if_exist(self):
    #     sql = """
    #     CREATE TABLE  IF NOT EXISTS user (
    #        username VARCHAR(100) PRIMARY KEY NOT NULL UNIQUE,
    #        email VARCHAR(150)  NOT NULL UNIQUE,
    #        password VARCHAR(150)  NOT NULL
    #     ) 
    #     """
        # self.con.execute(sql)
        # self.con.commit()




class Logger:
    def write_log_to_system(self,messsage):
        syslog.syslog(syslog.LOG_ERR,messsage) 




class Email:

    def sendEmail(self,email):
            print(f"email sent to {email}")





class Registration:
    def registerUser(self,email,username,password):
        try:
            User().register(username,email,password)
            Email().sendEmail(email=email)
        except Exception as e :
            print(str(e))
            Logger().write_log_to_system(str(e))



r = Registration()
r.registerUser('200mou3a200@gmail.com','mos3sa','12345')