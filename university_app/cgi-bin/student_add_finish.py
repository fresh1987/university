#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()

from common_function import check_fac_spec

db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

def add_to_base(surname, name, patronymic, group_no, stud_faculty, stud_specialty):
    cur.execute("INSERT INTO students (surname, name, patronymic, group_no, stud_faculty, stud_specialty) VALUES (%s, %s, %s, %s, %s, %s);", [surname, name, patronymic, group_no, stud_faculty, stud_specialty])
    conn.commit()
    conn.close()


def main():
    form = cgi.FieldStorage()
    surname = form.getfirst("surname", "не задано")
    name = form.getfirst("name", "не задано")
    patronymic = form.getfirst("patronymic", "не задано")
    group_no = form.getfirst("group_no", "не задано")
    stud_faculty = form.getfirst("stud_faculty", "не задано")
    stud_specialty = form.getfirst("stud_specialty", "не задано")

    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
        	    	<html lang="en">
    	    	    <head>
        	    	    <!-- Meta Tag -->
    	    	        <meta charset="UTF-8">
           		        <title>Добавление</title>
            		</head>""")
    print("""
                <body>
                    <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2> """)

    if check_fac_spec(cur, stud_faculty, stud_specialty):
        add_to_base(surname, name, patronymic, group_no, stud_faculty, stud_specialty)

        print(""" <h3>ИНФОРМАЦИЯ О НОВОМ СТУДЕНТЕ ВНЕСЕНА</h3> """)
    else:
        print(""" <h3>НА УКАЗАННОМ ФАКУЛЬТЕТЕ НЕТ УКАЗАННОЙ СПЕЦИАЛЬНОСТИ</h3>
                        <form action="/cgi-bin/student_add_input.py">
                            <p><input type="submit" value="НАЗАД"> </p>
                        </form>""")
    print("""  
                <form action="/index.html">
                    <p><input type="submit" value="НА ГЛАВНУЮ"> </p>
                </form>
                
            </body>
        </html>""")

main()