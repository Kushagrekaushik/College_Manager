from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from print import my_cust_PDF
import pymysql
class report_teacher:
    def __init__(self,teacher_report_window):
        self.home=Toplevel(teacher_report_window)
        w=self.home.winfo_screenheight()
        h=self.home.winfo_screenheight()
        self.home.minsize(w - 100, h - 180)
        self.home.state('zoomed')
        self.home.geometry("%dx%d+%d+%d" % (w - 100, h - 180, 50,70))
        self.hlbl = Label(self.home, text="Teacher Details", font=('Clarendon BT', 40), background='#E9C5FF',
                          foreground='#550685', relief='groove', borderwidth=5)
        self.tablearea=Frame(self.home)
        self.table1=Treeview(self.tablearea,columns=['c1','c2','c3','c4','c5','c6','c7','c8'],height=25)
        self.table1.heading("c1",text="Teacher_Unique_ID ")
        self.table1.heading("c2",text="Name")
        self.table1.heading("c3",text="Phone")
        self.table1.heading("c4",text="Gender")
        self.table1.heading("c5",text="DOB")
        self.table1.heading("c6",text="Address")
        self.table1.heading("c7",text="Department")
        self.table1.heading("c8",text="Course_Taught")

        self.table1['show'] = 'headings'

        self.table1.column("#1",width=150,anchor='center')
        self.table1.column("#2",width=150,anchor='center')
        self.table1.column("#3",width=150,anchor='center')
        self.table1.column("#4",width=150,anchor='center')
        self.table1.column("#5",width=150,anchor='center')
        self.table1.column("#6",width=300,anchor='center')
        self.table1.column("#7",width=150,anchor='center')
        self.table1.column("#8",width=150,anchor='center')

        self.table1.pack()
        self.b1 = Button(self.home, text="print", foreground='white', background='#550685', command=self.print)
        self.b1.place(x=300, y=650, width=100, height=50)

        self.hlbl.place(x=0, y=0, width=w - 100, height=70)
        self.tablearea.place(x=40, y=100)
        self.fetchalldata()
        self.home.mainloop()

    def dataconnection(self):
        try:
            self.conn=pymysql.connect(host="localhost",db="manage_data",user="root",password="")
            self.curr=self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Data base Error"+str(e),parent=self.home)

    def fetchalldata(self):
        self.dataconnection()
        try:
            qry='select * from teacher_data'
            rowcount=self.curr.execute(qry)
            data=self.curr.fetchall()
            self.pdata = []
            if data:
                for row in data:
                    self.pdata.append(row[:8])
                    self.table1.insert("",END,values=row)
            else:
                messagebox.showwarning("No teacher data found ",parent=self.home)
        except Exception as e:
            messagebox.showerror("Query Error "+str(e),parent=self.home)

    def print(self):
        pdf = my_cust_PDF()
        headings = ['Id', 'Name','Phone No' ,'Gender', 'DOB', 'Address', 'Department', 'Course']
        pdf.print_chapter(self.pdata, headings,8)

        pdf.output('pdf_file1.pdf')
        import os
        os.system('explorer.exe "pdf_file1.pdf"')

if __name__ == '__main__':
    dummyHomepage=Tk()
    report_teacher(dummyHomepage)
    dummyHomepage.mainloop()