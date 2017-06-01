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

def update_base(specialty_id, faculty, specialty):
    cur.execute("UPDATE specialties SET specialty = %s, faculty = %s WHERE specialty_id = %s;", [specialty, faculty, specialty_id])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    specialty_id = form.getfirst("specialty_id", "не задано")
    faculty = form.getfirst("faculty", "не задано")
    specialty = form.getfirst("specialty", "не задано")



    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
	    	<html lang="en">
		    <head>
    		    <!-- Meta Tag -->
	    	    <meta charset="UTF-8">
       		    <title>Редактирование</title>
    		</head>""")
    if not check_fac_spec(cur, faculty, specialty):
        update_base(specialty_id, faculty, specialty)
        print("""
            <body>
                <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
                <h3>РЕДАКТИРОВАНИЕ ВЫПОЛНЕНО УСПЕШНО</h3>""")
    else:
        print("""ВВЕДЕННАЯ ИНФОРМАЦИЯ ПОВТОРЯЕТ НАЧАЛЬНУЮ   ЛИБО    УКАЗАННАЯ СПЕЦИАЛЬНОСТЬ УЖЕ ЕСТЬ НА ВЫБРАННОМ ФАКУЛЬТЕТЕ""")
    print("""
                <form action="/index.html">
                    <p><input type="submit" value="НА ГЛАВНУЮ"> </p>
                </form>
       </body>
   </html>""")

main()