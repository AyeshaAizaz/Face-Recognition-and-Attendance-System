from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from admin import Admin
import os


class Face_Recognition_System:

    def __init__(self, root):
        self.width = 1430
        self.height = 790
        self.root = root
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        self.root.title("Face Recognition and Attendance System")

        img = Image.open("bg.jpeg")
        img = img.resize((self.width, self.height), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.NEAREST)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=self.width, height=self.height)

        title = Label(f_lbl, text="Face Recognition and Attendance System",
                      font=("times new roman", 40, "bold"), bg='black', fg="white",
                      highlightthickness=0, bd=0)
        title.place(x=0, y=0, width=self.width, height=55)

        std_img = Image.open("Student.webp")
        std_img = std_img.resize((220,220), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.NEAREST)
        self.stdimg = ImageTk.PhotoImage(std_img)

        b1 = Button(f_lbl, image=self.stdimg, cursor="hand2",command=self.open_student)
        b1.place(relx=0.4, rely=0.5, anchor=CENTER)

        b1_1 = Button(f_lbl, text="Student", cursor="hand2", command=self.open_student,
                      font=("times new roman", 15, "bold"), bg='white', fg="black")
        b1_1.place(relx=0.4, rely=0.5, y=90, width=222, height=40, anchor=CENTER)

        admin_img = Image.open("admin.webp")
        admin_img = admin_img.resize((220, 220), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.NEAREST)
        self.admin_img = ImageTk.PhotoImage(admin_img)

        b2 = Button(f_lbl, image=self.admin_img, cursor="hand2", command=self.open_admin)
        b2.place(relx=0.2, rely=0.5, anchor=CENTER)

        b2_2 = Button(f_lbl, text="Admin", cursor="hand2", command=self.open_admin,
                      font=("times new roman", 15, "bold"), bg='white', fg="black")
        b2_2.place(relx=0.2, rely=0.5, y=90, width=222, height=40, anchor=CENTER)

    def open_student(self):
        self.root.withdraw()
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window, self.root)
        self.new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close_student(self.new_window))
        self.new_window.mainloop()

    def on_close_student(self, student_window):
        student_window.destroy()
        self.root.deiconify()

    def on_close_admin(self, admin_window):
        admin_window.destroy()
        self.root.deiconify()

    def open_admin(self):
        self.root.withdraw()
        self.new_window = Toplevel(self.root)
        self.app = Admin(self.new_window, self.root)
        self.new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close_admin(self.new_window))
        self.new_window.mainloop()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()