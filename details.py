import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import openpyxl
import cv2
import numpy as np
import mysql.connector


class Details:

    def __init__(self, root, main_window):
        self.width = 1430
        self.height = 790
        self.root = root
        self.main_window = main_window
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        self.root.title("Face Recognition and Attendance System")

        #Variables

        self.var_enrol = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_add = StringVar()
        self.var_nationality = StringVar()
        self.var_dept = StringVar()
        self.var_sem = StringVar()
        self.var_year = StringVar()
        self.var_r1 = StringVar()

        img = Image.open(r"D:\6th Semester\AI LAB\Project\bg.jpg")
        img = img.resize((self.width, self.height), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.NEAREST)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=self.width, height=self.height)

        title = Label(f_lbl, text="Face Recognition and Attendance System",
                      font=("times new roman", 40, "bold"), bg='black', fg="white",
                      highlightthickness=0, bd=0)
        title.place(x=0, y=0, width=self.width, height=65)

        main_frame = Frame(f_lbl, bd=2, bg='white')
        main_frame.place(x=0, y=66, width=self.width, height=self.height)

        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text="Student Details",
                                font=("times new roman", 25, "bold"), fg="black")
        left_frame.place(relx=0, rely=0, width=710, height=720)

        # Inside Left Frame
        frame2 = LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text="Personal Information",
                            font=("times new roman", 15, "bold"), fg="black")
        frame2.place(x=6, rely=0.02, width=690, height=190)

        # Personal Info
        frame2_1 = Label(frame2, text="Name", font=("times new roman", 12, "bold"), bg='white', fg="black")
        frame2_1.grid(row=0, column=0, padx=10, pady=10)

        std_name = ttk.Entry(frame2, textvariable=self.var_name, width=25, font=("times new roman", 12, "bold"))
        std_name.grid(row=0, column=1, padx=10, pady=10)

        frame2_2 = Label(frame2, text="Gender", font=("times new roman", 12, "bold"), bg='white', fg="black")
        frame2_2.grid(row=0, column=2, padx=5, pady=10)

        combo_gen = ttk.Combobox(frame2, textvariable=self.var_gender, font=("times new roman", 12), width=23, state='readonly')
        combo_gen['values'] = ('Select Gender', 'Male', 'Female')
        combo_gen.current(0)
        combo_gen.grid(row=0, column=3, padx=10, pady=10)

        frame2_3 = Label(frame2,  text="Phone No.", font=("times new roman", 12, "bold"), bg='white', fg="black")
        frame2_3.grid(row=1, column=0, padx=10, pady=10)

        std_no = ttk.Entry(frame2, textvariable=self.var_phone, width=25, font=("times new roman", 12, "bold"))
        std_no.grid(row=1, column=1, padx=10, pady=10)

        frame2_4 = Label(frame2, text="Email", font=("times new roman", 12, "bold"), bg='white', fg="black")
        frame2_4.grid(row=1, column=2, padx=10, pady=10)

        std_email = ttk.Entry(frame2, textvariable=self.var_email, width=25, font=("times new roman", 12, "bold"))
        std_email.grid(row=1, column=3, padx=10, pady=10)

        frame2_5 = Label(frame2, text="Address", font=("times new roman", 12, "bold"), bg='white', fg="black")
        frame2_5.grid(row=2, column=0, padx=10, pady=10)

        std_add = ttk.Entry(frame2, textvariable=self.var_add, width=25, font=("times new roman", 12, "bold"))
        std_add.grid(row=2, column=1, padx=10, pady=10)

        frame2_6 = Label(frame2, text="Nationality", font=("times new roman", 12, "bold"), bg='white', fg="black")
        frame2_6.grid(row=2, column=2, padx=10, pady=10)

        std_nat = ttk.Entry(frame2, textvariable=self.var_nationality, width=25, font=("times new roman", 12, "bold"))
        std_nat.grid(row=2, column=3, padx=10, pady=10)

        # Academic Info
        frame3 = LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text="Academic Information",
                            font=("times new roman", 15, "bold"), fg="black")
        frame3.place(x=6, rely=0.32, width=690, height=170)

        frame3_1 = Label(frame3, text="Enrollment No", font=("times new roman", 12, "bold"), bg='white', fg="black")
        frame3_1.grid(row=0, column=0, padx=10, pady=10)

        std_enroll = ttk.Entry(frame3, textvariable=self.var_enrol, width=22, font=("times new roman", 12, "bold"))
        std_enroll.grid(row=0, column=1, padx=10, pady=10)

        frame3_2 = Label(frame3, text="Department", font=("times new roman", 12, "bold"), bg='white', fg="black")
        frame3_2.grid(row=0, column=2, padx=10, pady=10)

        combo1 = ttk.Combobox(frame3, textvariable=self.var_dept, font=("times new roman", 12), width=20, state='readonly')
        combo1['values'] = ('Select Department', 'CS', 'CE', 'SE', 'AI', 'DS')
        combo1.current(0)
        combo1.grid(row=0, column=3, padx=10, pady=10)

        frame3_3 = Label(frame3, text="Semester", font=("times new roman", 12, "bold"), bg='white', fg="black")
        frame3_3.grid(row=1, column=0, padx=10, pady=10)

        combo2 = ttk.Combobox(frame3, textvariable=self.var_sem, font=("times new roman", 12), width=20, state='readonly')
        combo2['values'] = ('Select Semester', '1', '2', '3', '4', '5', '6', '7', '8')
        combo2.current(0)
        combo2.grid(row=1, column=1, padx=10, pady=10)

        frame3_4 = Label(frame3, text="Year", font=("times new roman", 12, "bold"), bg='white', fg="black")
        frame3_4.grid(row=1, column=2, padx=10, pady=10)

        combo3 = ttk.Combobox(frame3, textvariable=self.var_year, font=("times new roman", 12), width=20, state='readonly')
        combo3['values'] = ('Select Year', 'First', 'Second', 'Third', 'Fourth', 'Fifth')
        combo3.current(0)
        combo3.grid(row=1, column=3, padx=10, pady=10)

        radio_btn1 = tkinter.Radiobutton(frame3, text="Take Photo Sample", value="Yes", background='white',
                                         font=("times new roman", 12), foreground='black', variable=self.var_r1)
        radio_btn1.grid(row=2, column=0, padx=10, pady=10)

        radio_btn2 = tkinter.Radiobutton(frame3, text="No Photo Sample",  value="No", background='white',
                                         font=("times new roman", 12), foreground='black', variable=self.var_r1)
        radio_btn2.grid(row=2, column=1, padx=10, pady=10)

        # Frame 4
        frame4 = LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE)
        frame4.place(x=6, rely=0.6, width=690, height=270)

        # Inside Frame 4
        save_btn = Button(frame4, text="Save", command=self.add_data, font=("times new roman", 15, "bold"), width=15,
                          bg='white', fg='black', bd=2)
        save_btn.place(relx=0.3, rely=0.2, anchor=CENTER)

        update_btn = Button(frame4, text="Update", command=self.update, font=("times new roman", 15, "bold"), width=15,
                            bg='white', fg='black', bd=2)
        update_btn.place(relx=0.65, rely=0.2, anchor=CENTER)

        del_btn = Button(frame4, text="Delete", command=self.delete_data, font=("times new roman", 15, "bold"), width=15,
                         bg='white', fg='black', bd=2)
        del_btn.place(relx=0.3, rely=0.4, anchor=CENTER)

        reset_btn = Button(frame4, text="Reset", command=self.reset, font=("times new roman", 15, "bold"), width=15,
                           bg='white', fg='black', bd=2)
        reset_btn.place(relx=0.65, rely=0.4, anchor=CENTER)

        take_photo_btn = Button(frame4, command=self.generate_dataset, text="Take Photo", font=("times new roman", 15, "bold"), width=15,
                                bg='white', fg='black', bd=2)
        take_photo_btn.place(relx=0.3, rely=0.6, anchor=CENTER)

        back_btn = Button(frame4, command=self.on_back, text="Back", font=("times new roman", 15, "bold"), width=15,
                          bg='white', fg='black', bd=2)
        back_btn.place(relx=0.65, rely=0.6, anchor=CENTER)

        # Right Frame
        right_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE)
        right_frame.place(relx=0.5, rely=0, width=710, height=720)

        search_frame = LabelFrame(right_frame, bd=2, bg='white', relief=RIDGE)
        search_frame.place(x=6, rely=0.01, width=690, height=60)

        search_lbl = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"),
                           bg='white', fg='black')
        search_lbl.grid(row=0, column=0, padx=10, pady=10)

        combo_search = ttk.Combobox(search_frame, font=("times new roman", 12), width=20, state='readonly')
        combo_search['values'] = ('Select', 'Enrollment', 'Name', 'Phone No', 'Email', 'Address', 'Department',
                              'Semester', 'Year', 'Nationality', 'Gender')
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=10, pady=10)

        entry_search = ttk.Entry(search_frame, width=20, font=("times new roman", 12))
        entry_search.grid(row=0, column=2, padx=10, pady=10)

        search_btn = Button(search_frame, text="Search", font=("times new roman", 12, "bold"), width=7,
                                  bg='white', fg='black', bd=1)
        search_btn.grid(row=0, column=3, padx=10, pady=10)

        showAll_btn = Button(search_frame, text="Show All", font=("times new roman", 12, "bold"), width=7,
                            bg='white', fg='black', bd=1)
        showAll_btn.grid(row=0, column=4, padx=10, pady=10)

        table_frame = LabelFrame(right_frame, bd=2, bg='white', relief=RIDGE)
        table_frame.place(x=6, rely=0.1, width=690, height=640)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=('Enrol', 'Name', 'Gender', 'Phone', 'Email',
                                                               'Add', 'Nationality', 'Dept', 'Sem', 'Year',
                                                               'photo'), xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('Enrol', text='Enrollment')
        self.student_table.heading('Name', text='Name')
        self.student_table.heading('Gender', text='Gender')
        self.student_table.heading('Phone', text='Phone No.')
        self.student_table.heading('Email', text='Email')
        self.student_table.heading('Add', text='Address')
        self.student_table.heading('Nationality', text='Nationality')
        self.student_table.heading('Dept', text='Department')
        self.student_table.heading('Sem', text='Semester')
        self.student_table.heading('Year', text='Year')
        self.student_table.heading('photo', text='Photo Sample')
        self.student_table["show"] = 'headings'

        self.student_table.column('Enrol', width=100)
        self.student_table.column('Name', width=100)
        self.student_table.column('Gender', width=100)
        self.student_table.column('Phone', width=100)
        self.student_table.column('Email', width=100)
        self.student_table.column('Add', width=100)
        self.student_table.column('Nationality', width=100)
        self.student_table.column('Dept', width=100)
        self.student_table.column('Sem', width=100)
        self.student_table.column('Year', width=100)
        self.student_table.column('photo', width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if (
            self.var_enrol.get() == ""
            or self.var_name.get() == ""
            or self.var_gender.get() == "Select Gender"
            or self.var_add.get() == ""
            or self.var_phone.get() == ""
            or self.var_email.get() == ""
            or self.var_nationality.get() == ""
            or self.var_dept.get() == "Select Department"
            or self.var_sem.get() == "Select Semester"
            or self.var_year.get() == "Select Year"
        ):
            messagebox.showerror("Error", "Fields cannot be empty", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Ahmed_14092001", database='face_recognizer')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_enrol.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_add.get(),
                    self.var_nationality.get(),
                    self.var_dept.get(),
                    self.var_sem.get(),
                    self.var_year.get(),
                    self.var_r1.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details has been added Successfully",
                                    parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Ahmed_14092001",
                                       database='face_recognizer')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)

            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_enrol.set(data[0])
        self.var_name.set(data[1])
        self.var_gender.set(data[2])
        self.var_phone.set(data[3])
        self.var_email.set(data[4])
        self.var_add.set(data[5])
        self.var_nationality.set(data[6])
        self.var_dept.set(data[7])
        self.var_sem.set(data[8])
        self.var_year.set(data[9])
        self.var_r1.set(data[10])

    def update(self):
        if (
            self.var_enrol.get() == ""
            or self.var_name.get() == ""
            or self.var_gender.get() == "Select Gender"
            or self.var_add.get() == ""
            or self.var_phone.get() == ""
            or self.var_email.get() == ""
            or self.var_nationality.get() == ""
            or self.var_dept.get() == "Select Department"
            or self.var_sem.get() == "Select Semester"
            or self.var_year.get() == "Select Year"
        ):
            messagebox.showerror("Error", "Fields cannot be empty", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update data?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Ahmed_14092001",
                                                   database='face_recognizer')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Name=%s, Gender=%s, Number=%s, Email=%s, "
                                      "Address=%s, Nationality=%s, Department=%s, Semester=%s, Year=%s, PhotoSample=%s where Enrollment=%s", (
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        self.var_add.get(),
                        self.var_nationality.get(),
                        self.var_dept.get(),
                        self.var_sem.get(),
                        self.var_year.get(),
                        self.var_r1.get(),
                        self.var_enrol.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def delete_data(self):
        selected_item = self.student_table.selection()

        if not selected_item or self.var_enrol.get() == "":
            messagebox.showerror("Error", "Please select a record to delete.", parent=self.root)
        else:
            try:
                delete_confirmation = messagebox.askyesno(
                    "Delete", "Do you want to delete this student?", parent=self.root
                )

                if delete_confirmation > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Ahmed_14092001",
                                                   database='face_recognizer')
                    my_cursor = conn.cursor()
                    sql = "delete from student where Enrollment=%s"
                    val = (self.var_enrol.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete_confirmation:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def reset(self):
        self.var_enrol.set("")
        self.var_name.set("")
        self.var_gender.set("Select Gender")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_add.set("")
        self.var_nationality.set("")
        self.var_dept.set("Select Department")
        self.var_sem.set("Select Semester")
        self.var_year.set("Select Year")
        self.var_r1.set("")

    def on_back(self):
        self.root.destroy()
        self.main_window.deiconify()

    def generate_dataset(self):
        if (
                self.var_enrol.get() == ""
                or self.var_name.get() == ""
                or self.var_gender.get() == "Select Gender"
                or self.var_add.get() == ""
                or self.var_phone.get() == ""
                or self.var_email.get() == ""
                or self.var_nationality.get() == ""
                or self.var_dept.get() == "Select Department"
                or self.var_sem.get() == "Select Semester"
                or self.var_year.get() == "Select Year"
        ):
            messagebox.showerror("Error", "Fields cannot be empty", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Ahmed_14092001",
                                               database='face_recognizer')
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myres = my_cursor.fetchall()
                id=0
                for x in myres:
                    id+=1
                my_cursor.execute("update student set Name=%s, Gender=%s, Number=%s, Email=%s, "
                                      "Address=%s, Nationality=%s, Department=%s, Semester=%s, Year=%s, PhotoSample=%s where Enrollment=%s",
                                      (
                                          self.var_name.get(),
                                          self.var_gender.get(),
                                          self.var_phone.get(),
                                          self.var_email.get(),
                                          self.var_add.get(),
                                          self.var_nationality.get(),
                                          self.var_dept.get(),
                                          self.var_sem.get(),
                                          self.var_year.get(),
                                          self.var_r1.get(),
                                          self.var_enrol.get()
                                      ))
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(image):
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = image[y:y + h, x:x + w]
                        if not face_cropped.size == 0:
                            return face_cropped
                        else:
                            print("faces_cropped is empty")

                    return None

                cam = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cam.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"Data/user.{str(id)}.{str(img_id)}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(np.array(face), str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0),2)
                        cv2.imshow("Cropped Face", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating datasets completed")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


"""if __name__ == "__main__":
    root = Tk()
    obj = Details(root)
    root.mainloop()"""

