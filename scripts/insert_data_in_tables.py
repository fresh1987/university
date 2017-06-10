# -*- coding: utf-8 -*-

# This script add data in database
import sys
sys.path.append("../university_app/cgi-bin")
from common_function import cur, conn,  examination_form_mas, marks_mas

#import psycopg2
from random import randint

# function to fill the mas data from file
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

# Script constant
surnames = []
names = []
patronymics = []
examination_mas_save = []

stud_id = 0
discipline_id = 0

faculty_quantity = 20
specialty_quantity = 10
students_group_quantity = 20
course_quantity = 5
discipline_quantity = 100

man_surname_all = fill_mas('man_surname')
woman_surname_all = fill_mas('woman_surname')
man_name_all = fill_mas('man_name')
woman_name_all = fill_mas('woman_name')
man_patronymic_all = fill_mas('man_patronymic')
woman_patronymic_all = fill_mas('woman_patronymic')


# fill the base
for f in range(10, 10+faculty_quantity):
    # input faculties
    faculty_base = 'faculty_' + str(f)

    # add specialties to base
    for s in range(10, 10+specialty_quantity):
        specialty_base = 'f_' + str(f) + '_specialty_' + str(s)
        specialty_short = "f_" + faculty_base[-2:] + "_s_" + str(s)
        new_add = (faculty_base, specialty_base)
        cur.execute("INSERT INTO specialties (faculty, specialty) VALUES (%s, %s);", (faculty_base, specialty_base))

        # add disciplines to base
        examination_form_massiv = []
        for d in range(100, discipline_quantity+100):
            discipline_name_base =  specialty_short + '_discipline_'+str(d)
            variable = examination_form_mas[randint(0, 1)]
            cur.execute("INSERT INTO disciplines (discipline_name, examination_form, faculty, specialty) VALUES (%s, %s, %s, %s);", (discipline_name_base, variable, faculty_base, specialty_base))
            examination_form_massiv.append(variable)


        for k in range(1,6):
            # add students to base
            group_nom = str(f) + str(s) + '0' + str(k)
            for l in range(1, students_group_quantity + 1):
                stud_id += 1
                # take fio
                if randint(1,2) == 1:
                    (surname, name, patronymic) = fill_fio( man_surname_all, man_name_all, man_patronymic_all)
                else:
                    (surname, name, patronymic) = fill_fio( woman_surname_all, woman_name_all, woman_patronymic_all)

                cur.execute("INSERT INTO students (surname, name, patronymic, group_no, stud_faculty, stud_specialty) VALUES (%s, %s, %s, %s, %s, %s);", \
                        (surname, name, patronymic, group_nom, faculty_base, specialty_base))

                # add student marks to base
                discipline_id_cycle = discipline_id
                for discp in range(0, int(discipline_quantity/course_quantity) * k):
                    discipline_id_cycle += 1
                    if examination_form_massiv[discp] == examination_form_mas[0]:
                        mark = marks_mas[randint(0,1)]
                    else:
                        mark = marks_mas[randint(2,6)]
                    cur.execute("INSERT INTO marks (stud_id, discipline_id, mark) VALUES (%s, %s, %s);", (stud_id, discipline_id_cycle, mark))
        discipline_id += discipline_quantity
conn.commit()
conn.close()

print("SUCCESS")