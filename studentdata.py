from tkinter import*
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk, messagebox
import sqlite3

class studentClass:
    def __init__(self, root ): # default constructor and root is a tkinter class object
        self.root = root
        self.root.title("Student Performance Analysis")
        self.root.geometry("1190x490+170+170") # Setting width
        self.root.config(bg="white")
        self.root.focus_force()
        #sqlite3.Connection(SELECT * FROM COURSE)
         #***********title***********
        title = Label(self.root, text="Manage Student Details", font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=10, y=15, width=1140, height=35)

        #***********Variables***********
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_sem=StringVar()
        self.var_gender=StringVar()
        self.var_sub1=StringVar()
        self.var_sub2=StringVar()
        self.var_course=StringVar()
        self.var_sub3=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()

        # ***********Labelss***********
        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=60)
        lbl_name=Label(self.root,text="Name",font=("goudy old style", 15, "bold"),bg="white").place(x=360,y=60)
        lbl_course=Label(self.root,text="Course",font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=100)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style", 15, "bold"),bg="white").place(x=360,y=100)
        lbl_Sem=Label(self.root,text="Sem",font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=140)
        lbl_sub1=Label(self.root,text="Sub 1",font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=180)
        lbl_sub2=Label(self.root,text="Sub 2",font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=220)
        lbl_sub3=Label(self.root,text="Sub 3",font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=260)
        #***********Entry Fields***********
        self.course_list=[]
        #***********function_call to update the list***********
        self.fetch_course()

        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style", 15, "bold"),bg="lightyellow")
        self.txt_roll.place(x=150,y=60,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=480,y=60,width=200)
        txt_Sem=Entry(self.root,textvariable=self.var_sem,font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=150,y=140,width=200)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("goudy old style", 15, "bold"),state="readonly",justify=CENTER)
        self.txt_gender.place(x=480,y=100,width=200)
        self.txt_gender.current(0)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style", 15, "bold"),state="readonly",justify=CENTER)
        self.txt_course.place(x=150,y=100,width=200)
        self.txt_course.set("Select")

        
        #***********function_call to update the list****

        txt_sub1=Entry(self.root,textvariable=self.var_sub1,font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=150,y=180,width=200)
        txt_sub2=Entry(self.root,textvariable=self.var_sub2,font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=150,y=220,width=200)
        txt_sub3=Entry(self.root,textvariable=self.var_sub3,font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=150,y=260,width=200)
        


        #***********Buttons***********
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2", command=self.add)
        self.btn_add.place(x=150,y=350,width=110,height=60)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2", command=self.update)
        self.btn_update.place(x=270,y=350,width=110,height=60)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2", command=self.delete)
        self.btn_delete.place(x=390,y=350,width=110,height=60)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2", command=self.clear)
        self.btn_clear.place(x=510,y=350,width=110,height=60)

        #***********Search Panel***********
        self.var_search=StringVar()

        lbl_search_roll=Label(self.root,text="Roll No.",font=("goudy old style", 15, "bold"),bg="white").place(x=690,y=60)

        txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=840,y=60,width=180)

        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2", command=self.seacrh).place(x=1040,y=60,width=110,height=28)

        
        #***********Content***********
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=690,y=100,width=490,height=300)

        scrolly = Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame,orient=HORIZONTAL)

        self.student_table=ttk.Treeview(self.C_Frame,columns=("Name","Roll","Course","Gender","Sem","Sub1","Sub2","Sub3"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.student_table.xview)
        scrolly.config(command=self.student_table.yview)

        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Roll",text="Roll")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Sem",text="Sem")
        self.student_table.heading("Sub1",text="Sub 1")
        self.student_table.heading("Sub2",text="Sub 2")
        self.student_table.heading("Sub3",text="Sub3")
        self.student_table["show"]="headings"

        self.student_table.column("Name",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Sub1",width=100)
        self.student_table.column("Sub2",width=100)
        self.student_table.column("Sub3",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#===============================================================

    def clear(self):
        self.show()
        self.var_name.set("")
        self.var_roll.set("")
        self.var_sem.set("")
        self.var_gender.set("Select")
        self.var_sub1.set("")
        self.var_sub2.set("")
        self.var_sub3.set("")
        self.var_course.set("Select")
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select student from the list first", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student deleted Successfully", parent=self.root)
                        self.clear()     
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def get_data(self, ev):
        self.txt_roll.config(state="readonly")
        r=self.student_table.focus()
        content=self.student_table.item(r)
        row=content["values"]
        self.var_name.set(row[0])
        self.var_roll.set(row[1])
        self.var_course.set(row[2])
        self.var_gender.set(row[3])
        self.var_sem.set(row[4])
        self.var_sub1.set(row[5])
        self.var_sub2.set(row[6])
        self.var_sub3.set(row[7])

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Roll Number already present", parent=self.root)
                else:
                    cur.execute("insert into student(Name,Roll,Course,Gender,Sem,Sub1,Sub2,Sub3) values(?,?,?,?,?,?,?,?)",(
                        self.var_name.get(),
                        self.var_roll.get(),
                        self.var_course.get(),
                        self.var_gender.get(),
                        self.var_sem.get(),
                        self.var_sub1.get(),
                        self.var_sub2.get(),
                        self.var_sub3.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Student Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Student from list", parent=self.root)
                else:
                    cur.execute("update student set Name=?,Course=?,Gender=?,Sem=?,Sub1=?,Sub2=?,Sub3=? where Roll=?",(
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_gender.get(),
                        self.var_sem.get(),
                        self.var_sub1.get(),
                        self.var_sub2.get(),
                        self.var_sub3.get(),
                        self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Student Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def fetch_course(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def seacrh(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from student where roll=?", (self.var_search.get(),))
            row=cur.fetchone()
            if row != None:
                self.student_table.delete(*self.student_table.get_children())
                self.student_table.insert("", END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        
if __name__=="__main__":
    root=Tk()
    obj=studentClass(root)
    root.mainloop()