import tkinter
from tkinter import *
from tkinter import messagebox
from database import *
from functools import partial

class ProfessorHome():
    COURSES = ['--Select--']

    def __init__(self):     # Loading All Courses from Database
        course_record = database_connection('SELECT * FROM '+DATABASE_NAME+'.course;', 'all', 0)
        if len(course_record) != 0:
            for row in course_record:
                self.COURSES.append(row[2])

    def initializing_professor(self):
        self.prof_window = tkinter.Tk()
        self.prof_window.geometry("700x600")
        self.prof_window.title("Professor")
        self.prof_window.configure(background="#c9af98")


        self.title_label = tkinter.Label(self.prof_window)
        self.title_label.place(relx=0.135, rely=0.051, height=41, width=484)
        self.title_label.configure(background="#c9af98")
        self.title_label.configure(font="-family {Lucida Sans} -size 15 -weight"
                                         " bold")
        self.title_label.configure(text='''~ ~ View Professor ~ ~''')


        self.prof_id_label = tkinter.Label(self.prof_window, text="Professor ID : ")
        self.prof_id_label.place(relx=0.155, rely=0.251, height=41, width=175)
        self.prof_id_label.configure(background="#c9af98")
        self.prof_id_label.configure(font="-family {Lucida Sans} -size 12 -weight"
                                         " bold")

        self.prof_id = tkinter.Label(self.prof_window, text="P003452")
        self.prof_id .place(relx=0.465, rely=0.251, height=41, width=200)
        self.prof_id .configure(background="#c9af98")
        self.prof_id .configure(font="-family {Lucida Sans} -size 12 -weight"
                                         " bold")

        self.prof_name_label = tkinter.Label(self.prof_window, text="Professor Name :")
        self.prof_name_label.place(relx=0.155, rely=0.351, height=41, width=200)
        self.prof_name_label.configure(background="#c9af98")
        self.prof_name_label.configure(font="-family {Lucida Sans} -size 12 -weight bold")

        self.prof_name = tkinter.Label(self.prof_window, text="Ahmad Alhamed")
        self.prof_name.place(relx=0.465, rely=0.351, height=41, width=200)
        self.prof_name.configure(background="#c9af98")
        self.prof_name.configure(font="-family {Lucida Sans} -size 12 -weight  bold")


        self.prof_email_label = tkinter.Label(self.prof_window, text="Email / Username : " )
        self.prof_email_label.place(relx=0.155, rely=0.451, height=41, width=200)
        self.prof_email_label.configure(background="#c9af98")
        self.prof_email_label.configure(font="-family {Lucida Sans} -size 12 -weight bold")

        self.prof_email = tkinter.Label(self.prof_window, text="alhamed.ahmad@mylambton.ca")
        self.prof_email.place(relx=0.465, rely=0.451, height=41, width=300)
        self.prof_email.configure(background="#c9af98")
        self.prof_email.configure(font="-family {Lucida Sans} -size 12 -weight bold")

        self.prof_phone_label = tkinter.Label(self.prof_window, text="Phone No.:")
        self.prof_phone_label.place(relx=0.155, rely=0.551, height=41, width=200)
        self.prof_phone_label.configure(background="#c9af98")
        self.prof_phone_label.configure(font="-family {Lucida Sans} -size 12 -weight bold")

        self.prof_phone = tkinter.Label(self.prof_window, text="+1-416-345-3452")
        self.prof_phone.place(relx=0.465, rely=0.551, height=41, width=200)
        self.prof_phone.configure(background="#c9af98")
        self.prof_phone.configure(font="-family {Lucida Sans} -size 12 -weight bold")

        # self.add_button = tkinter.Button(self.prof_window,
        #                                  text='Add Grades',
        #                                  command=self.add_grade)
        # self.add_button.place(relx=0.150, rely=0.736, height=44, width=120)
        # self.add_button.configure(background="#bfbfbf")
        # self.add_button.configure(font="-family {Segoe UI} -size 14 -weight bold -underline 1")

        self.view_button = tkinter.Button(self.prof_window,
                                          text='View Grades',
                                          command=self.view_grade)
        self.view_button.place(relx=0.400, rely=0.736, height=44, width=120)
        self.view_button.configure(background="#bfbfbf")
        self.view_button.configure(font="-family {Segoe UI} -size 14 -weight bold -underline 1")

        self.quit_button = tkinter.Button(self.prof_window,
                                          text='Quit',
                                          command=self.prof_window.destroy)
        self.quit_button.place(relx=0.650, rely=0.736, height=44, width=120)
        self.quit_button.configure(background="#bfbfbf")
        self.quit_button.configure(font="-family {Segoe UI} -size 14 -weight bold -underline 1")

        tkinter.mainloop()

    def view_grade(self):
        self.search_frame = tkinter.Toplevel(self.prof_window)
        self.search_frame.geometry("800x400")
        self.search_frame.title("View Grade")
        self.search_frame.configure(background="#f1d2b6")
        self.view_title_frame = tkinter.Frame(self.search_frame)
        self.view_title_frame.configure(background="#f1d2b6")
        self.view_detials_frame = tkinter.Frame(self.search_frame)
        #self.add_detials_frame.configure(background="#f1d2b6")
        self.view_button_frame = tkinter.Frame(self.search_frame)
        self.view_button_frame.configure(background="#f1d2b6")

        self.view_frame = tkinter.Frame(self.search_frame)
        self.view_frame.configure(background="#f1d2b6")

        # Student-ID
        self.view_student_id = tkinter.StringVar()
        self.form_id(self.view_detials_frame, "Student", self.view_student_id, label_row=0, label_column=0,
                     entry_row=0, entry_column=1, padx=0, pady=15)

        # Label: '/'
        self.divide1_label = tkinter.Label(self.view_detials_frame, text=" OR ", font="-weight bold -size 10")
        self.divide1_label.grid(row=0, column=2, pady=5)

        # Student-Name
        self.view_student_name = tkinter.StringVar()
        self.form_name(self.view_detials_frame, "Student", self.view_student_name, label_row=0, label_col=3,
                       padx=5, entry_row=0, entry_col=4, pady=15)

        # Label: '/'
        self.divide2_label = tkinter.Label(self.view_detials_frame, text=" OR ", font="-weight bold -size 10")
        self.divide2_label.grid(row=0, column=5, pady=5)

        # Course
        self.course_choice_label = tkinter.Label(self.view_detials_frame, text="Course:")
        self.course_choice_label.configure(background="#f1d2b6")
        self.view_course_type_var = tkinter.StringVar()
        self.view_course_type_var.set(self.COURSES[0])
        self.drop_menu = tkinter.OptionMenu(self.view_detials_frame, self.view_course_type_var, *self.COURSES)
        self.course_choice_label.grid(row=0, column=6, pady=5)
        self.drop_menu.grid(row=0, column=7)

        # Buttons : Submit
        self.view_submit_button = tkinter.Button(self.view_button_frame,
                                                 text='Submit',
                                                 command=self.populate_view_grade_data)
        self.quit_button = tkinter.Button(self.view_button_frame,
                                          text='Cancel',
                                          command=self.search_frame.destroy)
        self.view_submit_button.grid(row=1, column=0, padx=15, pady=5, ipadx=10)
        self.quit_button.grid(row=1, column=1, ipadx=10)

        self.view_title_frame.grid(row=0, column=0)
        self.view_detials_frame.grid(row=1, column=0, padx=100)
        self.view_button_frame.grid(row=2, column=0)
        self.view_frame.grid(row=3, column=0)
        self.search_frame.grid()

    def populate_view_grade_data(self):

        self.search_data_frame = tkinter.Frame(self.search_frame)
        self.search_data_frame.configure(background="#f1d2b6")

        query = "SELECT * FROM "+DATABASE_NAME+".student;"
        record = database_connection(query, 'all', 0)

        self.data_id_label = tkinter.Label(self.search_data_frame, text="Student ID", font="-weight bold -size 9")
        self.data_id_label.configure(background="#f1d2b6")
        self.data_name_label = tkinter.Label(self.search_data_frame, text="Student Name", font="-weight bold -size 9")
        self.data_name_label.configure(background="#f1d2b6")
        self.data_course_label = tkinter.Label(self.search_data_frame, text="Student Course", font="-weight bold -size 9")
        self.data_course_label.configure(background="#f1d2b6")
        self.data_grade_label = tkinter.Label(self.search_data_frame, text="Grade", font="-weight bold -size 9")
        self.data_grade_label.configure(background="#f1d2b6")
        self.data_action_label = tkinter.Label(self.search_data_frame, text="Action", font="-weight bold -size 9")
        self.data_action_label.configure(background="#f1d2b6")

        index = 0
        self.student_id = StringVar()
        for row in record:
            self.student_id.set(row[1])
            # Fetch CourseName by Course ID
            course_name = database_connection("select * from "+DATABASE_NAME+".course where course_id=" + str(row[8]),
                                              '1',
                                              0)
            self.data_id = tkinter.Label(self.search_data_frame, text=row[1])
            self.data_id.configure(background="#f1d2b6")
            self.data_name = tkinter.Label(self.search_data_frame, text=row[2])
            self.data_name.configure(background="#f1d2b6")
            self.data_course = tkinter.Label(self.search_data_frame, text=course_name[2])
            self.data_course.configure(background="#f1d2b6")
            self.data_grade = tkinter.Label(self.search_data_frame, text=row[3])
            self.data_grade.configure(background="#f1d2b6")
            self.action_frame = tkinter.Frame(self.search_data_frame)
            self.action_frame.configure(background="#f1d2b6")
            self.update_button = tkinter.Button(self.action_frame,
                                                text='Edit',
                                                command=partial(self.edit_student_grade_Method, self.student_id.get()))
            self.delete_button = tkinter.Button(self.action_frame,
                                                text='Reset Grade',
                                                command=partial(self.reset_student_record, self.student_id.get()))

            self.data_id.grid(row=3 + index, column=0)
            self.data_name.grid(row=3 + index, column=1)
            self.data_course.grid(row=3 + index, column=2)
            self.data_grade.grid(row=3 + index, column=3)
            self.update_button.grid(row=0 + index, column=0, padx=5)
            self.delete_button.grid(row=0 + index, column=1)
            self.action_frame.grid(row=3 + index, column=4)
            index += 1

        self.data_id_label.grid(row=2, column=0)
        self.data_name_label.grid(row=2, column=1)
        self.data_course_label.grid(row=2, column=2)
        self.data_grade_label.grid(row=2, column=3)
        self.data_action_label.grid(row=2, column=4, columnspan=2)
        self.search_data_frame.grid(row=3 + index, column=0)

    def reset_student_record(self, update_student_id):
        values=[update_student_id, 0, '', 0, 0, 0, 0]

        common_query('UPDATE '+DATABASE_NAME+'.student SET grade = "" WHERE student_id='+update_student_id+';')
        self.search_frame.destroy()
        messagebox.showinfo("Success", "Data has been Reset Successfully!")

    def edit_student_grade_Method(self, update_id):

        sql_query_by_id = "select * from "+DATABASE_NAME+".student where student_id=" + update_id + ";"
        record = database_connection(sql_query_by_id, '1', 0)
        course_query = 'select * from '+DATABASE_NAME+'.course where course_id=' + str(record[8])
        course_name_by_course_id = database_connection(course_query, '1', 0)

        self.update_student_id = tkinter.StringVar()
        self.update_student_name = tkinter.StringVar()
        self.update_grade = tkinter.StringVar()
        self.update_student_email = tkinter.StringVar()
        self.update_username = tkinter.StringVar()
        self.update_password = tkinter.StringVar()
        self.update_phone = tkinter.StringVar()
        self.update_course_id = tkinter.StringVar()

        self.update_student_id.set(record[1])
        self.update_student_name.set(record[2])
        self.update_grade.set(record[3])
        self.update_student_email.set(record[4])
        self.update_username.set(record[5])
        self.update_password.set(record[6])
        self.update_phone.set(record[7])
        self.update_course_id.set(record[8])


        self.update_grade_window = tkinter.Toplevel(self.search_frame)
        self.update_grade_window.geometry("300x200")
        self.update_grade_window.title("Update Grade")
        self.update_grade_window.configure(background="#f1d2b6")
        # Student-ID
        self.edit_student_id_label = tkinter.Label(self.update_grade_window, text="Student ID : ",
                                                   font="-family {Lucida Sans} "
                                                        "-size 9 -weight bold")
        self.edit_student_id_label.configure(background="#f1d2b6")
        self.edit_student_id = tkinter.Label(self.update_grade_window, text=record[1])
        self.edit_student_id.configure(background="#f1d2b6")
        self.edit_student_id_label.grid(row=0, column=0, pady=5)
        self.edit_student_id.grid(row=0, column=1)

        # Student-Name
        self.edit_student_name_label = tkinter.Label(self.update_grade_window, text="Student Name :",
                                                     font="-family {Lucida Sans} "
                                                          "-size 9 -weight bold")
        self.edit_student_name_label.configure(background="#f1d2b6")
        self.edit_student_name = tkinter.Label(self.update_grade_window, text=record[2])
        self.edit_student_name.configure(background="#f1d2b6")
        self.edit_student_name_label.grid(row=1, column=0, pady=5)
        self.edit_student_name.grid(row=1, column=1)

        # Student-Course
        self.edit_student_course_choice_label = tkinter.Label(self.update_grade_window, text="Course:")
        self.edit_student_course_choice_label.configure(background="#f1d2b6")
        self.edit_student_course_type_var = tkinter.StringVar()
        if course_name_by_course_id[2] in self.COURSES:
            self.edit_student_course_type_var.set(self.COURSES[self.COURSES.index(course_name_by_course_id[2])])
        self.edit_student_drop_menu = tkinter.OptionMenu(self.update_grade_window, self.edit_student_course_type_var, *self.COURSES)
        self.edit_student_course_choice_label.grid(row=2, column=0, pady=5)
        self.edit_student_drop_menu.grid(row=2, column=1)

        # Student Grade
        self.edit_student_grade = tkinter.StringVar()
        self.edit_student_grade.set(record[3])

        self.edit_studentgrade_label = tkinter.Label(self.update_grade_window, text="Student Grade : ")
        self.edit_studentgrade_label.configure(background="#f1d2b6")
        self.edit_studentgrade_entry = tkinter.Entry(self.update_grade_window, width=6, font="-family {Lucida Sans} "
                                                                                 "-size 9 -weight bold",
                                         textvariable=self.edit_student_grade)

        self.edit_studentgrade_label.grid(row=3, column=0, pady=12)
        self.edit_studentgrade_entry.grid(row=3, column=1)

        # Buttons
        self.update_grade_button = tkinter.Button(self.update_grade_window,
                                               text='Update', command=self.update_student_data)
        self.quit_button = tkinter.Button(self.update_grade_window,
                                          text='Cancel',
                                          command=self.update_grade_window.destroy)
        self.update_grade_button.grid(row=5, column=0, padx=15, pady=15, ipadx=10)
        self.quit_button.grid(row=5, column=1, ipadx=10)

        self.update_grade_window.grid()

    def update_student_data(self):
        values=[]
        values.append(self.update_student_id.get())
        values.append(self.update_student_name.get())
        values.append(self.edit_student_grade.get())
        values.append(self.update_student_email.get())
        values.append(self.update_username.get())
        values.append(self.update_password.get())
        values.append(self.update_phone.get())
        course_id_record = database_connection(
            "select course_id from "+DATABASE_NAME+".course where course_name like '" + self.edit_student_course_type_var.get() + "';",
            '1', 0)
        values.append(course_id_record[0])
        update_query('student', values)
        self.update_grade_window.destroy()
        self.search_frame.destroy()
        messagebox.showinfo("Update Data", "Data Updated Sucessfully!")

    def add_grade(self):
        self.add_form_frame = tkinter.Toplevel(self.prof_window)
        self.add_form_frame.geometry("500x400")
        self.add_form_frame.title("Add Grade")
        self.add_form_frame.configure(background="#f1d2b6")

        self.add_title_frame = tkinter.Frame(self.add_form_frame)
        self.add_title_frame.configure(background="#f1d2b6")
        self.add_detials_frame = tkinter.Frame(self.add_form_frame)
        self.add_detials_frame.configure(background="#f1d2b6")
        self.add_button_frame = tkinter.Frame(self.add_form_frame)
        self.add_button_frame.configure(background="#f1d2b6")
        self.add_title_label = tkinter.Label(self.add_title_frame, text="~ ~ Add Grades ~ ~",
                                             font="-weight bold -size 10")
        self.add_title_label.configure(background="#f1d2b6")
        self.add_title_label.grid(row=0, column=0, columnspan=2, pady=15)

        # Student ID
        self.add_student_id = tkinter.StringVar()
        self.form_id(self.add_detials_frame, "Student", self.add_student_id, label_row=1, label_column=0,
                     entry_row=1, entry_column=1, padx=0, pady=15)

        self.or_1_label = tkinter.Label(self.add_detials_frame, text="~ ~ ~ ~ OR ~ ~ ~ ~",
                                        font="-weight bold -size 10")

        self.or_1_label.grid(row=2, column=0, columnspan=2)

        # Student Name and Course ID
        self.add_student_name = tkinter.StringVar()
        self.form_name(self.add_detials_frame, "Student", self.add_student_name, label_row=3, label_col=0,
                       padx=5, entry_row=3, entry_col=1, pady=15)

        self.add_course_id = tkinter.StringVar()
        self.form_id(self.add_detials_frame, "Course", self.add_course_id, label_row=4, label_column=0,
                     entry_row=4, entry_column=1, padx=0, pady=5)

        self.or_2_label = tkinter.Label(self.add_detials_frame, text="~ ~ ~ ~ OR ~ ~ ~ ~",
                                        font="-weight bold -size 10")
        self.or_2_label.grid(row=5, column=0, columnspan=2, pady=5)

        # Course Type
        self.course_choice_label = tkinter.Label(self.add_detials_frame, text="Course:")
        self.course_choice_label.configure(background="#f1d2b6")
        self.course_type_var = tkinter.StringVar()
        self.course_type_var.set(self.COURSES[0])
        self.drop_menu = tkinter.OptionMenu(self.add_detials_frame, self.course_type_var, *self.COURSES)
        self.course_choice_label.grid(row=6, column=0, pady=5)
        self.drop_menu.grid(row=6, column=1)

        # Grades
        self.grade = tkinter.StringVar()
        self.grade_label = tkinter.Label(self.add_detials_frame, text="Student Grade : ")
        self.grade_label.configure(background="#f1d2b6")
        self.grade_entry = tkinter.Entry(self.add_detials_frame, width=6, textvariable=self.grade)
        self.grade_label.grid(row=7, column=0, pady=12)
        self.grade_entry.grid(row=7, column=1)

        # Buttons : Submit
        self.add_grade_button = tkinter.Button(self.add_button_frame,
                                               text='Add')
        self.quit_button = tkinter.Button(self.add_button_frame,
                                          text='Cancel',
                                          command=self.add_form_frame.destroy)
        self.add_grade_button.grid(row=8, column=0, padx=15, pady=15, ipadx=10)
        self.quit_button.grid(row=8, column=1, ipadx=10)

        self.add_title_frame.grid(row=0, column=0)
        self.add_detials_frame.grid(row=1, column=0, padx=100)
        self.add_button_frame.grid(row=2, column=0)

        self.add_form_frame.grid()

    def form_id(self, frame, text, variable, label_row, label_column, entry_row, entry_column, padx, pady):
        self.student_id_label = tkinter.Label(frame, text=text + " ID : ")
        self.student_id_label.configure(background="#f1d2b6")
        self.student_id_entry = tkinter.Entry(frame, width=10, font=("Calibri", 12),
                                              textvariable=variable)
        self.student_id_label.grid(row=label_row, column=label_column, pady=pady)
        self.student_id_entry.grid(row=entry_row, column=entry_column)

    def form_name(self, frame, text, variable, label_row, label_col, padx, entry_row, entry_col, pady):
        self.name_label = tkinter.Label(frame, text=text + " Name : ")
        self.name_label.configure(background="#f1d2b6")
        self.name_entry = tkinter.Entry(frame, width=20, font=("Calibri", 12),
                                        textvariable=variable)
        self.name_label.grid(row=label_row, column=label_col, padx=padx, pady=pady)
        self.name_entry.grid(row=entry_row, column=entry_col)

# prof = ProfessorHome()
# prof.initializing_professor()