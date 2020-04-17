import tkinter
from tkinter import messagebox
from database import *


class Student(tkinter.Toplevel):
    def __init__(self):
        pass

    def initialising_student(self):
        self.student_window = tkinter.Tk()
        self.student_window.geometry("300x250")
        self.student_window.title("Students")
        self.student_window.configure(background="#c9af98")

        self.search_frame = tkinter.Frame(self.student_window)
        self.search_frame.configure(background="#c9af98")
        self.welcome_label = tkinter.Label(self.search_frame, text="WELCOME Deep Upadhyay,", font='bold')
        self.welcome_label.configure(background="#c9af98")

        self.welcome_label.grid(row=0, column=0, columnspan=2, padx=30, pady=20)

        self.student_id = tkinter.StringVar()
        self.form_id(self.search_frame, "Student", self.student_id, 1, 0, 1, 1, 0, 5)

        # Buttons : Submit
        self.submit_button = tkinter.Button(self.search_frame,
                                            text='Submit', command=self.submit_data)
        self.quit_button = tkinter.Button(self.search_frame,
                                          text='Quit',
                                          command=self.student_window.destroy)
        self.submit_button.grid(row=2, column=0, padx=10, pady=20, ipadx=10)
        self.quit_button.grid(row=2, column=1, ipadx=10)

        self.search_frame.grid(row=0, column=0)
        tkinter.mainloop()

    def form_id(self, frame, text, variable, label_row, label_column, entry_row, entry_column, padx, pady):
        self.student_id_label = tkinter.Label(frame, text=text + " ID : ")
        self.student_id_label.configure(background="#c9af98")
        self.student_id_entry = tkinter.Entry(frame, width=15, font=("Calibri", 12),
                                              textvariable=variable)
       
        self.student_id_label.grid(row=label_row, column=label_column, pady=pady)
        self.student_id_entry.grid(row=entry_row, column=entry_column)

    def submit_data(self):

        if self.student_id.get():
            student_record = database_connection('select * from '+DATABASE_NAME+'.student where student_id='+self.student_id.get(), '1', 0)
            course_record = database_connection('select * from '+DATABASE_NAME+'.course where course_id='+str(student_record[8]), '1', 0)

            self.column_label = tkinter.Label(self.search_frame, text="Course        Grade")
            self.column_label.configure(background="#c9af98")
            self.column_data = tkinter.Label(self.search_frame, text=str(course_record[2])+"            "+str(student_record[3]))
            self.column_data.configure(background="#c9af98")
            self.column_label.grid(row=3, column=0, pady=5, columnspan=2)
            self.column_data.grid(row=4, column=0, pady=5, columnspan=2)
        else:
            # No Input provided.
            pass


# student = Student()
# student.initialising_student()