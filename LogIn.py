import tkinter
from tkinter import messagebox
from database import *
from Admin import *
from ProfessorHome import *
from Student import *


class LogIn:
    def __init__(self):
        pass

    def initializing_login(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("757x584+201+50")
        self.main_window.minsize(116, 1)
        self.main_window.maxsize(1370, 750)
        self.main_window.resizable(1, 1)
        self.main_window.title("Account Login")
        self.main_window.configure(background="#c9af98")

        self.welcome_label = tkinter.Label(self.main_window)
        self.welcome_label.place(relx=0.317, rely=0.051, height=41, width=284)
        self.welcome_label.configure(background="#c9af98")
        self.welcome_label.configure(font="-family {Lucida Sans} -size 15 -weight"
                                          " bold")
        self.welcome_label.configure(text='''Choose User Type''')

        # User Type
        self.user_type = tkinter.IntVar()

        self.admin_type_label = tkinter.Radiobutton(self.main_window)
        self.admin_type_label.place(relx=0.185, rely=0.360, relheight=0.058, relwidth=0.156)
        self.admin_type_label.configure(background="#c9af98")
        self.admin_type_label.configure(font="-family {Lucida Sans Typewriter} -size 14 -weight bold")
        self.admin_type_label.configure(text='''Admin''')
        self.admin_type_label.configure(variable=self.user_type, value=1)

        self.Canvas1 = tkinter.Canvas(self.main_window)
        self.Canvas1.place(relx=0.185, rely=0.137, relheight=0.227, relwidth=0.182)
        self.img = tkinter.PhotoImage(file="admin.gif")
        self.Canvas1.create_image(70, 64, image=self.img)

        self.professor_type_label = tkinter.Radiobutton(self.main_window)
        self.professor_type_label.place(relx=0.423, rely=0.360, relheight=0.058, relwidth=0.182)
        self.professor_type_label.configure(background="#c9af98")
        self.professor_type_label.configure(font="-family {Lucida Sans Typewriter} -size 14 -weight bold")
        self.professor_type_label.configure(text='''Professor''')
        self.professor_type_label.configure(variable=self.user_type, value=2)

        self.Canvas2 = tkinter.Canvas(self.main_window)
        self.Canvas2.place(relx=0.423, rely=0.137, relheight=0.227, relwidth=0.182)
        self.img2 = tkinter.PhotoImage(file="professor.gif")
        self.Canvas2.create_image(70, 64, image=self.img2)

        self.student_type_label = tkinter.Radiobutton(self.main_window)
        self.student_type_label.place(relx=0.647, rely=0.360, relheight=0.058, relwidth=0.156)
        self.student_type_label.configure(background="#c9af98")
        self.student_type_label.configure(font="-family {Lucida Sans Typewriter} -size 14 -weight bold")
        self.student_type_label.configure(text='''Student''')
        self.student_type_label.configure(variable=self.user_type, value=3)

        self.Canvas3 = tkinter.Canvas(self.main_window)
        self.Canvas3.place(relx=0.661, rely=0.137, relheight=0.227, relwidth=0.182)
        self.img1 = tkinter.PhotoImage(file="student3.gif")
        self.Canvas3.create_image(70, 64, image=self.img1)

        # self.admin_type_label.pack()
        # self.professor_type_label.pack()
        # self.student_type_label.pack()

        # Username Label and Entry
        self.username = tkinter.StringVar()
        self.username_label = tkinter.Label(self.main_window)
        self.username_label.place(relx=0.251, rely=0.445, height=41, width=134)
        self.username_label.configure(background="#c9af98")
        self.username_label.configure(font="-family {Lucida Sans} -size 15 -weight bold")
        self.username_label.configure(text='''Username :''')

        self.username_entry = tkinter.Entry(self.main_window,
                                            textvariable=self.username)
        self.username_entry.place(relx=0.476, rely=0.462, relheight=0.058, relwidth=0.309)
        self.username_entry.configure(background="white")
        self.username_entry.configure(font="-family {Segoe UI} -size 14")

        # self.username_label.pack()
        # self.username_entry.pack()

        # Password Label and Entry
        self.password = tkinter.StringVar()
        self.password_label = tkinter.Label(self.main_window)
        self.password_label.place(relx=0.251, rely=0.548, height=41, width=134)
        self.password_label.configure(background="#c9af98")
        self.password_label.configure(font="-family {Lucida Sans} -size 15 -weight bold")
        self.password_label.configure(text='''Password :''')

        self.password_entry = tkinter.Entry(self.main_window,
                                            textvariable=self.password)
        self.password_entry.place(relx=0.476, rely=0.565, relheight=0.058, relwidth=0.309)
        self.password_entry.configure(background="white")
        self.password_entry.configure(font="-family {Segoe UI} -size 14")

        # self.password_label.pack()
        # self.password_entry.pack()

        # Buttons : LogIn
        self.login_button = tkinter.Button(self.main_window,
                                           command=self.logged_in)
        self.login_button.place(relx=0.323, rely=0.736, height=44, width=111)
        self.login_button.configure(background="#bfbfbf")
        self.login_button.configure(font="-family {Segoe UI} -size 14 -weight bold -underline 1")
        self.login_button.configure(text='''Login''')

        self.quit_button = tkinter.Button(self.main_window,
                                          command=self.main_window.destroy)
        self.quit_button.place(relx=0.534, rely=0.736, height=44, width=111)
        self.quit_button.configure(background="#bfbfbf")
        self.quit_button.configure(font="-family {Segoe UI} -size 14 -weight bold -underline 1")
        self.quit_button.configure(text='''Quit''')

        tkinter.mainloop()

    def destroy_main_window(self):
        self.main_window.destroy()

    def logged_in(self):
        option = ""
        if self.user_type.get() == 1:
            option = "Admin"
        elif self.user_type.get() == 2:
            option = "Professor"
        elif self.user_type.get() == 3:
            option = "Student"
        else:
            option = "500"

        credentials = database_connection('SELECT * FROM '+DATABASE_NAME+'.login;', 'all', 0)

        flag = False
        for row in credentials:
            if row[1] == self.username.get() and row[2] == self.password.get() and row[3] == option:
                flag = True

        print("Option: ", option)
        if flag:
            if option == "Admin":
                self.main_window.destroy()
                load_admin = Admin()
                load_admin.initializing_admin()
            elif option == "Professor":
                self.main_window.destroy()
                load_professor = ProfessorHome()
                load_professor.initializing_professor()
            elif option == "Student":
                self.main_window.destroy()
                load_student = Student()
                load_student.initialising_student()
            else:
                pass


# login = LogIn()
# login.initializing_login()

