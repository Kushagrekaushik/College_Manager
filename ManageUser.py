from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox, Treeview
import pymysql
from tkcalendar import DateEntry
from PIL import ImageTk, Image

class UserClass:
    def __init__(self,manageuser):
        self.home = Toplevel(manageuser)
        w = self.home.winfo_screenwidth()
        h = self.home.winfo_screenheight()
        self.home.minsize(w-100,h-180)
        self.home.geometry("%dx%d+%d+%d"%(w-100,h-180,50,70))

        #----------------- widgets ---------------------------
        self.hlbl = Label(self.home,text="User",font=('Clarendon BT',40),background='#E9C5FF',
                          foreground='#550685',relief='groove',borderwidth=5)
        self.L1 = Label(self.home,text="Username")
        self.L2 = Label(self.home,text="Password")
        self.L3 = Label(self.home,text="User Type")
        self.t1 = Entry(self.home)
        self.t2 = Entry(self.home,show='*')
        self.v1 = StringVar()
        self.c1 = Combobox(self.home,values=("Admin","Employee"), textvariable=self.v1)

        # ----------- table -----------------------------
        self.tablearea = Frame(self.home)
        self.mytable = Treeview(self.tablearea, columns=['c1', 'c2'], height=10)
        self.mytable.heading("c1", text="User Name")
        self.mytable.heading("c2", text="User Type")
        self.mytable['show'] = 'headings'

        self.mytable.column("#1", width=200, anchor='center')
        self.mytable.column("#2", width=200, anchor='center')
        self.mytable.bind("<ButtonRelease-1>",lambda e : self.getpk())

        self.mytable.pack()

        #------------- buttons --------------
        self.b1 = Button(self.home,text='Save',foreground='white',background='#550685',command=self.savedata)
        self.b2 = Button(self.home,text='Fetch',foreground='white',background='#550685',command=self.fetchdata)
        self.b3 = Button(self.home,text='Update',foreground='white',background='#550685',command=self.Updatedata)
        self.b4 = Button(self.home,text='Delete',foreground='white',background='#550685',command=self.Deletedata)
        self.b5 = Button(self.home,text='Search',foreground='white',background='#550685',command=self.fetchalldata)

        # ----------- placements ------------------------
        self.hlbl.place(x=0,y=0,width=w-100,height=70)
        x1 = 50
        y1 = 100
        x_diff=100
        y_diff=50

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)
        self.b2.place(x=x1+x_diff+x_diff+50,y=y1)
        self.tablearea.place(x=x1+x_diff+x_diff+x_diff+50,y=y1)

        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)
        self.b5.place(x=x1+x_diff+x_diff+50,y=y1)

        y1+=y_diff
        self.b1.place(x=x1,y=y1,width=100)
        self.b3.place(x=x1+x_diff,y=y1,width=100)
        self.b4.place(x=x1+x_diff+x_diff,y=y1,width=100)

        self.clearPage()
        self.home.mainloop()


    def dataconnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="manage_data",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while database connection : "+str(e),parent=self.home)

    def savedata(self):
        self.dataconnection()
        try:
            qry = "insert into usertable values(%s,%s,%s)"
            rowcount = self.curr.execute(qry,(self.t1.get(),self.t2.get(),self.v1.get()))
            self.conn.commit()
            if(rowcount==1):
                messagebox.showinfo("Success","User Record Saved Successfully",parent=self.home)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion : "+str(e),parent=self.home)

    def Updatedata(self):
        self.dataconnection()
        try:
            qry = " update usertable set password=%s, usertype=%s  where username=%s"
            rowcount = self.curr.execute(qry,(self.t2.get(), self.v1.get(),self.t1.get()))
            self.conn.commit()
            if(rowcount==1):
                messagebox.showinfo("Success","User Record Updated Successfully",parent=self.home)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error","Error while updating  : "+str(e),parent=self.home)

    def Deletedata(self):
        ans = messagebox.askquestion("Confirmation","Are you sure to delete ??",parent=self.home)
        if ans=="yes":
            self.dataconnection()
            try:
                qry = " delete from usertable where username=%s"
                rowcount = self.curr.execute(qry,(self.t1.get()))
                self.conn.commit()
                if(rowcount==1):
                    messagebox.showinfo("Success","User Record Deleted Successfully",parent=self.home)
                    self.clearPage()
            except Exception as e:
                messagebox.showerror("Query Error","Error while deletion  : "+str(e),parent=self.home)

    def getpk(self):
        rowid = self.mytable.focus()
        content = self.mytable.item(rowid)
        values = content['values']
        pk = values[0]
        self.fetchdata(pk)

    def fetchdata(self,pk=None):
        if pk==None:
            un = self.t1.get()
        else:
            un=pk
        self.dataconnection()
        try:
            qry = "select * from usertable where username=%s"
            rowcount = self.curr.execute(qry,(un))
            data = self.curr.fetchone()
            # print("data = ",data)
            self.clearPage()
            if data:
                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])
                self.v1.set(data[2])

                self.b3['state'] = 'normal'
                self.b4['state'] = 'normal'
            else:
                messagebox.showwarning("No Record","User Record Not Found",parent=self.home)
        except Exception as e:
            messagebox.showerror("Query Error","Error while fetching : "+str(e),parent=self.home)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.c1.set("Choose Usertype")
        self.b3['state']='disabled'
        self.b4['state']='disabled'

    def fetchalldata(self):
        self.dataconnection()
        self.mytable.delete(*self.mytable.get_children())
        try:
            utype =self.v1.get()
            if utype=="Choose Usertype":
                utype=""
            qry = "select * from usertable where usertype like %s "
            rowcount = self.curr.execute(qry,(utype+"%"))
            data = self.curr.fetchall()
            if data:
                for row in data:
                    myrow = [row[0],row[2]]
                    self.mytable.insert("",END,values=myrow)
            else:
                messagebox.showwarning("No Record","User Record Not Found",parent=self.home)
        except Exception as e:
            messagebox.showerror("Query Error","Error while fetching : "+str(e),parent=self.home)



if __name__ == '__main__':
    dummyHomepage=Tk()
    UserClass(dummyHomepage)
    dummyHomepage.mainloop()
























