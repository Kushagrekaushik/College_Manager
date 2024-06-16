from tkinter import messagebox
import pymysql
class MainClass:
    def __init__(self):
        self.dataconnection()
        try:
            qry = "select * from usertable"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchall()
            if data:
                from loginpage import LoginClass
                LoginClass()
            else:
                from Admin import CreateAdminClass
                CreateAdminClass()
        except Exception as e:
            messagebox.showerror("Query Error", "Error while fetching : " + str(e))


    def dataconnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="manage_data",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while database connection : "+str(e))


if __name__ == '__main__':
    MainClass()