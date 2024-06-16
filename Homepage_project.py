from tkinter import *
from ManageStudents_project import StudentClass
from ManageTeacher_project import TeacherClass
from Manage_Clerks import ClerkClass
from ManageUser import  UserClass
from course import  course
from departments import  DepartmentClass

# from Project.ManageUser import UserClass
# from Project.course import course
# from Project.departments import DepartmentClass
from report_student import *
from report_clerk import *
from report_teacher import *

class homepage:
    def __init__(self, uname, utype):
        self.uname = uname
        self.utype = utype
        self.home=Tk()
        w = self.home.winfo_screenwidth()
        h = self.home.winfo_screenheight()
        self.home.minsize(700, 450)
        self.home.geometry("%dx%d+%d+%d" % (700, 450, 400,200))
        self.home.state("zoomed")
        self.home.option_add("*TearOff",False)
        self.menubar=Menu()
        self.home.config(menu=self.menubar)
        self.menu1=Menu()
        self.menu2=Menu()
        self.menu3=Menu()
        self.menu4=Menu()
        self.menubar.add_cascade(menu=self.menu1,label='User')
        self.menubar.add_cascade(menu=self.menu2,label='Department')
        self.menubar.add_cascade(menu=self.menu3,label='Reports')
        self.menubar.add_cascade(menu=self.menu4,label='Account')
        # from PIL import ImageTk,Image
        # self.iconimg1 = Image.open("App_images//Student.png")
        # self.iconimg1 = self.iconimg1.resize((20, 20))
        # self.iconimg2 = ImageTk.PhotoImage(self.iconimg1)
        # self.menu1.add_command(label='Student',image=self.iconimg2,compound=LEFT,command=lambda: StudentClass(self.home))

        self.menu1.add_command(label='Teacher',command=lambda: TeacherClass(self.home))
        self.menu1.add_command(label='clerk',command=lambda: ClerkClass(self.home))
        self.menu2.add_command(label="Department", command=lambda: DepartmentClass(self.home))
        self.menu2.add_command(label="Course", command=lambda: course(self.home))
        self.menu3.add_command(label='Student',command=lambda:report_student(self.home))
        self.menu3.add_command(label='teacher',command=lambda:report_teacher(self.home))
        self.menu3.add_command(label='clerk',command=lambda:report_clerk(self.home))
        self.menu4.add_command(label="Manage User",command=lambda: UserClass(self.home))

        # from PIL import ImageTk, Image
        # self.bkimg1 = Image.open("App_images//michael-marsh-U0dBV_QeiYk-unsplash.jpg")
        # self.bkimg1 = self.bkimg1.resize((w, h))
        # self.bkimg2 = ImageTk.PhotoImage(self.bkimg1)
        # self.bklbl = Label(self.home, image=self.bkimg2)
        # self.bklbl.place(x=0, y=0)

        self.home.mainloop()

if __name__=='__main__':
    homepage("dummy","Admin")