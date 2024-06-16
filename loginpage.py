from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
class LoginClass:
    def __init__(self):
        self.window = Tk()
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()

        self.window.geometry("%dx%d+%d+%d"%(500,400,550,200))

        #----------------- widgets ---------------------------
        self.hlbl = Label(self.window,text="Welcome",font=('Clarendon BT',40),background='#E9C5FF',
                          foreground='#550685',relief='groove',borderwidth=5)
        self.L1 = Label(self.window,text="Username")
        self.L2 = Label(self.window,text="Password")

        self.t1 = Entry(self.window)
        self.t2 = Entry(self.window,show='*')


        #------------- buttons --------------
        self.b1 = Button(self.window,text='Login',foreground='white',
                         background='#550685',command=self.CheckData)

        # ----------- placements ------------------------
        self.hlbl.place(x=0,y=0,width=503,height=70)
        x1 = 50
        y1 = 100
        x_diff=100
        y_diff=50

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.b1.place(x=x1,y=y1,width=100)
        self.clearPage()
        self.window.mainloop()


    def dataconnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="manage_data",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while database connection : "+str(e),parent=self.window)

    def CheckData(self):
        self.dataconnection()
        try:
            qry = "select * from usertable where username=%s and password=%s"
            rowcount = self.curr.execute(qry, (self.t1.get(),self.t2.get()))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                uname=data[0]
                utype=  data[2]
                messagebox.showinfo("No Record", "Hello "+uname+"\n"+utype, parent=self.window)

                self.window.destroy()
                from Homepage_project import homepage
                homepage(uname,utype)

            else:
                messagebox.showwarning("No Record", "Wrong username or password", parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while fetching : " + str(e), parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)


if __name__ == '__main__':
    LoginClass()
























