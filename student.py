from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkcalendar import DateEntry


class Student:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1350x720+0+0")
        self.root.title("Face Recognition System")


        # ************ Variables ***********
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()


       # first img
        img=Image.open(r"project_img\images15.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

       # second img
        img1=Image.open(r"project_img\images19.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

       # third img
        img2=Image.open(r"project_img\images16.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=400,height=130)

       # bg img
        img3=Image.open(r"project_img\images4.jpg")
        img3=img3.resize((1350,720),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1350,height=660)

        title_lbl=Label(bg_img,text="STUDENT  MANAGEMENT  SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1350,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=50,width=1350,height=600)

        #left lable frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=8,width=660,height=500)

        img_left=Image.open(r"project_img\images20.jpg")
        img_left=img_left.resize((650,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=650,height=100)

         # current course Information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=105,width=650,height=110)

        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","IT","CS","BMS")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        dep_lab=Label(current_course_frame,text="*",font=("times new roman",13,"bold"),bg="white",fg="red").place(x=320,y=5)

         # Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","AWP","Java","Python","DS","DBMS","Hacking")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        course_lab=Label(current_course_frame,text="*",font=("times new roman",13,"bold"),bg="white",fg="red").place(x=620,y=5)


         # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        year_lab=Label(current_course_frame,text="*",font=("times new roman",13,"bold"),bg="white",fg="red").place(x=320,y=50)

         # Semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        sem_combo["values"]=("Select Semester","Semester I","Semester II","Semester III","Semester IV","Semester V","Semester VI")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        sem_lab=Label(current_course_frame,text="*",font=("times new roman",13,"bold"),bg="white",fg="red").place(x=620,y=50)


         # Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=215,width=650,height=260)

        # Student ID
        studentId_label=Label(class_student_frame,text="Student ID",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=2,pady=4,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=2,pady=4,sticky=W)

        studentId_lab=Label(class_student_frame,text="*",font=("times new roman",13,"bold"),bg="white",fg="red").place(x=313,y=1)


         # Student Name
        studentName_label=Label(class_student_frame,text="Student Name",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=5,pady=4,sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=5,pady=4,sticky=W)

        studentName_lab=Label(class_student_frame,text="*",font=("times new roman",13,"bold"),bg="white",fg="red").place(x=630,y=1)

        # Roll No
        roll_no_label=Label(class_student_frame,text="Roll NO",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=0,padx=2,pady=4,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=1,padx=2,pady=4,sticky=W)

        roll_lab=Label(class_student_frame,text="*",font=("times new roman",13,"bold"),bg="white",fg="red").place(x=313,y=30)

        # Phone No
        phone_label=Label(class_student_frame,text="Phone No",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=2,column=2,padx=5,pady=4,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=2,column=3,padx=5,pady=4,sticky=W)

        phone_lab=Label(class_student_frame,text="*",font=("times new roman",13,"bold"),bg="white",fg="red").place(x=630,y=30)

        # Gender
        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=5,pady=4,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=20)
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=4,sticky=W)

        gender_lab=Label(class_student_frame,text="*",font=("times new roman",13,"bold"),bg="white",fg="red").place(x=313,y=60)

        # DOB
        dob_label=Label(class_student_frame,text="DOB",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=1,column=2,padx=5,pady=4,sticky=W)
        
       
        cal=DateEntry(class_student_frame,selectmode="day",width=18,textvariable=self.var_dob,font=("times new roman",13,"bold"))
        cal.grid(row=1,column=3,padx=5,pady=4,sticky=W)

        dob_lab=Label(class_student_frame,text="*",font=("times new roman",13,"bold"),bg="white",fg="red").place(x=630,y=60)
       

        # Email
        email_label=Label(class_student_frame,text="Email ID",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=5,pady=4,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=2,pady=4,sticky=W)

        email_lab=Label(class_student_frame,text="*",font=("times new roman",13,"bold"),bg="white",fg="red").place(x=313,y=95)

        # Address
        address_label=Label(class_student_frame,text="Address",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=3,column=2,padx=5,pady=4,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=3,column=3,padx=5,pady=4,sticky=W)

        address_lab=Label(class_student_frame,text="*",font=("times new roman",13,"bold"),bg="white",fg="red").place(x=630,y=95)

        
        # radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes",cursor="hand2")
        radiobtn1.grid(row=4,column=0)

        radio1_lab=Label(class_student_frame,text="*",font=("times new roman",13,"bold"),bg="white",fg="red").place(x=130,y=130)
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No",cursor="hand2")
        radiobtn2.grid(row=4,column=1)

        # buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=165,width=645,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,cursor="hand2",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,cursor="hand2",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,cursor="hand2",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,cursor="hand2",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

         # buttons frame
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=200,width=645,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,cursor="hand2",width=31,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",command=self.generate_dataset,cursor="hand2",width=31,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


       #right lable frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=8,width=645,height=500)

        img_right=Image.open(r"project_img\images18.jpg")
        img_right=img_right.resize((640,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=0,y=0,width=640,height=130)

        # Search System
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=630,height=70)

        search_label=Label(search_frame,text="Search By :",font=("times new roman",13,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Name","Roll_No","Phono_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=3,pady=4,sticky=W)


        search_btn=Button(search_frame,text="Search",cursor="hand2",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)

        showAll_btn=Button(search_frame,text="Show All",cursor="hand2",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=2)

        # table Frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=630,height=265)
        
        # Scrollbar 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","roll","phone","gender","dob","email","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Headings
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email ID")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # *************************** Function Detection **************************

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" :
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else :
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="p123@g",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_radio1.get()
                      
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es :
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    

    #******************** Fetch Data ****************
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="p123@g",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data= my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data :
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #***************** get cursor **************
    def get_cursor(self ,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12]),

    #  update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" :
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="p123@g",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                          self.var_dep.get(),                              
                                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                                          self.var_semester.get(),              
                                                                                                                                                                                          self.var_std_name.get(),
                                                                                                                                                                                          self.var_roll.get(),
                                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                                          self.var_phone.get(),
                                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                                          self.var_radio1.get(), 
                                                                                                                                                                                          self.var_std_id.get()             

                                                                                                                                                                                         ))
                else: 
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details successfylly update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es :
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    # Delete Function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="p123@g",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student detials",parent=self.root)
            except Exception as es :
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                    
    # reset funtion
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")
    
    #************* Generate data set or Take photo Smaples***************
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_radio1.get()=="No" :
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="p123@g",database="face_recognizer")
               my_cursor=conn.cursor()
               my_cursor.execute("select * from student ")
               myreshult=my_cursor.fetchall()
               id=0
               for x in myreshult:
                   id+=1
               my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                          self.var_dep.get(),                              
                                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                                          self.var_semester.get(),              
                                                                                                                                                                                          self.var_std_name.get(),
                                                                                                                                                                                          self.var_roll.get(),
                                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                                          self.var_phone.get(),
                                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                                          self.var_radio1.get(), 
                                                                                                                                                                                          self.var_std_id.get()==id+1             

                                                                                                                                                                                         ))
               conn.commit()
               self.fetch_data()
               self.reset_data()
               conn.close()

               #************** Load predifiend data on face frontals from opevcv ****************

               face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

               def face_cropped(img):
                   gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
                   faces=face_classifier.detectMultiScale(gray,1.3,5)
                   # scaling factor=1.3
                   # Minimum Neighbor=5

                   for (x,y,w,h) in faces:
                       face_cropped=img[y:y+h,x:x+w]
                       return face_cropped
                   
               cap=cv2.VideoCapture(0)
               img_id=0
               while True:
                   ret,my_frame=cap.read()
                   if face_cropped(my_frame) is not None:
                       img_id+=1
                       face=cv2.resize(face_cropped(my_frame),(450,450))
                       face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                       file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                       cv2.imwrite(file_name_path,face)
                       cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                       cv2.imshow("Crooped Fase",face)

                   if cv2.waitKey(1)==13 or int(img_id)==100:
                       break
                   
               cap.release()
               cv2.destroyAllWindows()
               messagebox.showinfo("Result","Generating data sets compled !!!",parent=self.root)
            
            except Exception as es :
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)











                 
    
        
if __name__=="__main__":
    root=Tk()
    obj= Student(root)
    root.mainloop()