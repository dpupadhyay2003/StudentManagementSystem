import tkinter
from tkinter import messagebox
from database import *
from functools import partial


class Admin:
    DEPARTMENT = ['Student', 'Professor', 'Course']
    COURSES = ['--Select--']

    def __init__(self):     # Loading All Courses from Database
        course_record = database_connection('SELECT * FROM '+DATABASE_NAME+'.course;', 'all', 0)
        if len(course_record) != 0:
            for row in course_record:
                self.COURSES.append(row[2])

    def initializing_admin(self):
        self.admin_window = tkinter.Tk()
        self.admin_window.geometry("500x500")
        self.admin_window.title("Administration")
        self.admin_window.configure(background="#c9af98")

        self.acctype_frame = tkinter.Frame(self.admin_window)
        self.choice_frame = tkinter.Frame(self.admin_window)
        self.button_frame = tkinter.Frame(self.admin_window)

        self.select_label = tkinter.Label(self.admin_window)
        self.select_label.place(relx=0.035, rely=0.051, height=41, width=484)
        self.select_label.configure(background="#c9af98")
        self.select_label.configure(font="-family {Lucida Sans} -size 15 -weight"
                                         " bold")
        self.select_label.configure(text='''~ ~ Select Action Taken On Object ~ ~''')

        self.acc_type_var = tkinter.StringVar(self.admin_window)
        self.acc_type_var.set(self.DEPARTMENT[0])

        self.drop_menu = tkinter.OptionMenu(self.admin_window, self.acc_type_var, *self.DEPARTMENT,
                                            command=self.drop_menu_change)
        self.drop_menu.place(relx=0.335, rely=0.251, height=41, width=184)
        self.drop_menu.configure(background="#bfbfbf")
        self.drop_menu.configure(font="-family {Lucida Sans} -size 14 -weight bold")

        self.selection = tkinter.IntVar()
        self.selection.set(1)
        self.add_label = tkinter.Radiobutton(self.admin_window,
                                             text='Add',
                                             variable=self.selection,
                                             value=1)
        self.add_label.place(relx=0.155, rely=0.451, height=41, width=175)
        self.add_label.configure(background="#c9af98")
        self.add_label.configure(font="-family {Lucida Sans} -size 15 -weight"
                                      " bold")

        self.search_label = tkinter.Radiobutton(self.admin_window,
                                                text='Search',
                                                variable=self.selection,
                                                value=2)
        self.search_label.place(relx=0.465, rely=0.451, height=41, width=200)
        self.search_label.configure(background="#c9af98")
        self.search_label.configure(font="-family {Lucida Sans} -size 15 -weight"
                                         " bold")

        # self.add_label.grid(row=1, column=0)
        # self.search_label.grid(row=1, column=1)

        # Buttons : Submit
        self.submit_button = tkinter.Button(self.admin_window,
                                            text='Submit',
                                            command=self.submit_request)
        self.submit_button.place(relx=0.250, rely=0.636, height=44, width=111)
        self.submit_button.configure(background="#bfbfbf")
        self.submit_button.configure(font="-family {Segoe UI} -size 14 -weight bold -underline 1")

        self.quit_button = tkinter.Button(self.admin_window,
                                          text='Quit',
                                          command=self.admin_window.destroy)
        self.quit_button.place(relx=0.550, rely=0.636, height=44, width=111)
        self.quit_button.configure(background="#bfbfbf")
        self.quit_button.configure(font="-family {Segoe UI} -size 14 -weight bold -underline 1")

        tkinter.mainloop()

    def drop_menu_change(self, select):
        # print(self.acc_type_var.get())
        pass

    def submit_request(self):
        # print("# # Details # #")
        # print("selection Type : ", self.selection.get())
        if self.selection.get() == 1:
            # print("Choice Selected : Add")
            self.add_form(self.acc_type_var.get())
        elif self.selection.get() == 2:
            # print("Choice Selected : Search")
            self.search_form(self.acc_type_var.get())
        else:
            print("Invalid Option!")

    def search_form(self, acc_type):
        self.frame_flag = False
        self.search_form_frame = tkinter.Toplevel(self.admin_window)
        self.search_form_frame.geometry("570x220")
        self.search_form_frame.configure(background="#f1d2b6")
        self.search_form_frame.title("Search " + acc_type + " Form")

        self.searching_form_frame = tkinter.Frame(self.search_form_frame)
        self.searching_form_frame.configure(background="#f1d2b6")
        # ID
        self.student_id = tkinter.StringVar()
        self.prof_id = tkinter.StringVar()
        self.course_id = tkinter.StringVar()
        if acc_type == 'Student':
            self.form_id(self.searching_form_frame, "Student", self.student_id, 0, 0, 0, 1, 0, 15)
        elif acc_type == 'Professor':
            self.form_id(self.searching_form_frame, "Professor", self.prof_id, 0, 0, 0, 1, 0, 15)
        elif acc_type == 'Course':
            self.form_id(self.searching_form_frame, "Course", self.course_id, 0, 0, 0, 1, 0, 15)
        else:
            pass

        self.or_label = tkinter.Label(self.searching_form_frame, text=" -- or -- ")
        self.or_label.grid(row=0, column=2, padx=15)

        # Name
        self.student_name = tkinter.StringVar()
        self.prof_name = tkinter.StringVar()
        self.course_name = tkinter.StringVar()
        if acc_type == 'Student':
            self.form_name(self.searching_form_frame, "Student", self.student_name, 0, 3, 0, 0, 4)
        elif acc_type == 'Professor':
            self.form_name(self.searching_form_frame, "Professor", self.prof_name, 0, 3, 0, 0, 4)
        elif acc_type == 'Course':
            self.form_name(self.searching_form_frame, "Course", self.course_name, 0, 3, 0, 0, 4)
        else:
            pass

        # Buttons : Submit
        self.search_button = tkinter.Button(self.searching_form_frame,
                                            text='Search', command=self.submit_search_form)
        self.quit_button = tkinter.Button(self.searching_form_frame,
                                          text='Quit',
                                          command=self.search_form_frame.destroy)
        self.search_button.grid(row=1, column=0, padx=10, pady=15, ipadx=10)
        self.quit_button.grid(row=1, column=1, ipadx=10)

        self.searching_form_frame.grid()

    def add_form(self, acc_type):
        # Make Form to Add.
        # Student ID, Student Name, Grade, Username, Password, email, phoneNo
        self.add_form_frame = tkinter.Toplevel(self.admin_window)
        self.add_form_frame.geometry("570x220")
        self.add_form_frame.configure(background="#f1d2b6")
        self.add_form_frame.title("Add " + acc_type + " Form")
        # ID
        self.student_id = tkinter.StringVar()
        self.prof_id = tkinter.StringVar()
        self.course_id = tkinter.StringVar()
        if acc_type == 'Student':
            self.form_id(self.add_form_frame, "Student", self.student_id, 4, 0, 4, 1, 0, 15)
        elif acc_type == 'Professor':
            self.form_id(self.add_form_frame, "Professor", self.prof_id, 4, 0, 4, 1, 0, 15)
        elif acc_type == 'Course':
            self.form_id(self.add_form_frame, "Course", self.course_id, 4, 0, 4, 1, 0, 15)
        else:
            pass

        # Name
        self.student_name = tkinter.StringVar()
        self.prof_name = tkinter.StringVar()
        self.course_name = tkinter.StringVar()
        if acc_type == 'Student':
            self.form_name(self.add_form_frame, "Student", self.student_name, 4, 2, 15, 4, 3)
        elif acc_type == 'Professor':
            self.form_name(self.add_form_frame, "Professor", self.prof_name, 4, 2, 15, 4, 3)
        elif acc_type == 'Course':
            self.form_name(self.add_form_frame, "Course", self.course_name, 4, 2, 15, 4, 3)
        else:
            pass

        # Grade
        self.grade = tkinter.StringVar()
        if acc_type == 'Student':
            self.grade_label = tkinter.Label(self.add_form_frame, text="Student Grade : ")
            self.grade_entry = tkinter.Entry(self.add_form_frame, width=6, font=("Calibri", 12),
                                             textvariable=self.grade)
            self.grade_label.configure(background="#f1d2b6")
            self.grade_label.grid(row=6, column=0, pady=12)
            self.grade_entry.grid(row=6, column=1)
        else:
            pass

        # Student Email
        self.student_email = tkinter.StringVar()
        self.prof_email = tkinter.StringVar()
        if acc_type == 'Student':
            self.form_email(self.add_form_frame, "Student", self.student_email, 6, 2, 12, 6, 3)
        elif acc_type == 'Professor':
            self.form_email(self.add_form_frame, "Professor", self.prof_email, 6, 0, 12, 6, 1)
        else:
            pass

        # Username and Password
        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()
        if acc_type == 'Student' or acc_type == 'Professor':
            self.form_username(self.add_form_frame, self.username, 7, 0, 7, 1)
            self.form_password(self.add_form_frame, self.password, 7, 2, 12, 7, 3)
        else:
            pass

        # Phone Number
        self.phone = tkinter.StringVar()
        if acc_type == 'Student' or acc_type == 'Professor':
            self.phone_label = tkinter.Label(self.add_form_frame, text="Phone No. : ")
            self.phone_entry = tkinter.Entry(self.add_form_frame, width=15, font=("Calibri", 12),
                                             textvariable=self.phone)
            self.phone_label.configure(background="#f1d2b6")
            self.phone_label.grid(row=8, column=0)
            self.phone_entry.grid(row=8, column=1)
        else:
            pass

        # Course Dropdown
        if acc_type == 'Student' or acc_type == 'Professor':
            self.course_drop_label = tkinter.Label(self.add_form_frame, text="Course : ")
            self.course_var = tkinter.StringVar(self.add_form_frame)
            self.course_var.set(self.COURSES[0])

            self.course_drop_menu = tkinter.OptionMenu(self.add_form_frame, self.course_var, *self.COURSES)
            self.course_drop_label.grid(row=8, column=2)
            self.course_drop_menu.grid(row=8, column=3)

        # Course Fees
        self.course_fees = tkinter.StringVar()
        if acc_type == 'Course':
            self.fees_label = tkinter.Label(self.add_form_frame, text="Course Fees : ")
            self.fees_entry = tkinter.Entry(self.add_form_frame, width=15, font=("Calibri", 12),
                                            textvariable=self.course_fees)
            self.fees_label.configure(background="#f1d2b6")
            self.fees_label.grid(row=5, column=0)
            self.fees_entry.grid(row=5, column=1)

        # Buttons : Submit
        self.submit_button = tkinter.Button(self.add_form_frame,
                                            text='Add', command=self.submit_add_form)
        self.quit_button = tkinter.Button(self.add_form_frame,
                                          text='Quit',
                                          command=self.add_form_frame.destroy)
        self.submit_button.grid(row=9, column=0, padx=10, pady=15, ipadx=10)
        self.quit_button.grid(row=9, column=1, ipadx=10)

        self.add_form_frame.grid()

    def get_course_id(self, course_name):
        course_record = database_connection('SELECT * FROM '+DATABASE_NAME+'.course where course_name like "'+
                                            course_name + '";', 'all', 0)
        for row in course_record:
            print(row[2] == course_name)
            if row[2] == course_name:
                return row[1]
        return 1

    def submit_add_form(self):
        values = []
        # print("acc_type: ", self.acc_type_var.get())
        if self.acc_type_var.get() == 'Student':
            if 100 > int(self.grade.get()) > 0:
                values.append(str(self.student_id.get()))
                values.append(str(self.student_name.get()))
                values.append(str(self.grade.get()))
                values.append(str(self.student_email.get()))
                values.append(str(self.username.get()))
                values.append(str(self.password.get()))
                values.append(str(self.phone.get()))
                values.append(str(self.get_course_id(self.course_var.get())))
                if insert_Query('student', values):
                    self.add_form_frame.destroy()
                    messagebox.showinfo("Success", "Data Inserted Successfully!")
                else:
                    messagebox.showerror("Error: 500", "Failed To Insert Data!")
            else:
                messagebox.showerror("Error", "InValid Grade!")

        elif self.acc_type_var.get() == 'Professor':
            values.clear()
            values.append(self.prof_id.get())
            values.append(self.prof_name.get())
            values.append(self.prof_email.get())
            values.append(self.username.get())
            values.append(self.password.get())
            values.append(self.phone.get())
            values.append(str(self.get_course_id(self.course_var.get())))

            if insert_Query('professor', values):
                self.add_form_frame.destroy()
                messagebox.showinfo("Success", "Data Inserted Successfully!")
            else:
                messagebox.showerror("Error: 500", "Failed To Insert Data!")

        elif self.acc_type_var.get() == 'Course':
            values.clear()
            values.append(self.course_id.get())
            values.append(self.course_name.get())
            values.append(self.course_fees.get())

            if insert_Query('course', values):
                self.add_form_frame.destroy()
                messagebox.showinfo("Success", "Data Inserted Successfully!")
            else:
                messagebox.showerror("Error: 500", "Failed To Insert Data!")
        else:
            pass

    def student_populate_table(self):
        self.frame_flag = True
        self.search_data_frame = tkinter.Frame(self.search_form_frame)
        self.search_data_frame.configure(background="#f1d2b6")

        self.update_student_id = tkinter.StringVar()
        self.update_student_name = tkinter.StringVar()
        self.update_grade = tkinter.StringVar()
        self.update_student_email = tkinter.StringVar()
        self.update_username = tkinter.StringVar()
        self.update_password = tkinter.StringVar()
        self.update_phone = tkinter.StringVar()
        self.update_course_id = tkinter.StringVar()

        self.data_id_label = tkinter.Label(self.search_data_frame, text="Student ID")
        self.data_name_label = tkinter.Label(self.search_data_frame, text="Student Name")
        self.data_course_label = tkinter.Label(self.search_data_frame, text="Student Course")
        self.data_grade_label = tkinter.Label(self.search_data_frame, text="Grade")
        self.data_action_label = tkinter.Label(self.search_data_frame, text="Action")

        # Get All data as per id or Name
        query = ""
        if self.student_id.get():
            query = "select * from "+DATABASE_NAME+".student where student_id=" + self.student_id.get()
        elif self.student_name.get():
            query = "select * from "+DATABASE_NAME+".student where student_name like '%" + self.student_name.get()+"%'"
        else:
            query = "select * from "+DATABASE_NAME+".student"

        record = database_connection(query, 'all', 0)
        index = 0
        for row in record:
            self.update_student_id.set(row[1])
            self.update_student_name.set(row[2])
            self.update_grade.set(row[3])
            self.update_student_email.set(row[4])
            self.update_username.set(row[5])
            self.update_password.set(row[6])
            self.update_phone.set(row[7])
            self.update_course_id.set(row[8])

            # Fetch CourseName by Course ID
            course_name = database_connection("select * from "+DATABASE_NAME+".course where course_id="+str(row[8]), '1', 0)

            self.data_id = tkinter.Label(self.search_data_frame, text=self.update_student_id.get())
            self.data_name = tkinter.Label(self.search_data_frame, text=self.update_student_name.get())
            self.data_course = tkinter.Label(self.search_data_frame, text=course_name[2])
            self.data_grade = tkinter.Label(self.search_data_frame, text=self.update_grade.get())
            self.action_frame = tkinter.Frame(self.search_data_frame)

            self.update_button = tkinter.Button(self.action_frame,
                                                text='Update', command=partial(self.update_data, self.update_student_id.get()))

            self.delete_button = tkinter.Button(self.action_frame,
                                                text='Delete', command=partial(self.delete_student_by_id, self.update_student_id.get()))

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
        self.search_data_frame.grid(row=index + 1, column=0)

    def professor_populate_table(self):
        self.frame_flag = True
        self.search_data_frame = tkinter.Frame(self.search_form_frame)
        self.search_data_frame.configure(background="#f1d2b6")

        self.update_prof_id = tkinter.StringVar()
        self.update_prof_name = tkinter.StringVar()
        self.update_prof_email = tkinter.StringVar()
        self.update_username = tkinter.StringVar()
        self.update_password = tkinter.StringVar()
        self.update_phone = tkinter.StringVar()
        self.update_course_id = tkinter.StringVar()

        self.data_id_label = tkinter.Label(self.search_data_frame, text="Professor ID")
        self.data_name_label = tkinter.Label(self.search_data_frame, text="Professor Name")
        self.data_course_label = tkinter.Label(self.search_data_frame, text="Course")
        self.data_action_label = tkinter.Label(self.search_data_frame, text="Action")

        # Get All data as per id or Name
        query = ""
        if self.prof_id.get():
            query = "select * from "+DATABASE_NAME+".professor where student_id=" + self.prof_id.get()
        elif self.prof_name.get():
            query = "select * from "+DATABASE_NAME+".professor where student_name like '%" + self.prof_name.get() + "%'"
        else:
            query = "select * from "+DATABASE_NAME+".professor"

        record = database_connection(query, 'all', 0)
        index = 0
        for row in record:
            self.update_prof_id.set(row[1])
            self.update_prof_name.set(row[2])
            self.update_prof_email.set(row[3])
            self.update_username.set(row[4])
            self.update_password.set(row[5])
            self.update_phone.set(row[6])
            self.update_course_id.set(row[7])

            # Fetch CourseName by Course ID
            course_name = database_connection("select * from "+DATABASE_NAME+".course where course_id=" + str(row[7]),
                                              '1', 0)

            self.data_id = tkinter.Label(self.search_data_frame, text=self.update_prof_id.get())
            self.data_name = tkinter.Label(self.search_data_frame, text=self.update_prof_name.get())
            self.data_course = tkinter.Label(self.search_data_frame, text=course_name[2])
            self.action_frame = tkinter.Frame(self.search_data_frame)

            self.update_button = tkinter.Button(self.action_frame,
                                                text='Update', command=partial(self.update_data, self.update_prof_id.get()))

            self.delete_button = tkinter.Button(self.action_frame,
                                                text='Delete', command=partial(self.delete_professor_by_id, self.update_prof_id.get()))
            self.data_id.grid(row=3 + index, column=0)
            self.data_name.grid(row=3 + index, column=1)
            self.data_course.grid(row=3 + index, column=2)
            self.update_button.grid(row=0 + index, column=0, padx=5)
            self.delete_button.grid(row=0 + index, column=1)
            self.action_frame.grid(row=3 + index, column=3)
            index += 1

        self.data_id_label.grid(row=2, column=0)
        self.data_name_label.grid(row=2, column=1)
        self.data_course_label.grid(row=2, column=2)
        self.data_action_label.grid(row=2, column=3)
        self.search_data_frame.grid(row=index + 1, column=0)

    def course_populate_table(self):
        self.frame_flag = True
        self.search_data_frame = tkinter.Frame(self.search_form_frame)
        self.search_data_frame.configure(background="#f1d2b6")

        self.update_course_id = tkinter.StringVar()
        self.update_course_name = tkinter.StringVar()
        self.update_course_fees = tkinter.StringVar()

        self.data_id_label = tkinter.Label(self.search_data_frame, text="Course ID")
        self.data_name_label = tkinter.Label(self.search_data_frame, text="Course Name")
        self.data_action_label = tkinter.Label(self.search_data_frame, text="Action")

        # Get All data as per id or Name
        query = ""
        if self.course_id.get():
            query = "select * from "+DATABASE_NAME+".course where course_id=" + self.course_id.get()
        elif self.course_name.get():
            query = "select * from "+DATABASE_NAME+".course where course_name like '%" + self.course_name.get() + "%'"
        else:
            query = "select * from "+DATABASE_NAME+".course"

        record = database_connection(query, 'all', 0)
        index = 0
        for row in record:
            self.update_course_id.set(row[1])
            self.update_course_name.set(row[2])
            self.update_course_fees.set(row[3])

            self.data_id = tkinter.Label(self.search_data_frame, text=self.update_course_id.get())
            self.data_name = tkinter.Label(self.search_data_frame, text=self.update_course_name.get())
            self.action_frame = tkinter.Frame(self.search_data_frame)

            self.update_button = tkinter.Button(self.action_frame,
                                                text='Update', command=partial(self.update_data, self.update_course_id.get()))
            self.delete_button = tkinter.Button(self.action_frame,
                                                text='Delete', command=partial(self.delete_course_by_id, self.update_course_id.get()))
            self.data_id.grid(row=3 + index, column=0)
            self.data_name.grid(row=3 + index, column=1)
            self.update_button.grid(row=0 + index, column=0, padx=5)
            self.delete_button.grid(row=0 + index, column=1)
            self.action_frame.grid(row=3 + index, column=2)
            index += 1

        self.data_id_label.grid(row=2, column=0)
        self.data_name_label.grid(row=2, column=1)
        self.data_action_label.grid(row=2, column=2)
        self.search_data_frame.grid(row=index + 1, column=0)

    def delete_student_by_id(self, delete_student_id):
        if delete_query('student', str(delete_student_id)):
            self.search_form_frame.destroy()
            messagebox.showinfo("Success", "Data Deleted Successfully!")
        else:
            messagebox.showerror("Error: 500", "Failed To Delete Data!")

    def delete_professor_by_id(self, delete_professor_id):
        if delete_query('professor', str(delete_professor_id)):
            self.search_form_frame.destroy()
            messagebox.showinfo("Success", "Data Deleted Successfully!")
        else:
            messagebox.showerror("Error: 500", "Failed To Delete Data!")

    def delete_course_by_id(self, delete_course_id):
        if delete_query('course', str(delete_course_id)):
            self.search_form_frame.destroy()
            messagebox.showinfo("Success", "Data Deleted Successfully!")
        else:
            messagebox.showerror("Error: 500", "Failed To Delete Data!")

    def submit_search_form(self):
        if self.acc_type_var.get() == "Professor":
            if not self.frame_flag:
                self.professor_populate_table()
            else:
                self.search_data_frame.destroy()
                self.professor_populate_table()

        elif self.acc_type_var.get() == "Student":
            if not self.frame_flag:
                self.student_populate_table()
            else:
                self.search_data_frame.destroy()
                self.student_populate_table()

        elif self.acc_type_var.get() == "Course":
            if not self.frame_flag:
                self.course_populate_table()
            else:
                self.search_data_frame.destroy()
                self.course_populate_table()
        else:
            pass

    def update_data(self, update_id):
        acc_type = self.acc_type_var.get()
        self.update_window = tkinter.Toplevel(self.search_form_frame)
        self.update_window.geometry("570x220")
        self.update_window.title("Update Data")

        sql_query_by_id = ""
        if acc_type == 'Student':
            sql_query_by_id = "select * from "+DATABASE_NAME+".student where student_id=" + update_id + ";"
        elif acc_type == 'Professor':
            sql_query_by_id = "select * from "+DATABASE_NAME+".professor where prof_id=" + update_id + ";"
        elif acc_type == 'Course':
            sql_query_by_id = "select * from "+DATABASE_NAME+".course where course_id=" + update_id + ";"
        else:
            pass

        record = database_connection(sql_query_by_id, '1', 0)
        course_query = ""
        if acc_type == 'Student':
            course_query = 'select * from '+DATABASE_NAME+'.course where course_id=' + str(record[8])
        elif acc_type == 'Professor':
            course_query = 'select * from '+DATABASE_NAME+'.course where course_id=' + str(record[7])
        else:
            pass
        course_name_by_course_id = database_connection(course_query, '1', 0)

        if acc_type == 'Student':
            self.update_student_id.set(record[1])
            self.update_student_name.set(record[2])
            self.update_grade.set(record[3])
            self.update_student_email.set(record[4])
            self.update_username.set(record[5])
            self.update_password.set(record[6])
            self.update_phone.set(record[7])
            self.update_course_id.set(record[8])
            # update_query('student', values)
        elif acc_type == 'Professor':
            self.update_prof_id.set(record[1])
            self.update_prof_name.set(record[2])
            self.update_prof_email.set(record[3])
            self.update_username.set(record[4])
            self.update_password.set(record[5])
            self.update_phone.set(record[6])
            self.update_course_id.set(record[7])
        elif acc_type == 'Course':
            self.update_course_id.set(record[1])
            self.update_course_name.set(record[2])
            self.update_course_fees.set(record[3])
        else:
            pass

        # ID
        if acc_type == 'Student':
            self.form_id(self.update_window, "Student", self.update_student_id, 4, 0, 4, 1, 0, 15)
        elif acc_type == 'Professor':
            self.form_id(self.update_window, "Professor", self.update_prof_id, 4, 0, 4, 1, 0, 15)
        elif acc_type == 'Course':
            self.form_id(self.update_window, "Course", self.update_course_id, 4, 0, 4, 1, 0, 15)
        else:
            pass

        # Name
        if acc_type == 'Student':
            self.form_name(self.update_window, "Student", self.update_student_name, 4, 2, 15, 4, 3)
        elif acc_type == 'Professor':
            self.form_name(self.update_window, "Professor", self.update_prof_name, 4, 2, 15, 4, 3)
        elif acc_type == 'Course':
            self.form_name(self.update_window, "Course", self.update_course_name, 4, 2, 15, 4, 3)
        else:
            pass

        # Grade
        if acc_type == 'Student':
            self.grade_label = tkinter.Label(self.update_window, text="Student Grade : ")
            self.grade_entry = tkinter.Entry(self.update_window, width=6, font=("Calibri", 12),
                                             textvariable=self.update_grade)
            self.grade_label.grid(row=6, column=0, pady=12)
            self.grade_entry.grid(row=6, column=1)
        else:
            pass

        # Student Email
        if acc_type == 'Student':
            self.form_email(self.update_window, "Student", self.update_student_email, 6, 2, 12, 6, 3)
        elif acc_type == 'Professor':
            self.form_email(self.update_window, "Professor", self.update_prof_email, 6, 0, 12, 6, 1)
        else:
            pass

        # Username and Password
        if acc_type == 'Student' or acc_type == 'Professor':
            self.form_username(self.update_window, self.update_username, 7, 0, 7, 1)
            self.form_password(self.update_window, self.update_password, 7, 2, 12, 7, 3)
        else:
            pass

        # Phone Number
        if acc_type == 'Student' or acc_type == 'Professor':
            self.phone_label = tkinter.Label(self.update_window, text="Phone No. : ")
            self.phone_entry = tkinter.Entry(self.update_window, width=15, font=("Calibri", 12),
                                             textvariable=self.update_phone)
            self.phone_label.grid(row=8, column=0)
            self.phone_entry.grid(row=8, column=1)
        else:
            pass

        # Course Fees
        if acc_type == 'Course':
            self.fees_label = tkinter.Label(self.update_window, text="Course Fees : $")
            self.fees_entry = tkinter.Entry(self.update_window, width=15, font=("Calibri", 12),
                                            textvariable=self.update_course_fees)
            self.fees_label.grid(row=5, column=0)
            self.fees_entry.grid(row=5, column=1)

        # Course Drop down
        if acc_type == "Student" or acc_type == "Professor":
            self.course_drop_label = tkinter.Label(self.update_window, text="Course : ")
            self.update_course_var = tkinter.StringVar(self.update_window)
            if course_name_by_course_id[2] in self.COURSES:
                self.update_course_var.set(self.COURSES[self.COURSES.index(course_name_by_course_id[2])])
            self.course_drop_menu = tkinter.OptionMenu(self.update_window, self.update_course_var, *self.COURSES)
            self.course_drop_label.grid(row=8, column=2)
            self.course_drop_menu.grid(row=8, column=3)


        # Buttons : Submit
        self.update_button = tkinter.Button(self.update_window,
                                            text='Update', command=self.submit_update_form)
        self.quit_button = tkinter.Button(self.update_window,
                                          text='Quit',
                                          command=self.update_window.destroy)
        self.update_button.grid(row=9, column=0, padx=10, pady=15, ipadx=10)
        self.quit_button.grid(row=9, column=1, ipadx=10)

        self.update_window.grid()

    def submit_update_form(self):
        values = []
        print("Acc Type: ", self.acc_type_var.get())
        if self.acc_type_var.get() == 'Student':
            if 100 > int(self.update_grade.get()) > 0:
                values.append(self.update_student_id.get())
                values.append(self.update_student_name.get())
                values.append(self.update_grade.get())
                values.append(self.update_student_email.get())
                values.append(self.update_username.get())
                values.append(self.update_password.get())
                values.append(self.update_phone.get())
                course_id_record = database_connection(
                    "select course_id from " + DATABASE_NAME + ".course where course_name like '" + self.update_course_var.get() + "';",
                    '1', 0)
                values.append(course_id_record[0])
                update_query('student', values)
            else:
                messagebox.showerror("Error", "InValid Grade!")
        elif self.acc_type_var.get() == 'Professor':
            values.append(self.update_prof_id.get())
            values.append(self.update_prof_name.get())
            values.append(self.update_prof_email.get())
            values.append(self.update_username.get())
            values.append(self.update_password.get())
            values.append(self.update_phone.get())
            course_id_record = database_connection(
                "select course_id from "+DATABASE_NAME+".course where course_name like '" + self.update_course_var.get() + "';",
                '1', 0)
            values.append(course_id_record[0])
            update_query('professor', values)
        elif self.acc_type_var.get() == 'Course':
            values.append(self.update_course_id.get())
            values.append(self.update_course_name.get())
            values.append(self.update_course_fees.get())
            update_query('course', values)

        else:
            pass
        self.update_window.destroy()
        self.search_form_frame.destroy()
        messagebox.showinfo("Update Data", "Data Updated Sucessfully!")

    def form_id(self, frame, text, variable, label_row, label_column, entry_row, entry_column, padx, pady):
        self.student_id_label = tkinter.Label(frame, text=text + " ID : ")
        self.student_id_entry = tkinter.Entry(frame, width=10, font=("Calibri", 12),
                                              textvariable=variable)
        self.student_id_label.configure(background="#f1d2b6")
        self.student_id_label.grid(row=label_row, column=label_column, pady=pady)
        self.student_id_entry.grid(row=entry_row, column=entry_column)

    def form_name(self, frame, text, variable, label_row, label_col, padx, entry_row, entry_col):
        self.name_label = tkinter.Label(frame, text=text + " Name : ")
        self.name_entry = tkinter.Entry(frame, width=20, font=("Calibri", 12),
                                        textvariable=variable)
        self.name_label.configure(background="#f1d2b6")
        self.name_label.grid(row=label_row, column=label_col, padx=padx)
        self.name_entry.grid(row=entry_row, column=entry_col)

    def form_email(self, frame, text, variable, label_row, label_col, pady, entry_row, entry_col):
        self.email_label = tkinter.Label(frame, text=text + " Email : ")
        self.email_entry = tkinter.Entry(frame, width=20, font=("Calibri", 12),
                                         textvariable=variable)
        self.email_label.configure(background="#f1d2b6")
        self.email_label.grid(row=label_row, column=label_col, pady=pady)
        self.email_entry.grid(row=entry_row, column=entry_col)

    def form_username(self, frame, variable, label_row, label_col, entry_row, entry_col):
        self.username_label = tkinter.Label(frame, text="Username : ")
        self.username_entry = tkinter.Entry(frame, width=15, font=("Calibri", 12),
                                            textvariable=variable)
        self.username_label.configure(background="#f1d2b6")
        self.username_label.grid(row=label_row, column=label_col)
        self.username_entry.grid(row=entry_row, column=entry_col)

    def form_password(self, frame, variable, label_row, label_col, pady, entry_row, entry_col):
        self.password_label = tkinter.Label(frame, text="Password : ")
        self.password_entry = tkinter.Entry(frame, width=15, font=("Calibri", 12),
                                            textvariable=variable)
        self.password_label.configure(background="#f1d2b6")
        self.password_label.grid(row=label_row, column=label_col, pady=pady)
        self.password_entry.grid(row=entry_row, column=entry_col)


# admin = Admin()
# admin.initializing_admin()