#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()

from common_function import check_discipline_on_faculty, check_fac_spec

db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

def update_base(discipline_id, discipline_name, examination_form):
    cur.execute("UPDATE disciplines SET discipline_name = %s, examination_form = %s WHERE discipline_id = %s;", [discipline_name, examination_form, discipline_id])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    discipline_id = form.getfirst("discipline_id", "не задано")
    discipline_name = form.getfirst("discipline_name", "не задано")
    examination_form = form.getfirst("examination_form", "не задано")
    faculty = form.getfirst("faculty", "не задано")
    specialty  = form.getfirst("specialty", "не задано")

    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
    	    	<html lang="en">
    		    <head>
        		    <!-- Meta Tag -->
    	    	    <meta charset="UTF-8">
           		    <title>Редактирование</title>
        		</head>""")
    if not check_discipline_on_faculty(cur, faculty, discipline_name, specialty):
        update_base(discipline_id, discipline_name, examination_form)
        print("""
            <body>
                <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
                <h3>РЕДАКТИРОВАНИЕ ВЫПОЛНЕНО УСПЕШНО</h3>""")
    else:
        print(""" <h3> ДИСЦИПЛИНА С ТАКИМ ИМЕНЕМ УЖЕ ЕСТЬ НА УКАЗАННОЙ СПЕЦИАЛЬНОСТИ ВЫБРАННОГО ФАКУЛЬТЕТА""")
    print(""" 
                <form action="/index.html">
                    <p><input type="submit" value="НА ГЛАВНУЮ"> </p>
                </form>
       </body>
   </html>""")

main()