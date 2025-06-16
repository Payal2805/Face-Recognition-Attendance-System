from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk       # pip install pillow
from tkinter import messagebox
import os
import tkinter
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from chatbot import ChatBot
import mysql.connector

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x720+0+0")

        #  Varibles
        self.var_email=StringVar()
        self.var_pass=StringVar()

        # bg Image
        img=Image.open(r"Login_img\images1.jpg")
        img=img.resize((1350,720),Image.ANTIALIAS)
        
        self.photoimg=ImageTk.PhotoImage(img)

        bg_lbl=Label(self.root,image=self.photoimg)
        bg_lbl.place(x=0,y=0,width=1350,height=720)

        # first img
        img1=Image.open(r"Login_img\images2.jpg")
        img1=img1.resize((450,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(bg_lbl,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=450,height=130)

       # second img
        img2=Image.open(r"project_img\images22.jpg")
        img2=img2.resize((450,130),Image.ANTIALIAS)
        
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(bg_lbl,image=self.photoimg2)
        f_lbl.place(x=450,y=0,width=450,height=130)

       # third img
        img3=Image.open(r"project_img\images19.jpg")
        img3=img3.resize((450,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(bg_lbl,image=self.photoimg3)
        f_lbl.place(x=900,y=0,width=450,height=130)

        title_lbl=Label(bg_lbl,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=130,width=1350,height=45)

        title_lbl=Label(self.root,text="Note : Enter Valid Username and valid Password  ",font=("times new roman",20,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=660,width=1350,height=40)

        frame=Frame(self.root,bd=2,bg="black")
        frame.place(x=520,y=200,width=340,height=450)

        img4=Image.open(r"Login_img\images6.png")
        img4=img4.resize((100,100),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lbl=Label(image=self.photoimg4,bg="black",borderwidth=0)
        f_lbl.place(x=645,y=210,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=105)

        # Labels
         # User Name
        username_label=Label(frame,text="Username : ",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_label.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

         # Password
        password_label=Label(frame,text="Password : ",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_label.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)
        
        # Show Password img
        show_img=Image.open(r"Login_img\images7.png")
        show_img=show_img.resize((30,25),Image.ANTIALIAS)
        self.photoimg_s=ImageTk.PhotoImage(show_img)
        
        # Hide Password img
        hide_img=Image.open(r"Login_img\images8.png")
        hide_img=hide_img.resize((30,25),Image.ANTIALIAS)
        self.photoimg_h=ImageTk.PhotoImage(hide_img)

        # Show passWord Button
        show_btn=Button(frame,image=self.photoimg_s,cursor="hand2",command=self.show,borderwidth=0,bg="white")
        show_btn.place(x=280,y=250,width=30)


        # ************** Icon Images ****************

        img5=Image.open(r"Login_img\images6.png")
        img5=img5.resize((30,30),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        f_lbl=Label(image=self.photoimg5,bg="black",borderwidth=0)
        f_lbl.place(x=560,y=350,width=30,height=30)


        img6=Image.open(r"Login_img\images2.png")
        img6=img6.resize((30,30),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        f_lbl=Label(image=self.photoimg6,bg="black",borderwidth=0)
        f_lbl.place(x=560,y=420,width=30,height=30)
        
        #Login button
        login_btn=Button(frame,text="Login",command=self.login,cursor="hand2",font=("times new roman",15,"bold"),bd=2,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        login_btn.place(x=110,y=300,width=120,height=35)

        # register button
        register_btn=Button(frame,text="New User Register",command=self.register_window,cursor="hand2",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        register_btn.place(x=15,y=340,width=160)

        # forget password button
        forgetpass_btn=Button(frame,text="Forget Password",command=self.forgot_password_window,cursor="hand2",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpass_btn.place(x=10,y=370,width=160)
    
    # Show password
    def show(self):
        hide_btn=Button(image=self.photoimg_h,cursor="hand2",command=self.hide,borderwidth=0,bg="white")
        hide_btn.place(x=800,y=455,width=30)
        self.txtpass.config(show='')

    # Hide password
    def hide(self):
        show_btn=Button(image=self.photoimg_s,cursor="hand2",command=self.show,borderwidth=0,bg="white")
        show_btn.place(x=800,y=455,width=30)
        self.txtpass.config(show='*')
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field required")

        elif self.txtuser.get()=="payal" and self.txtpass.get()=="payalg":
            #messagebox.showinfo("Success","Welcome to the Project")
            open_main=messagebox.askyesno("YesNo","Access only admin")
            if open_main >0:
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition_System(self.new_window)
            else:
                if not open_main:
                    return
        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="p123@g",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                          
                                                                                          self.txtuser.get(),
                                                                                          self.txtpass.get()
                                                                                       ))
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Inavalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main >0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ******************* Reset password *****************

    def reset_pass(self):
        if self.combo_security.get()=="Select":
            messagebox.showerror("Error","Select the Security Quetion",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Plaese Enter the Answer ",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Plaese Enter the New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="p123@g",database="mydata")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security.get(),self.txt_security.get(),)
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row ==None:
                messagebox.showerror("Error","Plaese Enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset, Plaese login new password",parent=self.root2)
                self.root2.destroy()



    # ****************** Forgot password window *****************************

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Plaese Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="p123@g",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row== None:
                messagebox.showerror("Error","Plaese enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+520+200")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Quetions  ",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select ","Your Birth Place","Your Friend Name","Your Pet Name")
                self.combo_security.place(x=50,y=110,width=250)
                self.combo_security.current(0)
               
                security_A=Label(self.root2,text="Security Answer  ",font=("times new roman",15,"bold"),bg="white")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password  ",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=120,y=290,width=100)





                        
            


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1350x720+0+0")
        #  Varibles
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        # bg Image
        img=Image.open(r"Login_img\images8.jpg")
        img=img.resize((1350,720),Image.ANTIALIAS)
        
        self.photoimg=ImageTk.PhotoImage(img)

        bg_lbl=Label(self.root,image=self.photoimg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # Left Image
        self.bg=ImageTk.PhotoImage(file=r"Login_img\images5.jpg")
        left_lbl=Label(self.root,image=self.bg)
        left_lbl.place(x=90,y=110,width=470,height=500)

        # Frame
        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=560,y=110,width=700,height=500)

        register_lbl=Label(main_frame,text="REGISTER  HERE ",font=("times new roman",25,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # Lable and entry

        # ********* row 1 **********
        frame=Label(main_frame,text="First Name  ",font=("times new roman",15,"bold"),bg="white")
        frame.place(x=50,y=100)

        self.fname_entry=ttk.Entry(main_frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(main_frame,text="Last Name  ",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(main_frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

         # ********* row 2 **********
        contact=Label(main_frame,text="Contact No  ",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(main_frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(main_frame,text="Email  ",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(main_frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

         # ********* row 3 **********
        security_Q=Label(main_frame,text="Select Security Quetions  ",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security=ttk.Combobox(main_frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select ","Your Birth Place","Your Friend Name","Your Pet Name")
        self.combo_security.place(x=50,y=270,width=250)
        self.combo_security.current(0)

        

        security_A=Label(main_frame,text="Security Answer  ",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(main_frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

         # ********* row 4 **********
        pswd=Label(main_frame,text="Password  ",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(main_frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(main_frame,text="Confirm Password  ",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(main_frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # checkButton
        self.var_check=IntVar()
        checkbtn=Checkbutton(main_frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        # Buttons
        img2=Image.open(r"Login_img\images1.png")
        img2=img2.resize((200,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(main_frame,image=self.photoimg2,cursor="hand2",command=self.register_data,borderwidth=0)
        b1.place(x=30,y=420,width=200)

        img3=Image.open(r"Login_img\images4.jpg")
        img3=img3.resize((200,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(main_frame,image=self.photoimg3,cursor="hand2",command=self.return_login,borderwidth=0)
        b1.place(x=330,y=400,width=200)

        # Function Data 
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Plaese Agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="p123@g",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User already exist plaese try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                         
                                                                                         self.var_fname.get(),
                                                                                         self.var_lname.get(),
                                                                                         self.var_contact.get(),
                                                                                         self.var_email.get(),
                                                                                         self.var_securityQ.get(),
                                                                                         self.var_securityA.get(),
                                                                                         self.var_pass.get()
                                                                                      ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
        self.root.destroy()


class Face_Recognition_System:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1350x720+0+0")    
        self.root.title("Face Recognition System")

       # first img
        img=Image.open(r"project_img\images1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

       # second img
        img1=Image.open(r"project_img\images22.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

       # third img
        img2=Image.open(r"project_img\images2.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=400,height=130)

       # bg img
        img3=Image.open(r"project_img\images4.jpg")
        img3=img3.resize((1350,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1350,height=660)

        title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1350,height=45)

        # ************ Time *************
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text= string)
            lbl.after(1000, time)

        lbl=Label(title_lbl,font=("times new roman",15,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()
       
       # student button
        img4=Image.open(r"project_img\images10.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=70,width=220,height=220)

        b1_1=Button(bg_img,text=" Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=260,width=220,height=40)

        # Detect face button
        img5=Image.open(r"project_img\images5.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=70,width=220,height=220)

        b1_1=Button(bg_img,text=" Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=260,width=220,height=40)

        # Attendance button
        img6=Image.open(r"project_img\images6.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=70,width=220,height=220)

        b1_1=Button(bg_img,text=" Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=260,width=220,height=40)

        # ChatBot button
        img7=Image.open(r"project_img\images12.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chatbot_data)
        b1.place(x=1000,y=70,width=220,height=220)

        b1_1=Button(bg_img,text=" ChatBot ",cursor="hand2",command=self.chatbot_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=260,width=220,height=40)

        
        # Train Data button
        img8=Image.open(r"project_img\images7.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=330,width=220,height=220)

        b1_1=Button(bg_img,text=" Train Data ",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=530,width=220,height=40)

        # Photos button
        img9=Image.open(r"project_img\images11.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=330,width=220,height=220)

        b1_1=Button(bg_img,text=" Photos ",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=530,width=220,height=40)

        # Developer button
        img10=Image.open(r"project_img\images9.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=330,width=220,height=220)

        b1_1=Button(bg_img,text=" Developer ",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=530,width=220,height=40)

        # Exit button
        img11=Image.open(r"project_img\images14.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=330,width=220,height=220)

        b1_1=Button(bg_img,text=" Exit ",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=530,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition ","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()

        else :
            return
        
     
    

    # ****************** Functions buttons ***************************
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window) 

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)    

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window) 

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)     

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)  

    def chatbot_data(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window) 



        
        



















if __name__=="__main__":
    main()
    
        