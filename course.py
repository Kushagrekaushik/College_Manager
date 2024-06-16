from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
from tkcalendar import DateEntry

import pymysql

class course:
    def __init__(self,coursewindow):
        self.home=coursewindow
        self.home=Toplevel(coursewindow)
        self.home.state("zoomed")
        w = self.home.winfo_screenwidth()
        h = self.home.winfo_screenheight()
        self.home.minsize(w - 100, h - 180)
        self.home.geometry("%dx%d+%d+%d" % (w - 100, h - 180, 50, 70))
#         Widgets
        self.back=Label(self.home,text="Course",font=('Clarendon BT',40),
                        background='#E9C5FF',foreground='#550685',relief='groove',borderwidth=5)
        self.l1=Label(self.home,text="Departments")
        self.l2=Label(self.home,text="Course")
        self.l3=Label(self.home,text="Duration")
        self.l4=Label(self.home,text="Fee")


        self.v1=StringVar()
        self.c1=Combobox(self.home,textvariable=self.v1)
        self.t2=Entry(self.home)
        self.t3=Entry(self.home)
        self.t4=Entry(self.home)

        self.tablearea = Frame(self.home)
        self.table1 = Treeview(self.tablearea, columns=['c1', 'c2', 'c3', 'c4'],
                               height=25)
        self.table1.heading("c1", text="Departments")
        self.table1.heading("c2", text="Course")
        self.table1.heading("c3", text="Duration")
        self.table1.heading("c4", text="Fee")

        self.table1['show'] = 'headings'

        self.table1.column("#1", width=100, anchor='center')
        self.table1.column("#2", width=100, anchor='center')
        self.table1.column("#3", width=100, anchor='center')
        self.table1.column("#4", width=70, anchor='center')

        self.table1.bind("<ButtonRelease-1>", lambda e: self.getpk())
        self.table1.pack()

#         Buttons
        self.b1=Button(self.home,text="Save",foreground='white',background='#550685',command=self.savedata)
        self.b2=Button(self.home,text="Fetch",foreground='white',background='#550685',command=self.fetchdata)
        self.b3=Button(self.home,text="Update",foreground='white',background='#550685',command=self.Updatedata)
        self.b4=Button(self.home,text="Delete",foreground='white',background='#550685',command=self.Deletedata)
        self.b5=Button(self.home,text="Search",foreground='white',background='#550685',command=self.fetchalldata)


        self.back.place(x=0, y=0, width=w - 100, height=70)
        x1 = 50
        y1 = 100
        x_diff = 130
        y_diff = 50

        self.l1.place(x=x1, y=y1)
        self.c1.place(x=x1 + x_diff, y=y1)
        self.b5.place(x=x1 + x_diff + x_diff + 50, y=y1)
        self.tablearea.place(x=x1 + x_diff + x_diff + x_diff + 50, y=y1)

        y1 += y_diff
        self.l2.place(x=x1, y=y1)
        self.t2.place(x=x1 + x_diff, y=y1)
        self.b2.place(x=x1 + x_diff + x_diff + 50, y=y1)

        y1 += y_diff
        self.l3.place(x=x1, y=y1)
        self.t3.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.l4.place(x=x1, y=y1)
        self.t4.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.b1.place(x=x1, y=y1, width=100)
        self.b3.place(x=x1 + x_diff , y=y1,width=100)
        self.b4.place(x=x1 + x_diff + x_diff ,y=y1,width=100)
        self.clearPage()
        self.fetchAlldept()
        self.home.mainloop()
    def dataconnection(self):
        try:
            self.conn=pymysql.connect(host="localhost",db="manage_data",user="root",password="")
            self.curr=self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Data base Error"+str(e),parent=self.home)
    def savedata(self):
        self.dataconnection()
        try:
            qry="insert into course_data value(%s,%s,%s,%s)"
            rowcount=self.curr.execute(qry,(self.v1.get(),self.t2.get(),self.t3.get(),self.t4.get()))
            self.conn.commit()
            if(rowcount==1):
                messagebox.showinfo("Success","course Saved successfully",parent=self.home)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion  : " + str(e), parent=self.home)
    def Updatedata(self):
        self.dataconnection()
        try:
            qry=" update course_data set Departments=%s, Duration=%s, Fee=%s  where Course=%s"
            rowcount=self.curr.execute(qry,(self.v1.get(),self.t3.get(),self.t4.get(),self.t2.get()))
            self.conn.commit()
            if (rowcount == 1):
                messagebox.showinfo("Success", "course Updated successfully", parent=self.home)
            self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error", "Error while updating : " + str(e), parent=self.home)
    def Deletedata(self):


        ans = messagebox.askquestion("Confirmation", "Are you sure to delete ??",parent=self.home)
        if ans == "yes":
            self.dataconnection()
            try:
                qry = " delete from course_data where Course=%s"
                rowcount = self.curr.execute(qry, (self.t2.get()))
                self.conn.commit()
                if (rowcount == 1):
                    messagebox.showinfo("Success", " course Deleted Successfully", parent=self.home)
                    self.clearPage()
            except Exception as e:
                messagebox.showerror("Query Error", "Error while deletion  : " + str(e), parent=self.home)

    def getpk(self):
        rowid = self.table1.focus()
        content = self.table1.item(rowid)
        values = content['values']
        pk = values[1]
        self.fetchdata(pk)



    def fetchdata(self,pk=None):
        if pk == None:
            Course = self.t2.get()
        else:
            Course  = pk
        self.dataconnection()
        try:
            qry="select * from course_data where Course = %s"
            rowcount=self.curr.execute(qry,(Course))
            data=self.curr.fetchone()
            self.clearPage()
            if data:

                self.v1.set(data[0])
                self.t2.insert(0,data[1])
                self.t3.insert(0,data[2])
                self.t4.insert(0,data[3])

                self.b3['state'] = 'normal'
                self.b4['state'] = 'normal'
            else:
                messagebox.showwarning("No Record","Course Not Found",parent=self.home)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion connection : "+str(e),parent=self.home)
    def fetchalldata(self):
        self.dataconnection()
        self.table1.delete(*self.table1.get_children())
        try:
            dept = self.v1.get()
            if dept == "Choose Department":
                dept = ""
            qry='select * from course_data where  Departments like %s '
            rowcount=self.curr.execute(qry,(dept+"%"))

            data=self.curr.fetchall()
            if data:
                for row in data:
                    self.table1.insert("",END,values=row)
            else:
                messagebox.showwarning("No course data found ",parent=self.home)
        except Exception as e:
            messagebox.showerror("Query Error "+str(e),parent=self.home)

    def clearPage(self):
        self.v1.set(None)
        self.t2.delete(0, END)
        self.t3.delete(0, END)
        self.t4.delete(0,END)


        self.b3['state'] = 'disabled'
        self.b4['state'] = 'disabled'

    def fetchAlldept(self):
        self.dataconnection()
        try:
            qry = "select * from department_data"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchall()

            self.deptList = []
            if data:
                self.c1.set("Choose Department")
                for row in data:
                    self.deptList.append(row[0])
                self.c1.set("No Department")

            self.c1.config(values=self.deptList)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while fetching : " + str(e), parent=self.home)



if __name__ == '__main__':
    dummyHomepage=Tk()
    course(dummyHomepage)
    dummyHomepage.mainloop()