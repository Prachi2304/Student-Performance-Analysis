from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
from student1 import RMS


class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("750x525+300+200")
        self.root.title("Student Performance Analysis")
        self.root.configure(bg="black")
        self.root.resizable(False,False)

        #bg image
        img=Image.open(r"C:\Users\ASUS\Desktop\New folder\logg.jpg")
        img=img.resize((400,525),Image.BILINEAR)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=525)

        frame=LabelFrame(self.root,font=("times new roman",12,"bold"),bg='white',fg='white')
        frame.place(x=425,y=80,width=300,height=300)

        heading=Label(frame,text='SIGN IN',fg='black',bg='white',font=("times new roman",12,"bold"))
        heading.place(x=90,y=0)


        def on_enter(e):
            userentry.delete(0,'end')
        def on_leave(e):
            name=userentry.get()
            if name=='':
                userentry.insert(0,'Username')

        userentry=Entry(frame,width=25,fg='black',border=2,bg='white',font=("times new roman",12,"bold"))
        userentry.place(x=50,y=80)
        userentry.insert(0,'Username')
        userentry.bind('<FocusIn>',on_enter)
        userentry.bind('<FocusOut>',on_leave)


        def on_enter(e):
            userpass.delete(0,'end')
        def on_leave(e):
            name=userpass.get()
            if name=='':
                userpass.insert(0,'Password')

        userpass=Entry(frame,width=25,fg='black',border=2,bg='white',font=("times new roman",12,"bold"))
        userpass.place(x=50,y=130)
        userpass.insert(0,'Password')
        userpass.bind('<FocusIn>',on_enter)
        userpass.bind('<FocusOut>',on_leave)


        def login():
            username=userentry.get()
            password=userpass.get()

            if username=='admin' and password=='admin123':
                messagebox.showinfo("Success","Logging In",parent=self.root)
                self.new_window=Toplevel(self.root)
                self.app=RMS(self.new_window)

            else:
                messagebox.showerror("Error","Wrong password!!",parent=self.root)

        button_login=Button(frame,width=20,pady=7,text='Login',command=login,bg='#57a1f8',fg='white',border=0)
        button_login.place(x=70,y=204)

                

        

        
        
        
        









        

if __name__=="__main__":
    root=Tk()
    object=Login(root)
    root.mainloop()
