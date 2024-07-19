import sqlite3
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

class Analysis:
    def __init__(self, root): # default constructor and root is a tkinter class object
        self.root = root
        self.root.title("Student Performance Analysis")
        self.root.geometry("1525x783+0+0") # Setting width
        self.root.config(bg="black")
        self.root.focus_force()

        title = Label(self.root, text="Student Performance Analysis", font=("goudy old style", 20, "bold"), bg="orange", fg="#262626").place(x=10, y=10, width=1505, height=50)
        
        frameb = Frame(self.root, bg="white")
        frameb.place(x=10, y=70, width=1000, height=710)
        
        fig = self.plot_3d_scatter()
        fig.subplots_adjust(left=0.15,right=0.85,top=0.85,bottom=0.15)
        canvas = FigureCanvasTkAgg(fig, master=frameb)
        canvas.draw()
        canvas.get_tk_widget().place(x=20, y=20, width=960, height=650)
        
        framec = Frame(self.root, bg="white")
        framec.place(x=1020, y=70, width=500, height=385)
        
        self.plot_donut_chart(framec)

        framed = Frame(self.root, bg="white")
        framed.place(x=1020, y=462, width=500, height=320)
        
        self.plot_stack_plot(framed)

    def plot_3d_scatter(self):
        connection = sqlite3.connect('rms.db')

        plt.style.use('_mpl-gallery')

        cursor = connection.cursor()

        query = "SELECT Sub1, Sub2, Sub3 FROM student"
        cursor.execute(query)
        rows = cursor.fetchall()

        x = np.array([row[0] for row in rows])
        y = np.array([row[1] for row in rows])
        z = np.array([row[2] for row in rows])
        colors = np.random.randint(500, size=len(rows))  

        fig = plt.figure(figsize=(14, 10))
        ax = fig.add_subplot(111, projection='3d')

        sc = ax.scatter(x, y, z, c=colors, cmap='gist_heat')
        font_label = {'family': 'Impact', 'size': 12, 'weight': 'bold'}

        ax.set_xlabel('Subject 1', fontdict=font_label)
        ax.set_ylabel('Subject 2', fontdict=font_label)
        ax.set_zlabel('Subject 3', fontdict=font_label)

        ax.set_title('Scatter Plot of Student Marks')

        ax.set_xticks(np.arange(30, max(x)+1, 10))
        ax.set_yticks(np.arange(30, max(y)+1, 10))
        ax.set_zticks(np.arange(30, max(z)+1, 10))

        return fig

    def plot_donut_chart(self, frame):
        connection = sqlite3.connect('rms.db')
        cursor = connection.cursor()
        cursor.execute("SELECT Course, COUNT(*) AS Count FROM student GROUP BY Course")
        results = cursor.fetchall()
        courses = []
        counts = []
        for row in results:
            courses.append(row[0])
            counts.append(row[1])

        norm_counts = [float(count) / sum(counts) for count in counts]
        colors = ['#6e4f38', '#9c755f', '#d1a17a', '#f6e1cf']
        fig, ax = plt.subplots(figsize=(8, 8))

        wedges, texts, autotexts = ax.pie(norm_counts, labels=courses, autopct='%1.1f%%',
                                        colors=colors, startangle=140, wedgeprops={'width': 0.4, 'edgecolor': 'w', 'linewidth': 1.5})
        centre_circle = plt.Circle((0, 0), 0.3, color='white', fc='white', linewidth=1.25)
        ax.add_artist(centre_circle)
        ax.axis('equal')
        plt.setp(autotexts, fontname='Impact', fontsize=14)
        ax.set_title('Distribution of Courses', fontsize=14)
        
        fig.subplots_adjust(left=0.15,right=0.85,top=0.85,bottom=0.15)
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=0, y=0, width=440, height=430)

    def plot_stack_plot(self, frame):
        connection = sqlite3.connect('rms.db')
        cursor = connection.cursor()
        query = """
        SELECT Gender, (Sub1 + Sub2 + Sub3) / 3 AS AverageMarks
        FROM student
        """
        cursor.execute(query)
        results = cursor.fetchall()
        
        male_marks = [row[1] for row in results if row[0] == 'M']
        female_marks = [row[1] for row in results if row[0] == 'F']
        unique_marks = sorted(set(male_marks + female_marks))
        male_distribution = [male_marks.count(mark) for mark in unique_marks]
        female_distribution = [female_marks.count(mark) for mark in unique_marks]
        
        x = np.array(unique_marks)
        male_distribution = np.array(male_distribution)
        female_distribution = np.array(female_distribution)
        
        fig = plt.figure(figsize=(10, 6))
        plt.stackplot(x, male_distribution, female_distribution, labels=['Male', 'Female'], colors=['#E7E7E7', '#626567'])
        plt.xlabel('Average Marks')
        plt.ylabel('Number of Students')
        plt.title('Distribution of Students by Average Marks and Gender')
        plt.legend(loc='upper left')
        
        fig.subplots_adjust(left=0.15,right=0.85,top=0.85,bottom=0.15)
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=10, y=0, width=470, height=320)

if __name__ == "__main__":
    root = Tk()
    obj = Analysis(root)
    root.mainloop()

