from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox, Treeview

from PIL import ImageTk,Image
from tkcalendar import DateEntry

import pymysql


class TeacherClass:
    default_image = "default_image.jpg"
    def __init__(self,Teacherwindow):
        self.home=Teacherwindow
        self.home=Toplevel(Teacherwindow)
        self.home.state("zoomed")
        w = self.home.winfo_screenwidth()
        h = self.home.winfo_screenheight()
        self.home.minsize(w - 100, h - 180)
        self.home.geometry("%dx%d+%d+%d" % (w - 100, h - 180, 50, 70))

#         Widgets
        self.back = Label(self.home, text="Staff", font=('Clarendon BT', 40),
                          background='#E9C5FF', foreground='#550685', relief='groove', borderwidth=5)
        self.l1=Label(self.home,text="Teacher_Unique_ID")
        self.l2=Label(self.home,text="Name")
        self.l3=Label(self.home,text="Phone")
        self.l4=Label(self.home,text="Gender")
        self.l5=Label(self.home,text="DOB")
        self.l6=Label(self.home,text="Address")
        self.l7=Label(self.home,text="Department")
        self.l8=Label(self.home,text="Course_Taught")



        self.t1=Entry(self.home)
        self.t2=Entry(self.home)
        self.t3=Entry(self.home)
        self.v1=StringVar()
        self.r1=Radiobutton(self.home,text="Male",value="Male",variable=self.v1)
        self.r2=Radiobutton(self.home, text="Female", value="Female", variable=self.v1)
        self.t5=DateEntry(self.home, width=12, background='darkblue', foreground='white', borderwidth=2,
                  year=2010, date_pattern='y-mm-dd')
        self.t6=Text(self.home,height=3,width=15)
        self.v2=StringVar()
        self.c1 = Combobox(self.home, textvariable=self.v2)
        self.c1.bind("<<ComboboxSelected>>", lambda e: self.fetchAllCourse())
        self.v3 = StringVar()
        self.c2 = Combobox(self.home,textvariable=self.v3)

        self.v1.set(None)
        self.c1.set("choose department")
        self.c2.set("choose Course")


        self.tablearea = Frame(self.home)
        self.table1 = Treeview(self.tablearea, columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'], height=20)
        self.table1.heading("c1", text="Teacher_Unique_ID ")
        self.table1.heading("c2", text="Name")
        self.table1.heading("c3", text="Phone")
        self.table1.heading("c4", text="Gender")
        self.table1.heading("c5", text="DOB")
        self.table1.heading("c6", text="Address")
        self.table1.heading("c7", text="Department")
        self.table1.heading("c8", text="Course_Taught")

        self.table1['show'] = 'headings'

        self.table1.column("#1", width=120, anchor='center')
        self.table1.column("#2", width=100, anchor='center')
        self.table1.column("#3", width=100, anchor='center')
        self.table1.column("#4", width=70, anchor='center')
        self.table1.column("#5", width=70, anchor='center')
        self.table1.column("#6", width=200, anchor='center')
        self.table1.column("#7", width=150, anchor='center')
        self.table1.column("#8", width=150, anchor='center')
        self.table1.bind("<ButtonRelease-1>", lambda e: self.getpk())
        self.table1.pack()


#         Buttons
        self.b1 = Button(self.home, text="Save", foreground='white', background='#550685', command=self.savedata)
        self.b2 = Button(self.home, text="Fetch", foreground='white', background='#550685', command=self.fetchdata)
        self.b3=Button(self.home,text="Update",foreground='white',background='#550685',command=self.Updatedata)
        self.b4=Button(self.home,text="Delete",foreground='white',background='#550685',command=self.Deletedata)
        self.b5 = Button(self.home, text="Search", foreground='white', background='#550685', command=self.fetchalldata)
        self.b6 = Button(self.home, text='Upload', foreground='white', background='#550685', command=self.getImage)
        self.imglbl = Label(self.home, relief='groove', borderwidth=2)

        self.back.place(x=0, y=0, width=w - 100, height=70)
        x1 = 50
        y1 = 100
        x_diff = 130
        y_diff = 80

        self.l1.place(x=x1, y=y1)
        self.t1.place(x=x1 + x_diff, y=y1)
        self.b2.place(x=x1 + x_diff + x_diff + 50, y=y1)
        self.tablearea.place(x=x1 + x_diff + x_diff + x_diff + 50, y=y1)

        y1 += y_diff
        self.l2.place(x=x1, y=y1)
        self.t2.place(x=x1 + x_diff, y=y1)
        self.b5.place(x=x1 + x_diff + x_diff + 50, y=y1)
        y1 += y_diff
        self.l3.place(x=x1, y=y1)
        self.t3.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.l4.place(x=x1, y=y1)
        self.r1.place(x=x1 + x_diff, y=y1)
        self.r2.place(x=x1 + x_diff + x_diff, y=y1)
        y1 += y_diff
        self.l5.place(x=x1, y=y1)
        self.t5.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.l6.place(x=x1, y=y1)
        self.t6.place(x=x1 + x_diff, y=y1)

        y1 += y_diff
        self.l7.place(x=x1, y=y1)
        self.c1.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.l8.place(x=x1, y=y1)
        self.c2.place(x=x1 + x_diff, y=y1)

        y1 += y_diff
        self.b1.place(x=x1, y=y1, width=100)
        self.b3.place(x=x1 + x_diff, y=y1, width=100)
        self.b4.place(x=x1 + x_diff + x_diff, y=y1, width=100)
        self.imglbl.place(x=x1 + x_diff + x_diff + x_diff + x_diff, y=y1-150 , width=150, height=150)
        self.b6.place(x=x1 + x_diff + x_diff + x_diff + x_diff, y=y1 , width=150)
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
        if self.validate_check() == False:
            return
        if self.actualname == self.default_image:
            pass
        else:
            self.img1.save("teacher_images//" + self.actualname)
        self.dataconnection()
        try:
            qry="insert into teacher_data value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            rowcount=self.curr.execute(qry,(self.t1.get(),self.t2.get(),self.t3.get(),self.v1.get(),
                                            self.t5.get(),self.t6.get('1.0',END),self.v2.get(),self.v3.get(),self.actualname))
            self.conn.commit()
            if(rowcount==1):
                messagebox.showinfo("Success","Teacher record Saved successfully",parent=self.home)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion  : " + str(e), parent=self.home)

    def Updatedata(self):
        if self.validate_check() == False:
            return
        if self.actualname == self.oldname:
            pass
        else:
            self.img1.save("teacher_images//" + self.actualname)
            if self.oldname == self.default_image:
                pass
            else:
                import os
                os.remove("teacher_images//" + self.oldname)
        self.dataconnection()
        try:
            qry = " update teacher_data set Name =%s,Phone =%s, Gender=%s, DOB=%s, Address=%s," \
                          " Department=%s,Course_Taught =%s,pic=%s where Teacher_Unique_ID=%s"
            rowcount = self.curr.execute(qry, (self.t2.get(), self.t3.get(), self.v1.get(), self.t5.get(),
                                                       self.t6.get('1.0', END), self.v2.get(), self.v3.get(),
                                               self.actualname,self.t1.get()))
            self.conn.commit()
            if (rowcount == 1):
                messagebox.showinfo("Success"," Teacher record Updated successfully", parent=self.home)
                self.clearPage()
        except Exception as e:
                messagebox.showerror("Query Error","Error while updating : " + str(e), parent=self.home)

    def Deletedata(self):

        ans = messagebox.askquestion("Confirmation", "Are you sure to delete ??", parent=self.home)
        if ans == "yes":
            if self.oldname == self.default_image:  # no image was given in past

                pass
            else:
                import os
                os.remove("teacher_images//" + self.oldname)
            self.dataconnection()
            try:
                qry = " delete from teacher_data where Teacher_Unique_ID=%s"
                rowcount = self.curr.execute(qry, (self.t1.get()))
                self.conn.commit()
                if (rowcount == 1):
                    messagebox.showinfo("Success", "Teacher Record Deleted Successfully", parent=self.home)
                    self.clearPage()
            except Exception as e:
                    messagebox.showerror("Query Error", "Error while deletion  : " + str(e), parent=self.home)

    def getpk(self):
                rowid = self.table1.focus()
                content = self.table1.item(rowid)
                values = content['values']
                pk = values[0]
                self.fetchdata(pk)
    def fetchdata(self,pk=None):
        if pk == None:
            Teacher_Unique_ID = self.t1.get()
        else:
            Teacher_Unique_ID = pk
        self.dataconnection()
        try:
            qry="select * from teacher_data where Teacher_Unique_ID = %s"
            rowcount=self.curr.execute(qry,(Teacher_Unique_ID))
            data=self.curr.fetchone()
            self.clearPage()
            if data:

                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])
                self.t3.insert(0,data[2])
                self.v1.set(data[3])
                self.t5.insert(0,data[4])
                self.t6.insert('1.0',data[5])
                self.v2.set(data[6])
                self.v3.set(data[7])
                self.actualname = data[8]
                self.oldname = data[8]
                self.img1 = Image.open("teacher_images//" + self.actualname)
                self.img1 = self.img1.resize((150, 150))
                self.img2 = ImageTk.PhotoImage(self.img1)
                self.imglbl.config(image=self.img2)

            else:
                messagebox.showwarning("No Record","Teacher Record Not Found",parent=self.home)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion connection : "+str(e),parent=self.home)
    def fetchalldata(self):
        self.dataconnection()
        self.table1.delete(*self.table1.get_children())
        try:
            qry='select * from teacher_data where Name like %s '
            rowcount=self.curr.execute(qry,(self.t2.get()+"%"))

            data=self.curr.fetchall()
            if data:
                for row in data:
                    self.table1.insert("",END,values=row)
            else:
                messagebox.showwarning("No teacher data found ",parent=self.home)
        except Exception as e:
            messagebox.showerror("Query Error "+str(e),parent=self.home)
    def fetchAlldept(self):
        self.dataconnection()
        try:
            qry = "select * from department_data"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchall()
            self.department_list = []
            if data:
                self.c1.set("Choose Department")
                for row in data:
                    self.department_list.append(row[0])
            else:
                self.c1.set("No Department")
            self.c1.config(values=self.department_list)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while fetching : " + str(e), parent=self.home)
    def fetchAllCourse(self):
        self.dataconnection()
        try:
            qry = "select * from course_data where Departments=%s"
            rowcount = self.curr.execute(qry, (self.v2.get()))
            data = self.curr.fetchall()
            self.courseList = []
            if data:
                self.c2.set("Choose Course")
                for row in data:
                    self.courseList.append(row[1])
            else:
                self.c2.set("No Course")
            self.c2.config(values=self.courseList)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while fetching : " + str(e), parent=self.home)
    def getImage(self):
        self.filename = askopenfilename(file=[("ALL", "*.jpg;*.png;*.jpeg"), ("PNG student_images", "*.png"), ("JPG", "*.jpg")])

        if self.filename != "":

            self.img1 = Image.open(self.filename)
            self.img1 = self.img1.resize((150, 150))
            self.img2 = ImageTk.PhotoImage(self.img1)
            self.imglbl.config(image=self.img2)

            import time
            uniqueness = str(int(time.time()))
            path = self.filename.split("/")

            name = path[-1]

            self.actualname = uniqueness + name

    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.t3.delete(0, END)
        self.v1.set(None)
        self.t5.delete(0, END)
        self.t6.delete('1.0', END)
        self.c1.set("Department")
        self.c2.set("Course_Taught")
        self.b3['state'] = 'disabled'
        self.b4['state'] = 'disabled'
        self.actualname = self.default_image
        self.img1 = Image.open("teacher_images//" + self.actualname)
        self.img1 = self.img1.resize((150, 150))
        self.img2 = ImageTk.PhotoImage(self.img1)
        self.imglbl.config(image=self.img2)

    def validate_check(self):
            if not (self.t1.get().isdigit()):
                messagebox.showwarning("Validation Check", "Invalid Teacher Id", parent=self.home)
                return False
            elif not (self.t2.get().isalpha()) or len(self.t2.get()) < 2:
                messagebox.showwarning("Validation Check", "Enter proper name ", parent=self.home)
                return False
            elif not (self.t3.get().isdigit()) or len(self.t3.get()) != 10:
                messagebox.showwarning("Validation Check", "Enter valid phone no \n10 digits only", parent=self.home)
                return False
            elif not (self.v1.get() == 'Male' or self.v1.get() == 'Female'):
                messagebox.showwarning("Input Error", "Please Select gender ", parent=self.home)
                return False
            elif (self.t5.get() == ""):
                messagebox.showwarning("Input Error", "Please Select DOB ", parent=self.home)
                return False
            elif len(self.t6.get('1.0', END)) < 3:
                messagebox.showwarning("Input Error", "Please Enter Address ", parent=self.home)
                return False
            elif (self.v2.get() == "Choose Department") or (self.v2.get() == "No Department"):
                messagebox.showwarning("Input Error", "Please Select Department ", parent=self.home)
                return False
            elif (self.v3.get() == "Choose Course") or (self.v3.get() == "No Course"):
                messagebox.showwarning("Input Error", "Please Select Course ", parent=self.home)
                return False

            return True


if __name__ == '__main__':
    dummyHomepage=Tk()
    TeacherClass(dummyHomepage)
    dummyHomepage.mainloop()