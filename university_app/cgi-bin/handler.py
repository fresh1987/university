#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import psycopg2

import cgitb
cgitb.enable()

db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

def get_values_for_request():
    form = cgi.FieldStorage()
    faculty = form.getfirst("faculty", "не задано")
    specialty = form.getfirst("specialty", "не задано")
    group_nom = form.getfirst("group_nom", "не задано")
    surname = form.getfirst("surname", "не задано")
    name = form.getfirst("name", "не задано")
    patronymic = form.getfirst("patronymic", "не задано")

    faculty = html.escape(faculty)
    specialty = html.escape(specialty)
    group_nom = html.escape(group_nom)
    surname = html.escape(surname)
    name = html.escape(name)
    patronymic= html.escape(patronymic)
    return(faculty, specialty, group_nom, surname, name, patronymic)


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
    (faculty, specialty, group_nom, surname, name, patronymic) = get_values_for_request()

    # Проверяем что № группы корректный
    try:
        students_mas = find_students(faculty, specialty, group_nom, surname, name, patronymic)
    except:
        students_mas = []

    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
		<html lang="en">
		<head>
		    <!-- Meta Tag -->
		    <meta charset="UTF-8">
		    <title>Результат поиска студентов</title>
		</head>
		<body>""")

    print("""
        <body>
       		<h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
            <h3>РЕЗУЛЬТАТЫ ПОИСКА</h3>
            <h3>""")
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
        print(""" <h1>Нет такого студента</h1>""")
    print("""
            </h3>
        </body>
   </html>""")

main()