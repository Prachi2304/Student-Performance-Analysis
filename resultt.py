import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import Image, ImageTk
import pandas as pd
import webbrowser
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as tkmsgbox
import sqlite3
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
class resultClass:
    def __init__(self, root ): # default constructor and root is a tkinter class object
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1525x783+0+0") # Setting width
        self.root.config(bg="white")
        self.root.focus_force()

#--------------------------------------------
        framenew = Frame(root, highlightbackground="#DF8C61", highlightthickness=2, bg="#131313")
        framenew.place(x=10, y=10, width=1515, height=770)
        self.frame = Frame(root, bg="grey")
        self.frame.place(x=550, y=310, width=860, height=450)
#-----------------------------
        db_connection = sqlite3.connect("rms.db")
        cursor = db_connection.cursor()
#---------------------------------------
        detail_frame = Frame(framenew, bd=2, relief=RIDGE)
        detail_frame.place(x=500, y=35, width=900, height=250)
        scroll_x = ttk.Scrollbar(detail_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detail_frame, orient=VERTICAL)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 13))
        style.configure("mystyle.Treeview.Heading", font=("Impact", 16))

        self.student_table = ttk.Treeview(detail_frame, style="mystyle.Treeview", column=("Name", "Roll", "Course", "Gender", "Sem", "Sub1", "Sub2", "Sub3", "Avg"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Roll", text="Roll")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Sem", text="Sem")
        self.student_table.heading("Sub1", text="Sub1")        
        self.student_table.heading("Sub2", text="Sub2")
        self.student_table.heading("Sub3", text="Sub3")        
        self.student_table.heading("Avg", text="Avg")        

        self.student_table["show"] = "headings"

        self.student_table.column("Name", width=170, anchor=CENTER)
        self.student_table.column("Roll", width=70, anchor=CENTER)
        self.student_table.column("Course", width=50, anchor=CENTER)
        self.student_table.column("Gender", width=50, anchor=CENTER)
        self.student_table.column("Sem", width=40, anchor=CENTER)
        self.student_table.column("Sub1", width=40, anchor=CENTER)
        self.student_table.column("Sub2", width=40, anchor=CENTER)
        self.student_table.column("Sub3", width=40, anchor=CENTER)
        self.student_table.column("Avg", width=40, anchor=CENTER)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>")    

#--------------------        
        label1 = ctk.CTkLabel(master=framenew, text='Performance Predictor', font=("Copperplate Gothic Light", 30, "underline"), text_color="white")
        label1.place(x=25, y=35)

        var_name1 = StringVar()
        label2 = ctk.CTkLabel(master=framenew, text='Roll Number : ', font=("Impact", 30), text_color="white")
        label2.place(x=25, y=95)
        self.namenty2 = ctk.CTkEntry(master=framenew, width=170, textvariable=var_name1, height=10, corner_radius=5, font=('Calibri', 20))
        self.namenty2.place(x=205, y=97)

        var_name2 = StringVar()
        label3 = ctk.CTkLabel(master=framenew, text='Current Avg : ', font=("Impact", 30), text_color="white")
        label3.place(x=25, y=145)
        self.namenty3 = ctk.CTkEntry(master=framenew, width=170, textvariable=var_name2, height=10, corner_radius=5, font=('Calibri', 20))
        self.namenty3.place(x=205, y=147)

        butchk = ctk.CTkButton(master=framenew, hover_color="#E05F1C", text='    Predict    ', command=self.predict, fg_color=("#131313"), text_color="#D3D3D3", border_width=4, border_color="#D3D3D3", corner_radius=25, font=("Impact", 33)) 
        butchk.place(x=115, y=225)

        label11 = ctk.CTkLabel(master=framenew, text='Result Analysis', font=("Copperplate Gothic Light", 30, "underline"), text_color="white")
        label11.place(x=25, y=310)

        label22 = ctk.CTkLabel(master=framenew, text='Sort by : ', font=("Impact", 30), text_color="white")
        label22.place(x=25, y=370)

        self.cmbox = ctk.CTkComboBox(master=framenew, width=200, font=('calibri', 20), button_hover_color="#E05F1C", values=['Sub1', 'Sub2', 'Sub3', 'Avg'], dropdown_hover_color="#E05F1C")
        self.cmbox.place(x=185, y=375)

        var_name11 = StringVar()
        label3 = ctk.CTkLabel(master=framenew, text='No of Records : ', font=("Impact", 30), text_color="white")
        label3.place(x=25, y=430)
        self.namenty33 = ctk.CTkEntry(master=framenew, width=170, textvariable=var_name11, height=10, corner_radius=5, font=('Calibri', 20))
        self.namenty33.place(x=215, y=432)


        self.rad_var2 = StringVar()

        rdbt2 = ctk.CTkRadioButton(framenew, hover_color="#E05F1C", font=("Impact", 30), fg_color="white",text_color="white", text="Highest", variable=self.rad_var2, value="high")
        rdbt2.place(x=45, y=490)
        rdbt22 = ctk.CTkRadioButton(framenew, hover_color="#E05F1C", font=("Impact", 30), fg_color="white",text_color="white", text="Lowest", variable=self.rad_var2, value="low")
        rdbt22.place(x=260, y=490)

        butsrt = ctk.CTkButton(master=framenew, hover_color="#E05F1C", text='    Sort    ', command=self.srt, fg_color=("#131313"), text_color="#D3D3D3", border_width=4, border_color="#D3D3D3", corner_radius=25, font=("Impact", 33)) 
        butsrt.place(x=130, y=560)

#----------------
    def ser(self, x: str):
        if x == "":
            tkmsgbox.showerror("Error", "Roll number is required")
        else:
            try:
                con = sqlite3.connect("rms.db")
                my_cursor = con.cursor()
                my_cursor.execute('SELECT *, (Sub1 + Sub2 + Sub3) / 3 as Avg FROM student WHERE Roll = ?', (x,))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                    con.commit()
            except Exception as es:
                tkmsgbox.showwarning("Warning", f"Something went wrong: {str(es)}")
            con.close()

    def srt(self):
        try:
            con = sqlite3.connect("rms.db")
            my_cursor = con.cursor()
            sort_by = self.cmbox.get()
            num_records = self.namenty33.get()
            order = self.rad_var2.get()
            
            if num_records == "":
                num_records = "18446744073709551615"  
            
            query = f"SELECT *, (Sub1 + Sub2 + Sub3) / 3 as Avg FROM student ORDER BY {sort_by} {'DESC' if order == 'high' else 'ASC'} LIMIT {num_records}"
            my_cursor.execute(query)
            rows = my_cursor.fetchall()
            
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in rows:
                    self.student_table.insert("", END, values=i)
                con.commit()
                
                self.plot_graph(rows, sort_by)
                
            con.close()
            
        except Exception as es:
            tkmsgbox.showwarning("Warning", f"Something went wrong: {str(es)}")

    def plot_graph(self, rows, sort_by):
        try:
            fig = Figure(figsize=(8, 6), dpi=100)
            ax = fig.add_subplot(111)
            
            x_data = [row[0] for row in rows]
            y_data = [row[self.student_table["columns"].index(sort_by)] for row in rows] 
            
            ax.plot(x_data, y_data, marker='o', linestyle='-', color='b')
            ax.set_xlabel('Name')  
            ax.set_ylabel(sort_by)  
            ax.set_title(f'Sorted by {sort_by}')
            ax.grid(True)
            
            for tick in ax.get_xticklabels():
                tick.set_rotation(45)
            
            for widget in self.frame.winfo_children():
                widget.destroy()
                
            fig.subplots_adjust(left=0.15, right=0.85, top=0.85, bottom=0.30)

            canvas = FigureCanvasTkAgg(fig, master=self.frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=BOTH, expand=1)
            
        except Exception as e:
            tkmsgbox.showwarning("Warning", f"Failed to plot graph: {str(e)}")

    def predict(self):
        roll = self.namenty2.get()
        current_avg = self.namenty3.get()
        
        if roll == "" or current_avg == "":
            tkmsgbox.showerror("Error", "All fields required")
            return
        
        try:
            current_avg = float(current_avg)
        except ValueError:
            tkmsgbox.showerror("Error", "Current Avg must be a number")
            return
        
        try:
            con = sqlite3.connect("rms.db")
            my_cursor = con.cursor()
            my_cursor.execute('SELECT Sem, (Sub1 + Sub2 + Sub3) / 3 as Avg FROM student WHERE Roll = ? ORDER BY Sem DESC LIMIT 1', (roll,))
            row = my_cursor.fetchone()
            
            if row:
                prev_sem, prev_avg = row
                prev_avg = float(prev_avg)
                change_percentage = ((current_avg - prev_avg) / prev_avg) * 100
                predictive_avg = current_avg + (current_avg * change_percentage / 100)
                
                fig = Figure(figsize=(8, 6), dpi=100)
                ax = fig.add_subplot(111)
                semesters = ["Previous Semester", "Current Semester", "Next Semester"]
                averages = [prev_avg, current_avg, predictive_avg]
                ax.plot(semesters, averages, marker='o', linestyle='-', color='b')
                ax.set_xlabel('Semester')
                ax.set_ylabel('Average Marks')
                ax.set_title('Performance Prediction')
                ax.grid(True)
                
                for i, avg in enumerate(averages):
                    ax.annotate(f'{avg:.2f}', (semesters[i], averages[i]), textcoords="offset points", xytext=(0, 10), ha='center')
                
                for widget in self.frame.winfo_children():
                    widget.destroy()
                fig.subplots_adjust(left=0.15, right=0.85, top=0.85, bottom=0.15)

                canvas = FigureCanvasTkAgg(fig, master=self.frame)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=BOTH, expand=1)
                
                self.ser(roll) 
                
            else:
                tkmsgbox.showinfo("Info", "No previous semester data found for this roll number")
                
            con.close()
        
        except Exception as es:
            tkmsgbox.showwarning("Warning", f"Something went wrong: {str(es)}")
if __name__=="main":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()