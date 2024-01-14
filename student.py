from datetime import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import mysql.connector


class Student:

    def __init__(self, student_root, main_window):
        self.width = 1430
        self.height = 790
        self.root = student_root
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

        b1 = Button(f_lbl, command=self.recognition, text="Mark Attendance", font=("times new roman", 25, "bold"),
                    width=15, bg='white', fg='black')
        b1.place(relx=0.25, rely=0.4, anchor=CENTER)

        b2 = Button(f_lbl, text="Exit", command=self.on_exit, font=("times new roman", 25, "bold"),
                    width=15, bg='white', fg='black')
        b2.place(relx=0.25, rely=0.6, anchor=CENTER)

    def on_exit(self):
        self.root.destroy()
        self.main_window.deiconify()

    def attendance(self, i, e):
        with open("attendance.csv", "r+", newline="\n") as f:
            mydata = f.readlines()
            nameList = []
            for line in mydata:
                entry = line.split((","))
                nameList.append(entry[0])
            if((e not in nameList) and (i not in nameList)):
                now=datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dt = now.strftime("%H:%M:%S")
                f.writelines(f'\n{e},{i},{dt},{d1},Present')
    def recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
            coord = []
            for (x,y,w,h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_img[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Ahmed_14092001",
                                               database='face_recognizer')
                my_cursor = conn.cursor()
                my_cursor.execute("select Name from student where Enrollment="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute("select Enrollment from student where Enrollment=" + str(id))
                e = my_cursor.fetchone()
                e = "+".join(e)

                if confidence > 77:  # Adjust the confidence threshold as needed
                    cv2.putText(img, f'Enrollment: {e}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                (255, 255, 255), 2)
                    cv2.putText(img, f'Name: {i}', (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                (255, 255, 255), 2)
                    self.attendance(i,e)
                else:
                    cv2.putText(img, 'Unknown', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, face_cascade):
            coord = draw_boundary(img, face_cascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        video_capture = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        # Load the trained CNN model
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("trained_model.xml")

        while True:
            _, img = video_capture.read()
            img = recognize(img, clf, face_cascade)
            cv2.imshow("face recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()