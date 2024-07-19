from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import customtkinter as ctk 
import tkinter.messagebox as tkmb
from PIL import Image, ImageTk
import pandas as pd #
import webbrowser#
import matplotlib.pyplot as plt #
import tkinter as tk #
from tkinter import ttk #
from math import factorial
from tkinter import * # 
import sqlite3
import tkinter.messagebox as tkmsgbox #
import pymysql #
import mysql.connector #
from PIL import Image, ImageTk
import os
import numpy as np
import mysql.connector
from tkinter import Tk, Frame
import mysql.connector
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from course import CourseClass
from resultt import resultClass
from analysis import Analysis
from about import About
from studentdata import studentClass
i=0


class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Performance Analysis")
        self.root.geometry("1525x783+0+0")

        title=Label(self.root,text="Student Performance Analysis",font=("Impact",25),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #menu
        m_Frame=LabelFrame(self.root,bg="white",highlightbackground="#033054", highlightthickness=2)
        m_Frame.place(x=10,y=70,width=1505,height=80)

        frame=Frame(root,bg="#083B64")
        frame.place(x=10,y=160,width=1505,height=610)
#-------------calculator
        framec=Frame(frame,bg="#122330",highlightbackground="black", highlightthickness=2)
        framec.place(x=980,y=20,width=450,height=380)

        def get_variables(num):
            global i
            display.insert(i,num)
            i+=1
         
        def calculate():
            entire_string = display.get()
            try:
                result = eval(entire_string)
                clear_all()
                display.insert(0,result)
            except Exception:
                clear_all()
                display.insert(0,"Error")
         
        def get_operation(operator):
            global i
            length = len(operator)
            display.insert(i,operator)
            i+=length
         
        def clear_all():
            display.delete(0,END)
         
        def undo():
            entire_string = display.get()
            if len(entire_string):
                new_string = entire_string[:-1]
                clear_all()
                display.insert(0,new_string)
            else:
                clear_all()
                display.insert(0,"Error")

        def fact():
            entire_string = display.get()
            try:
                result = factorial(int(entire_string))
                clear_all()
                display.insert(0,result)
            except Exception:
                clear_all()
                display.insert(0,"Error")


        display = Entry(framec,font=("Agency FB", 15, "bold"))
        display.place(x=78,y=20,width=295,height=40)

        Button(framec,text="1",width=6,height=3,font=("Agency FB", 12, "bold"),bg='black',fg='white',command = lambda :get_variables(1)).place(x=78,y=70)
        Button(framec,text=" 2",width=6,height=3,font=("Agency FB", 12, "bold"),bg='black',fg='white',command = lambda :get_variables(2)).place(x=128,y=70)
        Button(framec,text=" 3",width=6,height=3,font=("Agency FB", 12, "bold"),bg='black',fg='white',command = lambda :get_variables(3)).place(x=178,y=70)
         
        Button(framec,text="4",width=6,height=3,font=("Agency FB", 12, "bold"),bg='black',fg='white',command = lambda :get_variables(4)).place(x=78,y=150)
        Button(framec,text=" 5",width=6,height=3,font=("Agency FB", 12, "bold"),bg='black',fg='white',command = lambda :get_variables(5)).place(x=128,y=150)
        Button(framec,text=" 6",width=6,height=3,font=("Agency FB", 12, "bold"),bg='black',fg='white',command = lambda :get_variables(6)).place(x=178,y=150)
         
        Button(framec,text="7",width=6,height=3,font=("Agency FB", 12, "bold"),bg='black',fg='white',command = lambda :get_variables(7)).place(x=78,y=230)
        Button(framec,text=" 8",width=6,height=3,font=("Agency FB", 12, "bold"),bg='black',fg='white',command = lambda :get_variables(8)).place(x=128,y=230)
        Button(framec,text=" 9",width=6,height=3,font=("Agency FB", 12, "bold"),bg='black',fg='white',command = lambda :get_variables(9)).place(x=178,y=230)
         
        #adding other buttons to the calculator
        Button(framec,text="AC",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command=lambda :clear_all()).place(x=78,y=310)
        Button(framec,text=" 0",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command = lambda :get_variables(0)).place(x=128,y=310)
        Button(framec,text=" .",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command=lambda :get_variables(".")).place(x=178, y=310)
         
         
        Button(framec,text="+",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command= lambda :get_operation("+")).place(x=228,y=70)
        Button(framec,text="-",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command= lambda :get_operation("-")).place(x=228,y=130)
        Button(framec,text="",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command= lambda :get_operation("")).place(x=228,y=190)
        Button(framec,text="/",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command= lambda :get_operation("/")).place(x=228,y=250)
         
        # adding new operations
        Button(framec,text="pi",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command= lambda :get_operation("*3.14")).place(x=278,y=70)
        Button(framec,text="%",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command= lambda :get_operation("%")).place(x=278,y=130)
        Button(framec,text="(",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command= lambda :get_operation("(")).place(x=278,y=190)
        Button(framec,text="exp",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command= lambda :get_operation("")).place(x=278,y=250)
         
        Button(framec,text="<-",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command= lambda :undo()).place(x=328,y=70)
        Button(framec,text="x!",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white', command= lambda: fact()).place(x=328,y=130)
        Button(framec,text=")",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command= lambda :get_operation(")")).place(x=328,y=190)
        Button(framec,text="^2",width=6,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command= lambda :get_operation("**2")).place(x=328,y=250)
        Button(framec,text="=",width=23,height=2,font=("Agency FB", 12, "bold"),bg='black',fg='white',command= lambda :calculate()).place(x=228,y=310)



#---------------------------------------------------------
        
        btn_course = ctk.CTkButton(master=m_Frame,hover_color="#086CBD",text='    Courses    ',command=self.add_course,fg_color=("white"),text_color="black",border_width=5,border_color="black",corner_radius=25,font=("Impact",30)) 
        btn_course.place(x=10,y=12)
        
        btn_student = ctk.CTkButton(master=m_Frame,hover_color="#086CBD",text=' New Record ',command=self.add_student,fg_color=("white"),text_color="black",border_width=5,border_color="black",corner_radius=25,font=("Impact",30)) 
        btn_student.place(x=210,y=12)

#btn_student=Button(m_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_student).place(x=260,y=5,width=220,height=40)

        btn_performance = ctk.CTkButton(master=m_Frame,hover_color="#086CBD",text=' Performance Analysis ',command=self.add_result,fg_color=("white"),text_color="black",border_width=5,border_color="black",corner_radius=25,font=("Impact",30)) 
        btn_performance.place(x=420,y=12)

#        btn_result=Button(m_Frame,text="Performance Analysis",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_result).place(x=500,y=5,width=220,height=40)

        btn_view = ctk.CTkButton(master=m_Frame,hover_color="#086CBD",text=' Data Analysis ',command=self.analysis,fg_color=("white"),text_color="black",border_width=5,border_color="black",corner_radius=25,font=("Impact",30)) 
        btn_view.place(x=750,y=12)

#        btn_view=Button(m_Frame,text="Data Analysis",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.analysis).place(x=740,y=5,width=220,height=40)
        
        btn_rep = ctk.CTkButton(master=m_Frame,hover_color="#086CBD",text=' Report ',command=self.rep,fg_color=("white"),text_color="black",border_width=5,border_color="black",corner_radius=25,font=("Impact",30)) 
        btn_rep.place(x=980,y=12)

        btn_abt = ctk.CTkButton(master=m_Frame,hover_color="#086CBD",text=' About ',command=self.about,fg_color=("white"),text_color="black",border_width=5,border_color="black",corner_radius=25,font=("Impact",30)) 
        btn_abt.place(x=1150,y=12)

#        btn_logout=Button(m_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.logout).place(x=980,y=5,width=220,height=40)

        btn_exit = ctk.CTkButton(master=m_Frame,hover_color="#086CBD",text=' Exit ',command=self.exit,fg_color=("white"),text_color="black",border_width=5,border_color="black",corner_radius=25,font=("Impact",30)) 
        btn_exit.place(x=1320,y=12)


#        btn_exit=Button(m_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.exit).place(x=1220,y=5,width=220,height=40)

        #content
         
#        btn_about=Button(self.root,text="About",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.about).place(x=1300,y=670,width=220,height=40)
        
        
#-----graph-------------
         
        def plot_3d_stem_canvas(frame):
            db_connection = sqlite3.connect('rms.db')

            query = """
            SELECT Course, Sem, (Sub1 + Sub2 + Sub3) / 3 AS AverageMarks
            FROM student
            """
            cursor = db_connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()

            courses = list(set(row[0] for row in results))
            semesters = list(set(row[1] for row in results))
            courses.sort()
            semesters.sort()

            X, Y, Z = [], [], []
            colors = []
            for course in courses:
                for sem in semesters:
                    avg_marks = [float(row[2]) for row in results if row[0] == course and row[1] == sem]
                    if avg_marks:
                        X.append(courses.index(course))
                        Y.append(sem)
                        Z.append(np.mean(avg_marks))
                        colors.append(courses.index(course))  

            fig = Figure(figsize=(8, 6))
            ax = fig.add_subplot(111, projection='3d')

            norm = Normalize(vmin=min(colors), vmax=max(colors))
            cmap = plt.get_cmap('tab10')

            for x, y, z, color_idx in zip(X, Y, Z, colors):
                ax.plot([x, x], [y, y], [0, z], color='black', marker='o', markersize=5, alpha=0.6)

            sc = ax.scatter(X, Y, Z, c=colors, cmap=cmap, s=50, depthshade=True)

            ax.set_xticks(range(len(courses)))
            ax.set_xticklabels(courses, rotation=90)
            ax.set_xlabel('Course')
            ax.set_ylabel('Semester')
            ax.set_zlabel('Average Marks')
            ax.set_title('Average Marks of Each Semester for Each Course')
            ax.set_zlim(0, 80)  

            sm = ScalarMappable(cmap=cmap, norm=norm)
            sm.set_array([])
            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.draw()
            canvas.get_tk_widget().place(x=50, y=20, width=850, height=580)

        plot_3d_stem_canvas(frame)

#------------------
#==-------------------------update/del frame-----------------
        frameupd=Frame(root,bg="#131313")
        frameupd.place(x=940,y=565,width=545,height=200)
#------------------------update----------------------------
        var_name1=StringVar()
        var_new=StringVar()

        frameupda=Frame(frameupd,bg="white")
        frameupda.place(x=5,y=5,width=535,height=190)


        lb2=ctk.CTkLabel(master=frameupda,text="Column to be updated :",font=("Impact",30,"underline"))
        lb2.place(x=15,y=5)

        cmbox=ctk.CTkComboBox(master=frameupda,width=200,font=('calibri',20),button_hover_color="#086CBD",values=['Name','Roll','Course','Sem','Gender','Sub1','Sub2','Sub3'],dropdown_hover_color="#086CBD")
        cmbox.place(x=320,y=8)

        label2 = ctk.CTkLabel(master=frameupda,text='Enter Roll: ',font=("Impact",30,"underline"))
        label2.place(x=15,y=45)
        namenty2= ctk.CTkEntry(master=frameupda,width=345,textvariable= var_name1,height=10,corner_radius=5,font=('Calibri',20))
        namenty2.place(x=175,y=47)

        label3 = ctk.CTkLabel(master=frameupda,text='Updated Value: ',font=("Impact",30,"underline"))
        label3.place(x=15,y=85)
        namenty3= ctk.CTkEntry(master=frameupda,width=300,textvariable= var_new,height=10,corner_radius=5,font=('Calibri',20))
        namenty3.place(x=220,y=87)        
       
            #------------------------------------------------------------
        def upd():
            roll_number = var_name1.get()
            new_value = var_new.get()
            column_to_update = cmbox.get()
            
            if roll_number == "" or new_value == "" or column_to_update == "":
                tkmsgbox.showerror("Error", "All fields are required")
                return
            
            try:
                connection = sqlite3.connect('rms.db')
                
                cursor = connection.cursor()
                query = f"UPDATE student SET {column_to_update} = ? WHERE Roll = ?"
                cursor.execute(query, (new_value, roll_number))
                
                connection.commit()
                
                if cursor.rowcount == 0:
                    tkmsgbox.showinfo("Info", "No record found with the provided Roll number")
                else:
                    tkmsgbox.showinfo("Info", "Record updated successfully")
                
                connection.close()
                
            except sqlite3.Error as err:
                tkmsgbox.showerror("Error", f"Something went wrong: {err}")
#-------------------------upd button-----------------------------------
        butup = ctk.CTkButton(master=frameupd,hover_color="#086CBD",text='  Update  ',command=upd,fg_color=("white"),text_color="black",border_width=4,border_color="black",corner_radius=25,font=("Impact",30)) 
        butup.place(x=170,y=135)
#---------------

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
    def analysis(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Analysis(self.new_win)
    def exit(self):
        op=messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op==True:
            self.root.destroy()       
    def rep(self):
        os.system("mini_project_report[1].docx")
    def about(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=About(self.new_win)
if __name__=="__main__":
    root=Tk()
    object=RMS(root)
    root.mainloop()
        