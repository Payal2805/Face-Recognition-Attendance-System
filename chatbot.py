from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk            # pip install pillow


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x650+0+0")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg="powder blue",width=610)
        main_frame.pack()


        img_chat=Image.open(r"project_img\images12.jpg")
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg_chat=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg_chat,text="       CHAT  ME  ",font=("arial",30,"bold"),fg="green",bg="white")
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',15),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg="white",width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Something",font=("times new roman",14,"bold"),fg="green",bg="white")
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()

        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=30,font=("times new roman",16,"bold"))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send >>",command=self.send,font=("times new roman",15,"bold"),width=8,bg="green",fg="white")
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clare=Button(btn_frame,text="Clear Data",command=self.clear,font=("times new roman",15,"bold"),width=8,bg="red",fg="white")
        self.clare.grid(row=1,column=0,padx=5,sticky=W)
        
        self.msg=""
        self.label_2=Label(btn_frame,text=self.msg,font=("times new roman",14,"bold"),fg="red",bg="white")
        self.label_2.grid(row=1,column=1,padx=5,sticky=W)

     #******************* Function Declaretion ************************

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self):
        send="\t\t\t"+" You : "+self.entry.get()
        self.text.insert(END,"\n"+send)
        self.text.yview(END)

        if (self.entry.get()==""):
            self.msg="Please Enter Some Input"
            self.label_2.config(text=self.msg,fg="red")

        else:
            self.msg=""
            self.label_2.config(text=self.msg,fg="red")

        if (self.entry.get()=='hello'):
            self.text.insert(END,"\n\n"+" Bot : Hi")

        elif(self.entry.get()=='hi'):
            self.text.insert(END,"\n\n"+"Bot : Hello")

        elif(self.entry.get()=='how are you'):
            self.text.insert(END,"\n\n"+"Bot : Fine and you")

        elif(self.entry.get()=='fantastic'):
            self.text.insert(END,"\n\n"+"Bot : Nice To Hear")

        elif(self.entry.get()=='who created you'):
            self.text.insert(END,"\n\n"+"Bot : Payal-G did using Python")

        elif(self.entry.get()=='what is your name'):
            self.text.insert(END,"\n\n"+"Bot : My name is Mr. Hacker")

        elif(self.entry.get()=='bye'):
            self.text.insert(END,"\n\n"+"Bot : Thank you for Chatting")

        elif(self.entry.get()=='can you speak Marathi'):
            self.text.insert(END,"\n\n"+"Bot : I'm still learning it......")

        elif(self.entry.get()=='what is machine learning'):
            self.text.insert(END,"\n\n"+"Bot : Machine learning is an umbrella term for solving\nproblems for which development of algorithms by\nhuman programmers would be cost-prohibitive, and \ninstead the problems are solved by helping machines \n'discover' their 'own' algorithms, without needing to be\nexplicitly told what to do by any human-developed \nalgorithms.")

        elif(self.entry.get()=='how does face recognition work'):
            self.text.insert(END,"\n\n"+"Bot : It works by identifying and measuring facial \nfeatures in an image. Facial recognition can identify \nhuman faces in images or videos, determine if \nthe face in two images belongs to the same person, \nor search for a face among a large collection of existing \nimages.")

        elif(self.entry.get()=='how does face recognition work stap by stap'):
            self.text.insert(END,"\n\n"+"Bot : Step 1: \nFace detection :The camera detects and locates the image\n of a face, either alone or in a crowd.\nStep 2: \nFace analysis : Most facial recognition technology relies \non 2D rather than 3D images because it can more \nconveniently match a 2D image with public photos \nor those in a database.\nStep 3: \nConverting the image to data The face capture \nprocess transforms analog information (a face) \ninto a set of digital information (data) \nbsed on the person's facial features.\nStep 4: \nFinding a match Your faceprint is then \ncompared against a database of other \nknown faces. ")
        
        elif(self.entry.get()=='how many countries ues facial recognition'):
            self.text.insert(END,"\n\n"+"Bot : In total, there are \nnow 109 countries today that are either \nusing or have approved the use of facial \nrecognition technology for surveillance \npurposes. ")

        elif(self.entry.get()=='what is python programming'):
            self.text.insert(END,"\n\n"+"Bot : Python is a high-level, general-purpose \nprogramming language. Its design philosophy \nemphasizes code readability with the use of \nsignificant indentation via the off-side rule.\n Python is dynamically typed and \ngarbage-collected.")

        
        elif(self.entry.get()=='what is chatbot'):
            self.text.insert(END,"\n\n"+"Bot : A chatbot is a software application that aims to mimic \nhuman conversation through text or voice interactions, \ntypically online.")

        elif(self.entry.get()=='good' or self.entry.get()=='fine'):
            self.text.insert(END,"\n\n"+"Bot : Ok what can I do for you..!")

        elif(self.entry.get()=='YZ' or self.entry.get()=='yz' or self.entry.get()=='MC' or self.entry.get()=='mc' or self.entry.get()=='BC' or self.entry.get()=='bc'):
            self.text.insert(END,"\n\n"+"Bot : Excuse Me..! Mind your Language #@#@#.")

           
        else:
            self.text.insert(END,"\n\n"+"Bot : Sorry I dindn't get it")   















    

        
       


if __name__=='__main__':
    root=Tk()
    obj= ChatBot(root) 
    root.mainloop()       
        
