from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1350x720+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER ",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1350,height=45)

        img_top=Image.open(r"project_img\images30.jpg")
        img_top=img_top.resize((1350,675),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1350,height=675)

        lbl_email=Label(self.root,text="payaljadhav157@gmail.com",font=("Elephant",30,"bold"),bg="lightblue",fg="black")
        lbl_email.place(x=20,y=110,width=790,height=50)

        # frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=830,y=5,width=500,height=600)

        img_top1=Image.open(r"project_img\payalg.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        # Developer
        dev_label=Label(main_frame,text="Hello\n My Name, Payal ",font=("Elephant",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am\n Full Stack Developer ",font=("Andalus",19,"bold"),fg="#767171",bg="white")
        dev_label.place(x=0,y=75)

        # Logo img
        img=Image.open(r"Login_img\logo2.png")
        img=img.resize((70,70),Image.ANTIALIAS)
        self.photoimg_h=ImageTk.PhotoImage(img)

        img1=Image.open(r"Login_img\logo3.png")
        img1=img1.resize((90,70),Image.ANTIALIAS)
        self.photoimg_h1=ImageTk.PhotoImage(img1)

        img2=Image.open(r"Login_img\logo4.png")
        img2=img2.resize((70,70),Image.ANTIALIAS)
        self.photoimg_h2=ImageTk.PhotoImage(img2)

        img3=Image.open(r"Login_img\logo1.jpg")
        img3=img3.resize((70,70),Image.ANTIALIAS)
        self.photoimg_h3=ImageTk.PhotoImage(img3)

        # Logo Button
        show_btn=Button(main_frame,image=self.photoimg_h,cursor="hand2",borderwidth=0,bg="white")
        show_btn.place(x=10,y=140,width=70)

        show_btn=Button(main_frame,image=self.photoimg_h1,cursor="hand2",borderwidth=0,bg="white")
        show_btn.place(x=70,y=140,width=80)

        show_btn=Button(main_frame,image=self.photoimg_h2,cursor="hand2",borderwidth=0,bg="white")
        show_btn.place(x=150,y=140,width=70)

        show_btn=Button(main_frame,image=self.photoimg_h3,cursor="hand2",borderwidth=0,bg="white")
        show_btn.place(x=220,y=140,width=70)

        img_top2=Image.open(r"project_img\images31.jpg")
        img_top2=img_top2.resize((500,390),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(main_frame,image=self.photoimg_top2)
        f_lbl.place(x=0,y=210,width=500,height=390)





if __name__=="__main__":
    root=Tk()
    obj= Developer(root)
    root.mainloop()