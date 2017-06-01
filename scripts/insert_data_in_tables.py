# -*- coding: utf-8 -*-
db_name = "university"

import psycopg2
from random import randint

faculties = []
specialtes = []
disciplines = []
surnames = []
names = []
patronymics = []

# function to fill the mas data by file
def fill_mas(file_name):
    mas = []
    for i in open(file_name, 'r').readlines():
        mas.append(i[:-1])
    return mas

# function to generate student FIO
def fill_fio(surname_mas, name_mas, patronymic_mas):
    surn = surname_mas[randint(0,len(surname_mas)-1)]
    name = name_mas[randint(0,len(name_mas)-1)]
    patr = patronymic_mas[randint(0,len(patronymic_mas)-1)]
    return (surn, name, patr)


faculty_quantity = 20
specialty_quantity = 10
students_group_quantity = 20
course_quantity = 5
discipline_quantity = 100
examination_form_mas = ['Зачет', 'Экзамен']
marks_mas = [['Зачтено','Не зачтено'], ['Не аттест.', 'Не удовл.','Удовл.','Хорошо','Отлично']]
examination_mas_save = []

specialty_counter = 9
discipline_counter = 0

man_surname_all = fill_mas('man_surname')
woman_surname_all = fill_mas('woman_surname')
man_name_all = fill_mas('man_name')
woman_name_all = fill_mas('woman_name')
man_patronymic_all = fill_mas('man_patronymic')
woman_patronymic_all = fill_mas('woman_patronymic')



conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()


for f in range(10, 10+faculty_quantity):
    for s in range(10, 10+specialty_quantity):

        # input faculties
        faculty_base = 'faculty_' + str(f)
        specialty_counter += 1
        specialty_base = 'specialty_' + str(specialty_counter)
        new_add = (faculty_base, specialty_base)
        cur.execute("INSERT INTO specialties (faculty, specialty) VALUES (%s, %s);", (faculty_base, specialty_base))

        # input disciplines
        for d in range(1, discipline_quantity+1):
            discipline_counter += 1
            discipline_name_base = 'discipline_'+str(discipline_counter)
            variable = examination_form_mas[randint(0, 1)]
            examination_mas_save.append(variable)
            cur.execute("INSERT INTO disciplines (discipline_name, examination_form, faculty, specialty) VALUES (%s, %s, %s, %s);", (discipline_name_base, variable, faculty_base, specialty_base))


        discp_start = ((f - 10) * specialty_quantity + (s - 10)) * discipline_quantity
        student_nom_save = ((f - 10) * specialty_quantity + (s - 10)) * students_group_quantity * course_quantity
        for k in range(1,6):

            # input students and marks
            group_nom = str(f) + str(s) + '0' + str(k)
            for l in range(1, students_group_quantity + 1):
                # take fio
                if randint(1,2) == 1:
                    (surname, name, patronymic) = fill_fio( man_surname_all, man_name_all, man_patronymic_all)
                else:
                    (surname, name, patronymic) = fill_fio( woman_surname_all, woman_name_all, woman_patronymic_all)

                cur.execute("INSERT INTO students (surname, name, patronymic, group_no, stud_faculty, stud_specialty) VALUES (%s, %s, %s, %s, %s, %s);", \
                        (surname, name, patronymic, group_nom, faculty_base, specialty_base))

                # input marks
                student_nom = student_nom_save + (k-1)* students_group_quantity + l

                for discp in range(1, int(discipline_quantity/course_quantity) * k + 1):
                    if examination_mas_save[discp_start + discp - 1] == examination_form_mas[0]:
                        mark = marks_mas[0][randint(0,1)]
                    else:
                        mark = marks_mas[1][randint(0,4)]
                    disp_nom = discp_start + discp
                    cur.execute("INSERT INTO marks (stud_id, discipline_id, discipline_name, mark) VALUES (%s, %s, %s, %s);", (student_nom, disp_nom, "discipline_"+str(disp_nom), mark))

conn.commit()
conn.close()
