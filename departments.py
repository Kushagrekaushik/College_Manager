from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
from tkcalendar import DateEntry
class DepartmentClass:
    def __init__(self,Department_window):
        self.home = Department_window
        self.home = Toplevel(Department_window)
        self.home.state("zoomed")
        w = self.home.winfo_screenwidth()
        h = self.home.winfo_screenheight()
        self.home.minsize(w - 100, h - 180)
        self.home.geometry("%dx%d+%d+%d" % (w - 100, h - 180, 50, 70))
        self.back = Label(self.home, text="Departments", font=('Clarendon BT', 40),
                          background='#E9C5FF', foreground='#550685', relief='groove', borderwidth=5)
        self.l1 = Label(self.home, text="Department_name")
        self.l2 = Label(self.home, text="head_of_department")
        self.t1 = Entry(self.home)
        self.t2 = Entry(self.home)

        self.tablearea = Frame(self.home)
        self.table1 = Treeview(self.tablearea, columns=['c1', 'c2'],
                               height=25)
        self.table1.heading("c1", text="Department_name")
        self.table1.heading("c2", text="head_of_department")
        self.table1['show'] = 'headings'

        self.table1.column("#1", width=200, anchor='center')
        self.table1.column("#2", width=200, anchor='center')

        self.table1.bind("<ButtonRelease-1>", lambda e: self.getpk())
        self.table1.pack()

        self.b1 = Button(self.home, text="Save", foreground='white', background='#550685', command=self.savedata)
        self.b2 = Button(self.home, text="Fetch", foreground='white', background='#550685', command=self.fetchdata)
        self.b3 = Button(self.home, text="Update", foreground='white', background='#550685', command=self.Updatedata)
        self.b4 = Button(self.home, text="Delete", foreground='white', background='#550685', command=self.Deletedata)
        self.b5 = Button(self.home, text="Search", foreground='white', background='#550685', command=self.fetchalldata)

        self.back.place(x=0, y=0, width=w - 100, height=70)
        x1 = 50
        y1 = 100
        x_diff = 130
        y_diff = 50

        self.l1.place(x=x1, y=y1)
        self.t1.place(x=x1 + x_diff, y=y1)
        self.b2.place(x=x1 + x_diff + x_diff + 50, y=y1)
        self.tablearea.place(x=x1 + x_diff + x_diff + x_diff + 50, y=y1)

        y1 += y_diff
        self.l2.place(x=x1, y=y1)
        self.t2.place(x=x1 + x_diff, y=y1)
        self.b5.place(x=x1 + x_diff + x_diff + 50, y=y1)

        self.b1.place(x=x1, y=y1+50, width=100)
        self.b3.place(x=x1 + x_diff, y=y1+50, width=100)
        self.b4.place(x=x1 + x_diff + x_diff, y=y1+50, width=100)
        self.clearPage()
        self.home.mainloop()

    def dataconnection(self):
            try:
                self.conn = pymysql.connect(host="localhost", db="manage_data", user="root", password="")
                self.curr = self.conn.cursor()
            except Exception as e:
                messagebox.showerror("Data base Error" + str(e), parent=self.home)

    def savedata(self):
            self.dataconnection()
            try:
                qry = "insert into department_data value(%s,%s)"
                rowcount = self.curr.execute(qry, (self.t1.get(), self.t2.get()))
                self.conn.commit()
                if (rowcount == 1):
                    messagebox.showinfo("Success", "Department Saved successfully", parent=self.home)
                    self.clearPage()
            except Exception as e:
                messagebox.showerror("Query Error", "Error while insertion  : " + str(e), parent=self.home)

    def Updatedata(self):
            self.dataconnection()
            try:
                qry = " update department_data set head_of_department =%s  where Department_name=%s"
                rowcount = self.curr.execute(qry, (self.t2.get(),self.t1.get()))
                self.conn.commit()
                if (rowcount == 1):
                    messagebox.showinfo("Success", "Head of department Updated successfully", parent=self.home)
                self.clearPage()
            except Exception as e:
                messagebox.showerror("Query Error", "Error while updating : " + str(e), parent=self.home)

    def Deletedata(self):

            ans = messagebox.askquestion("Confirmation", "Are you sure to delete ??", parent=self.home)
            if ans == "yes":
                self.dataconnection()
                try:
                    qry = " delete from department_data where Department_name=%s"
                    rowcount = self.curr.execute(qry, (self.t1.get()))
                    self.conn.commit()
                    if (rowcount == 1):
                        messagebox.showinfo("Success", "Department Record Deleted Successfully", parent=self.home)
                        self.clearPage()
                except Exception as e:
                    messagebox.showerror("Query Error", "Error while deletion  : " + str(e), parent=self.home)

    def getpk(self):
            rowid = self.table1.focus()
            content = self.table1.item(rowid)
            values = content['values']
            pk = values[0]
            self.fetchdata(pk)

    def fetchdata(self, pk=None):
            if pk == None:
                Department_name = self.t1.get()
            else:
                Department_name = pk
            self.dataconnection()
            try:
                qry = "select * from department_data where Department_name = %s"
                rowcount = self.curr.execute(qry, (Department_name))
                data = self.curr.fetchone()
                self.clearPage()
                if data:

                    self.t1.insert(0, data[0])
                    self.t2.insert(0, data[1])

                    self.b3['state'] = 'normal'
                    self.b4['state'] = 'normal'
                else:
                    messagebox.showwarning("No Record", "Department Record Not Found", parent=self.home)
            except Exception as e:
                messagebox.showerror("Query Error", "Error while insertion connection : " + str(e), parent=self.home)

    def fetchalldata(self):
            self.dataconnection()
            self.table1.delete(*self.table1.get_children())
            try:
                qry = 'select * from department_data where head_of_department like %s '
                rowcount = self.curr.execute(qry, (self.t2.get() + "%"))

                data = self.curr.fetchall()
                if data:
                    for row in data:
                        self.table1.insert("", END, values=row)
                else:
                    messagebox.showwarning("No Department data found ", parent=self.home)
            except Exception as e:
                messagebox.showerror("Query Error " + str(e), parent=self.home)

    def clearPage(self):
            self.t1.delete(0, END)
            self.t2.delete(0, END)

            self.b3['state'] = 'disabled'
            self.b4['state'] = 'disabled'

if __name__ == '__main__':
    dummyHomepage=Tk()
    DepartmentClass(dummyHomepage)
    dummyHomepage.mainloop()
