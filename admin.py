from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from admin_id import Admin_Id

class Admin:

    def __init__(self, root, main_window):
        self.width = 1430
        self.height = 790
        self.root = root
        self.main_window = main_window
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

        Label(f_lbl, text="Username", font=("times new roman", 15, "bold")).place(relx=0.2, rely=0.4)
        Label(f_lbl, text="Password", font=("times new roman", 15, "bold")).place(relx=0.2, rely=0.5)

        self.entry1 = ttk.Entry(f_lbl, width=25, font=("times new roman", 15))
        self.entry1.place(relx=0.3, rely=0.4)

        self.entry2 = ttk.Entry(f_lbl, width=25, font=("times new roman", 15))
        self.entry2.place(relx=0.3, rely=0.5)

        b1 = Button(f_lbl, text="Login", font=("times new roman", 15, "bold"), width=10,
                    command=self.login, height=2, bd=6)
        b1.place(relx=0.25, rely=0.8, anchor=CENTER)

        b2 = Button(f_lbl, text="Exit", font=("times new roman", 15, "bold"), width=10,
                    command=self.on_exit, height=2, bd=6)
        b2.place(relx=0.4, rely=0.8, anchor=CENTER)

    def login(self):
        username = self.entry1.get()
        password = self.entry2.get()
        if username == '' or password == '':
            messagebox.showinfo("", "Fields cannot be empty")
        elif username == 'admin' and password == 'admin':
            self.open_id()
        else:
            messagebox.showinfo("", "Wrong credentials entered")

    def open_id(self):
        self.root.withdraw()
        self.new_window = Toplevel(self.root)
        self.app = Admin_Id(self.new_window, self.root)
        self.new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close_admin_id(self.new_window))
        self.new_window.mainloop()

    def on_close_admin_id(self, admin_id_window):
        admin_id_window.destroy()
        self.root.deiconify()

    def on_exit(self):
        self.root.destroy()
        self.main_window.deiconify()


if __name__ == "__main__":
    root = Tk()
    obj = Admin(root)
    root.mainloop()