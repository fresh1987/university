#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, print_body_head, get_values_from_address_bar

# find student in database
def find_students(faculty, specialty, group_nom, surname, name, patronymic):
    if specialty != "не задано":
        students_mas = []
        cur.execute("SELECT stud_id, surname, name, patronymic, group_no, stud_faculty, stud_specialty FROM students WHERE stud_specialty = %s;",  [specialty])
        rows = cur.fetchall()
        for row in rows:
            students_mas.append(row)
    else:
        students_mas = []
        cur.execute("SELECT stud_id, surname, name, patronymic, group_no, stud_faculty, stud_specialty FROM students")
        rows = cur.fetchall()
        for row in rows:
            students_mas.append(row)

    students_mas_del = students_mas[:]
    if surname != "не задано":
        for i in students_mas_del:
            if i[1] != surname:  students_mas.remove(i)
        students_mas_del = students_mas[:]

    if name != "не задано":
        for i in students_mas_del:
            if i[2] != name:  students_mas.remove(i)
        students_mas_del = students_mas[:]

    if patronymic != "не задано":
        for i in students_mas_del:
            if i[3] != patronymic:  students_mas.remove(i)
        students_mas_del = students_mas[:]

    if group_nom != "не задано":
        for i in students_mas_del:
            if i[4] != group_nom:  students_mas.remove(i)
        students_mas_del = students_mas[:]

    if faculty!= "не задано":
        for i in students_mas_del:
            if i[5] != faculty:  students_mas.remove(i)
        students_mas_del = students_mas[:]

    return students_mas


def main():
    form = cgi.FieldStorage()
    [faculty, specialty, group_nom, surname, name, patronymic] = get_values_from_address_bar(form, "faculty", "specialty", "group_nom", "surname", "name", "patronymic")

    # Проверяем что № группы корректный
    try:
        students_mas = find_students(faculty, specialty, group_nom, surname, name, patronymic)
    except:
        students_mas = []

    print_head("Результат поиска студентов")
    print_body_head("РЕЗУЛЬТАТЫ ПОИСКА", "no")
    if students_mas != []:
        print(""" 
            <table border="1" width="700px" align="left"  cellpadding="5" >   
                <tr align="center" height="30px">
                    <td><p><nobr>№ студентческого билета</nobr></p></td>
                    <td>Фамилия</td>
                    <td>Имя</td>
                    <td>Отчество</td>
                    <td><nobr>№ группы</nobr></td>
                    <td>Факультет</td>
                    <td>Специальность</td>
                    <td></td>
                </tr>""")
        for i in students_mas:
            print("""
                <tr>""")
            for j in i :
                print("<td>", j, "</td>")
            print("""
                    <td>
                        <form action="/cgi-bin/student_profile.py">
                        <input type="hidden" name="stud_id" value=\"""", end ='')
            print(i[0], end ='')
            print("""\">
                        <p><input type="submit" value="Посмотреть профиль"> </p>
                        </form>
                    </td>
                </tr> """)
        print(""
            "</table>")

    else:
        print("""
                <tr>
                    <td>
                        <h1><nobr>Нет такого студента</nobr></h1>
                    </td>
                </tr>""")
    print("""
        </body>
   </html>""")

main()