import os.path
from tkinter import *
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
from keras.layers import Dense
from keras.layers import Flatten
from keras.models import Sequential
from keras.src.layers import Conv2D, MaxPooling2D
from tkinter import messagebox
from PIL import Image, ImageTk
from details import Details
import os


class Admin_Id:

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

        b1 = Button(f_lbl, text="Student Details", font=("times new roman", 25, "bold"), width=15,
                    command=self.open_details)
        b1.place(relx=0.3, rely=0.3, anchor=CENTER)

        b2 = Button(f_lbl, command=self.train_classifier, text="Train Data", width=15,
                    font=("times new roman", 25, "bold"))
        b2.place(relx=0.3, rely=0.45, anchor=CENTER)

        b3 = Button(f_lbl, command=self.open_img, text="Photos", width=15,
                    font=("times new roman", 25, "bold"))
        b3.place(relx=0.3, rely=0.6, anchor=CENTER)

        b4 = Button(f_lbl, text="Exit", command=self.on_exit, width=15,
                    font=("times new roman", 25, "bold"))
        b4.place(relx=0.3, rely=0.75, anchor=CENTER)

    def open_img(self):
        os.startfile("Data")

    def open_details(self):
        self.root.withdraw()
        self.new_window = Toplevel(self.root)
        self.app = Details(self.new_window, self.root)
        self.new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close_details(self.new_window))
        self.new_window.mainloop()

    def on_close_details(self, details_window):
        details_window.destroy()
        self.root.deiconify()

    def on_exit(self):
        self.root.destroy()
        self.main_window.deiconify()

    def train_classifier(self):
        data_dir = ("Data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training Image", imageNp)

        ids = np.array(ids)
        model = cv2.face.LBPHFaceRecognizer_create()
        model.train(faces, ids)
        model.write("trained_model.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed")


if __name__ == "__main__":
    root = Tk()
    obj = Admin_Id(root)
    root.mainloop()