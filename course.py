from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3

class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x550+100+170")
        self.root.title("Student Performance Analysis")
        self.root.config(bg="white")
        self.root.focus_force()

        title=Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1230,height=35)

        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()

        title_lbl_course=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        title_lbl_duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        title_lbl_charges=Label(self.root,text="Charges",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        title_lbl_dscription=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)

        ###entryfields

        self.txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_course.place(x=150,y=60,width=200)
        title_text_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        title_text_charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)
        self.txt_description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_description.place(x=150,y=180,width=500,height=130)

        ####buttons
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        ###searchpanel
        self.var_search=StringVar()
        title_lbl_coursename=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)
        txt_course=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60,width=200)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.seacrh).place(x=1090,y=60,width=140,height=28)


        ###content 
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=510,height=340)

        scroll_x=ttk.Scrollbar(self.C_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(self.C_Frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(self.C_Frame,column=("cid","Name","Duration","Charges","description"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("cid",text="Course ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Duration",text="Duration")
        self.student_table.heading("Charges",text="Charges")
        self.student_table.heading("description",text="Description")
        self.student_table["show"]='headings'

        self.student_table.column("cid",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Duration",width=100)
        self.student_table.column("Charges",width=100)
        self.student_table.column("description",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    #########
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0',END)
        self.txt_course.config(state=NORMAL)

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where name=?", (self.var_course.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select course from the list first", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?", (self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Course deleted Successfully", parent=self.root)
                        self.clear()              
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def get_data(self,ev):
        self.txt_course.config(state="readonly")
        self.txt_course
        r=self.student_table.focus()
        content=self.student_table.item(r)
        row=content["values"]
        #print(row)
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        #self.var_course.set(row[4])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
            # Debugging print statements
                print(f"Course: {self.var_course.get()}")
                print(f"Duration: {self.var_duration.get()}")
                print(f"Charges: {self.var_charges.get()}")
                print(f"Description: {self.txt_description.get('1.0', END)}")
            
                cur.execute("select * from course where name=?", (self.var_course.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Course Name already present", parent=self.root)
                else:
                    cur.execute("insert into course (name, duration, charges, description) values(?, ?, ?, ?)", (
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where name=?", (self.var_course.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Course from list", parent=self.root)
                else:
                    cur.execute("update course set duration=?,charges=?,description=? where name=?",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    
    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def seacrh(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")




        
        

        
        
if __name__=="__main__":
    root=Tk()
    object=CourseClass(root)
    root.mainloop()
        
