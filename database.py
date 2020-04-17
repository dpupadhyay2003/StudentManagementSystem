import mysql.connector
from mysql.connector import Error

HOST = 'localhost'
DATABASE_NAME = 'college_software'
USERNAME = 'root'
PASSWORD = ''


def installing_database():
    try:
        connection = mysql.connector.Connect(host=HOST, user=USERNAME, password=PASSWORD)
        if connection.is_connected():
            cursor = connection.cursor()

            # Creating Database
            cursor.execute('use information_schema;')
            cursor.execute('SELECT COUNT(*) FROM schemata WHERE SCHEMA_NAME="' + DATABASE_NAME + '";')
            if cursor.fetchone()[0] == 0:
                cursor.execute('CREATE DATABASE '+DATABASE_NAME+';')
                cursor.execute('use '+DATABASE_NAME+';')
            else:
                cursor.execute('use '+DATABASE_NAME+';')

            # Create Tables
            cursor.execute(
                'CREATE TABLE `' + DATABASE_NAME + '`.`login` (  `id` int(11) NOT NULL AUTO_INCREMENT,  `username` varchar(45) NOT NULL,  `password` varchar(45) NOT NULL,  `account_type` varchar(45) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;');
            cursor.execute(
                'CREATE TABLE `' + DATABASE_NAME + '`.`course` (`id` INT NOT NULL AUTO_INCREMENT,`course_id` VARCHAR(45) NOT NULL,`course_name` VARCHAR(45) NOT NULL,`course_fees` VARCHAR(45) NOT NULL,  PRIMARY KEY (`id`));')
            cursor.execute(
                'CREATE TABLE `' + DATABASE_NAME + '`.`professor` (  `id` INT(11) NOT NULL AUTO_INCREMENT,  `prof_id` VARCHAR(45) NOT NULL,  `prof_name` VARCHAR(45) NOT NULL,  `prof_email` VARCHAR(45) NOT NULL,  `username` VARCHAR(45) NOT NULL,  `password` VARCHAR(45) NOT NULL,  `phone` INT(12) NULL,  `course_id` INT(12) NULL,  PRIMARY KEY (`id`), FOREIGN KEY (`course_id`) REFERENCES `college_software`.`course`(`id`));')
            cursor.execute(
                'CREATE TABLE `' + DATABASE_NAME + '`.`student` ( `id` INT(11) NOT NULL AUTO_INCREMENT,  `student_id` VARCHAR(45) NOT NULL, `student_name` VARCHAR(45) NOT NULL,  `grade` INT(11) NULL DEFAULT NULL, `student_email` VARCHAR(45) NOT NULL,  `username` VARCHAR(45) NOT NULL, `password` VARCHAR(45) NOT NULL,  `phone` INT(12) NULL, `course_id` INT(12) NULL,  PRIMARY KEY (`id`), FOREIGN KEY (`course_id`) REFERENCES `college_software`.`course`(`id`));')

            # Creating 3 Users: Admin, Professor and Password:
            cursor.execute(
                'INSERT INTO `' + DATABASE_NAME + '`.`login`(`id`,`username`,`password`,`account_type`) VALUES (1, "admin", "admin", "Admin"),(2, "professor", "professor", "Professor"),(3, "student", "student", "Student");')


    except Error as e:
        print("Error While conecting MySQL!", e)
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            print('MySQL Connection is Closed.')


def database_connection(query, count, fetch_size):
    try:
        connection = mysql.connector.Connect(host=HOST, database=DATABASE_NAME, user=USERNAME, password=PASSWORD)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query)
            if count == '1':
                return cursor.fetchone()
            elif count == 'all':
                return cursor.fetchall()
            elif count == 'many':
                return cursor.fetchmany(fetch_size)
            else:
                return ''
    except Error as e:
        print("Error While conecting MySQL!", e)
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            print('MySQL Connection is Closed.')


def insert_Query(table_name, data_list):
    try:
        connection = mysql.connector.Connect(host=HOST, database=DATABASE_NAME, user=USERNAME, password=PASSWORD)
        if connection.is_connected():
            cursor = connection.cursor()

            insert_query = ''
            if table_name == 'student':
                insert_query = 'INSERT INTO ' + DATABASE_NAME + '.student (student_id, student_name, grade, student_email, username, password, ' \
                                                                'phone, course_id) VALUES ("' + data_list[0] + '", "' + \
                               data_list[1] + '", ' + data_list[2] + ', "' + \
                               data_list[3] + '", "' + data_list[4] + '", "' + data_list[5] + '", ' + data_list[6] + ',' \
                                                                                                                     '' + \
                               data_list[7] + ') '
            elif table_name == 'professor':
                insert_query = 'INSERT INTO ' + DATABASE_NAME + '.professor (prof_id, prof_name, prof_email, username, password, ' \
                                                                'phone, course_id) VALUES ("' + data_list[0] + '", "' + \
                               data_list[1] + '", "' + data_list[2] + '",' \
                                                                      '"' + data_list[3] + '", "' + data_list[
                                   4] + '", "' + data_list[5] + '", "' + data_list[6] + '") '
            elif table_name == 'course':
                insert_query = 'INSERT INTO ' + DATABASE_NAME + '.course (course_id, course_name, course_fees) ' \
                                                                'VALUES ("' + data_list[0] + '", "' + data_list[
                                   1] + '", "' + data_list[2] + '") '
            else:
                pass
            cursor.execute(insert_query)
            return True
    except Error as e:
        print("Error While conecting MySQL!", e)
        return False
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            print('MySQL Connection is Closed.')


def delete_query(table_name, id):
    try:
        connection = mysql.connector.Connect(host=HOST, database=DATABASE_NAME, user=USERNAME, password=PASSWORD)
        if connection.is_connected():
            cursor = connection.cursor()

            delete_query = ''
            if table_name == 'student':
                delete_query = 'DELETE FROM ' + DATABASE_NAME + '.student WHERE student_id=' + id + ';'
            elif table_name == 'professor':
                delete_query = 'DELETE FROM ' + DATABASE_NAME + '.professor WHERE prof_id=' + id + ';'
            elif table_name == 'course':
                delete_query = 'DELETE FROM ' + DATABASE_NAME + '.course WHERE course_id=' + id + ';'
            else:
                pass
            cursor.execute(delete_query)
            return True
        else:
            return False
    except Error as e:
        print("Error While connecting MySQL!", e)
        return False
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            print('MySQL Connection is Closed.')


def update_query(table_name, dataList):
    try:
        connection = mysql.connector.Connect(host=HOST, database=DATABASE_NAME, user=USERNAME, password=PASSWORD)
        if connection.is_connected():
            cursor = connection.cursor()

            update_query = ''
            if table_name == 'student':
                update_query = 'update ' + DATABASE_NAME + '.student set student_name="' + dataList[1] + '", grade="' + \
                               dataList[2] + '", student_email="' + dataList[3] + '",' \
                                                                                  ' username="' + dataList[
                                   4] + '", `password`="' + dataList[5] + '", phone="' + dataList[
                                   6] + '", course_id="' + \
                               dataList[7] + '"' \
                                             ' where student_id="' + dataList[0] + '";'
            elif table_name == 'professor':
                update_query = 'update ' + DATABASE_NAME + '.professor set prof_name="' + dataList[
                    1] + '", prof_email="' + dataList[2] + '", ' \
                                                           'username="' + dataList[3] + '", `password`="' + dataList[
                                   4] + '", phone="' + dataList[5] + '", ' \
                                                                     'course_id="' + dataList[6] + '" where prof_id="' + \
                               dataList[0] + '" ;'
            elif table_name == 'course':
                update_query = 'update ' + DATABASE_NAME + '.course set course_name="' + dataList[1] + '", ' \
                                                                                                       'course_fees="' + \
                               dataList[2] + '" where course_id="' + dataList[0] + '";'
            else:
                pass
            cursor.execute(update_query)
            return True
        else:
            return False
    except Error as e:
        print("Error While connecting MySQL!", e)
        return False
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            print('MySQL Connection is Closed.')


def common_query(query):
    try:
        connection = mysql.connector.Connect(host=HOST, database=DATABASE_NAME, user=USERNAME, password=PASSWORD)
        if connection.is_connected():
            cursor = connection.cursor()
            if cursor.execute(query):
                return True
            else:
                return False
    except Error as e:
        print("Error While conecting MySQL!", e)
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            print('MySQL Connection is Closed.')
