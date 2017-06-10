# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import html

# add title to webpage
def print_head(page_title):
    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
            <html lang="en">
        		<head>
            	    <!-- Meta Tag -->
            	    <meta charset="UTF-8">
                   	<title>""")
    print(page_title)
    print(                  """</title>
            	</head>""")

# add beginning of <body> code
def print_body_head(caption, show_button_manePage):
    print("""
        <body>
            <table>
            <tr>
            <td>
            <table border="0" width="90%" align="left" cellpadding="0" height="1%">
                <tr>
                    <td>
                        <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
                    </td>
                    <td>""", end='')

    if show_button_manePage == "yes":
        print(      """ <form action = "../index.html" >
                            <p> <input type = "submit" value = "НА ГЛАВНУЮ"> </p > 
                        </form >""")
    print(          """
                    </td>
                </tr>
                <tr>
                    <td>
                        <h3>
                            <nobr>""", end='')
    print(caption, end='')
    print(              """</nobr>
                        </h3>
                    </td>
                </tr> """)


def get_values_from_address_bar(form, *mas):
    out_mas = []
    for i in mas:
        j = form.getfirst(i, "не задано")
        out_mas.append(html.escape(j))
    return out_mas



# Check. Faculty and specialty are exist.
def check_fac_spec(cur, faculty, specialty):
    cur.execute("SELECT faculty from specialties WHERE faculty=%s AND specialty=%s;",[faculty, specialty])
    rows = cur.fetchall()
    if rows == []:
        return 0
    else:
        return 1

# Check. Is discipline exist on faculty
def check_discipline_on_faculty(cur, faculty,  discipline_name, specialty):
    cur.execute("SELECT discipline_name from disciplines WHERE faculty=%s AND discipline_name=%s AND specialty=%s;", [faculty,  discipline_name, specialty])
    rows = cur.fetchall()
    if rows == []:
        return 0
    else:
        return 1


def check_discipline_name_and_Id(cur, discipline_name, discipline_id):
    cur.execute("SELECT discipline_name from disciplines WHERE discipline_name=%s AND discipline_id=%s;", [discipline_name, discipline_id])
    rows = cur.fetchall()
    if rows == []:
        return 0
    else:
        return 1



# check. Student (stud_id) study discipline_id
def check_mark_by_stud_id_and_discipline_id(cur, stud_id, discipline_id):
    cur.execute("SELECT mark from  marks WHERE stud_id=%s AND discipline_id=%s;",[stud_id, discipline_id])
    rows = cur.fetchall()
    if rows == []:
        return 0
    else:
        return 1


# get examination_form of discipline_id for a student
def get_and_check_examination_form(cur, stud_id, discipline_id):
    cur.execute("SELECT faculty, specialty from students WHERE stud_id=%s", [stud_id])
    mas1 = cur.fetchall()
    cur.execute("SELECT faculty, specialty, examination_form from disciplines WHERE discipline_id=%s", [discipline_id])
    mas2 = cur.fetchall()
    if mas1[0] != mas2[0] or mas1[1] != mas2[1] :
        return 0
    else:
        return mas2[2]


# GET all faculties and specialties
def get_faculties_specialties_mas(cur):
    cur.execute("SELECT DISTINCT faculty from specialties")
    faculties = cur.fetchall()
    cur.execute("SELECT DISTINCT specialty from specialties")
    specialties = cur.fetchall()
    faculties.sort()             # TODO: потом убрать сортировку и сделать так, чтобы факультетам соотвествовали специальности.
    specialties.sort()
    return [faculties, specialties]


# GET different variants of examination_form
def get_examination_form_mas(cur):
    cur.execute("SELECT DISTINCT examination_form from disciplines")
    examination_form = cur.fetchall()
    examination_form.sort()
    return examination_form



db_name = "university"
import psycopg2
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

marks_mas = ['Не зачтено', 'Зачтено', 'Не аттест.', 'Не удовл.', 'Удовл.', 'Хорошо', 'Отлично'] # TODO реализовать отдельную БД с разными типами оценок, в завиисимотси от формы аттестиции
examination_form_mas = ['Зачет', 'Экзамен']

