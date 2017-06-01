#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2
from common_function import check_fac_spec
import cgitb
cgitb.enable()
from common_function import check_discipline_on_faculty, check_fac_spec


db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

def add_to_base(discipline_name, faculty, specialty, examination_form):
    cur.execute("INSERT INTO disciplines (discipline_name, faculty, specialty, examination_form) VALUES (%s, %s, %s, %s);", [discipline_name, faculty, specialty, examination_form])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    discipline_name = form.getfirst("discipline_name", "не задано")
    faculty = form.getfirst("faculty", "не задано")
    specialty = form.getfirst("specialty", "не задано")
    examination_form = form.getfirst("examination_form", "не задано")

    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
        	    	<html lang="en">
    	    	    <head>
        	    	    <!-- Meta Tag -->
    	    	        <meta charset="UTF-8">
           		        <title>Добавление дисциплины</title>
            		</head>""")
    print("""
                <body>
                    <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2> """)

    if check_fac_spec(cur, faculty, specialty):
        if not check_discipline_on_faculty(cur, faculty,  discipline_name, specialty):
            add_to_base(discipline_name, faculty, specialty, examination_form)
            print(""" <h3>ИНФОРМАЦИЯ О НОВОЙ ДИСЦИПЛИНЕ ВНЕСЕНА УСПЕШНО</h3> """)
        else:
            print(""" <h3>ДИСЦИПЛИНА С ТАКИМ ИМЕНЕМ УЖЕ ЕСТЬ НА УКАЗАННОЙ СПЕЦИАЛЬНОСТИ ВЫБРАННОГО ФАКУЛЬТЕТА</h3>""")
    else:
        print("""     <h3>НА ВЫБРАННОМ ФАКУЛЬТЕТЕ НЕТ УКАЗАННОЙ СПЕЦИАЛЬНОСТИ </h3>
                        <form action="/cgi-bin/discipline_add_input.py">
                            <p><input type="submit" value="НАЗАД"> </p>
                        </form>""")
    print("""  
                <form action="/index.html">
                    <p><input type="submit" value="НА ГЛАВНУЮ"> </p>
                </form>
                
            </body>
        </html>""")

main()