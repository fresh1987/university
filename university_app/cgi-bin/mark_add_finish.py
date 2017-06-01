#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()

from common_function import check_mark_by_stud_id_and_discipline_id


db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

def add_to_base(mark, stud_id, discipline_id, discipline_name):
    cur.execute("INSERT INTO marks (mark, stud_id, discipline_id, discipline_name) VALUES (%s, %s, %s, %s);", [mark, stud_id, discipline_id, discipline_name])
    conn.commit()
    conn.close()


def get_discipline_name(discipline_id):
    cur.execute("SELECT discipline_name from disciplines WHERE discipline_id=%s;", [discipline_id])
    return cur.fetchall()[0][0]

def chech_mark(discipline_id, mark):
    cur.execute("SELECT examination_form from disciplines WHERE discipline_id=%s;", [discipline_id])
    examination_form = cur.fetchall()[0][0]
    if (examination_form == "Зачет" and mark in ['Не аттест.', 'Не удовл.', 'Удовл.', 'Хорошо', 'Отлично']) or \
            (examination_form == "Экзамен" and mark in ['Не зачтено', 'Зачтено']):
        return 0
    else:
        return 1


def main():
    form = cgi.FieldStorage()

    stud_id = form.getfirst("stud_id", "не задано")
    discipline_id  = form.getfirst("discipline_id", "не задано")
    mark  = form.getfirst("mark", "не задано")
    discipline_name = get_discipline_name(discipline_id)

    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
        	    	<html lang="en">
    	    	    <head>
        	    	    <!-- Meta Tag -->
    	    	        <meta charset="UTF-8">
           		        <title>Добавление</title>
            		</head>""")

    if not chech_mark(discipline_id, mark):
        print(""" 
                <h3>Оценка не соотвествует форме аттестации выбранной дисциплины</h3>""")
    else:
        print("""
                <body>
                    <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2> """)

        if not check_mark_by_stud_id_and_discipline_id(cur, stud_id, discipline_id):
            add_to_base(mark, stud_id, discipline_id, discipline_name)
            print(""" <h3>ИНФОРМАЦИЯ О НОВОЙ ОЦЕНКЕ ВНЕСЕНА</h3> """)
        else:
            print(""" <h3>НЕЛЬЗЯ ДОБАВИТЬ, Т.К. У СТУДЕНТА УЖЕ ЕСТЬ ОЦЕНКА ПО ЭТОЙ ДИСЦИПЛИНЕ </h3> """)

    print("""  
                <form action="/index.html">
                    <p><input type="submit" value="НА ГЛАВНУЮ"> </p>
                </form>
                
            </body>
        </html>""")

main()