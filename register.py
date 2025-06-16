from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk       # pip install pillow
from tkinter import messagebox
import mysql.connector

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
        img=Image.open(r"F:\Face Recognition system\Login_img\images8.jpg")
        img=img.resize((1350,720),Image.ANTIALIAS)
        
        self.photoimg=ImageTk.PhotoImage(img)

        bg_lbl=Label(self.root,image=self.photoimg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # Left Image
        self.bg=ImageTk.PhotoImage(file=r"F:\Face Recognition system\Login_img\images5.jpg")
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
        img2=Image.open(r"F:\Face Recognition system\Login_img\images1.png")
        img2=img2.resize((200,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(main_frame,image=self.photoimg2,cursor="hand2",command=self.register_data,borderwidth=0)
        b1.place(x=30,y=420,width=200)

        img3=Image.open(r"F:\Face Recognition system\Login_img\images4.jpg")
        img3=img3.resize((200,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(main_frame,image=self.photoimg3,cursor="hand2",borderwidth=0)
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
        

       






if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
        