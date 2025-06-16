from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1350x720+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK ",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1350,height=45)

        img_top=Image.open(r"project_img\images33.jpg")
        img_top=img_top.resize((1350,675),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1350,height=675)

        dev_label=Label(f_lbl,text="Email : payaljadhav157@gmail.com ",font=("times new roman",19,"bold"),fg="blue",bg="white")
        dev_label.place(x=470,y=200)


if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()