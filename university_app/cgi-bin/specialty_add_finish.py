#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()
db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

from common_function import check_fac_spec

def add_to_base(faculty, specialty):
    cur.execute("INSERT INTO specialties (faculty,specialty) VALUES (%s, %s);", [faculty, specialty])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    faculty = form.getfirst("faculty", "не задано")
    specialty = form.getfirst("specialty", "не задано")

    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
    	    	<html lang="en">
    		    <head>
        		    <!-- Meta Tag -->
    	    	    <meta charset="UTF-8">
           		    <title>Добавление</title>
        		</head>""")
    if not check_fac_spec(cur, faculty, specialty):
        add_to_base(faculty, specialty)
        print("""
            <body>
                <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
                <h3>ИНФОРМАЦИЮ О НОВОМ НАПРАВЛЕНИИ ПОДГОТОВКИ ВНЕСЕНА УСПЕШНО</h3>""")
    else:
        print("""УКАЗАННАЯ СПЕЦИАЛЬНОСТЬ УЖЕ ЕСТЬ НА ВЫБРАННОМ ФАКУЛЬТЕТЕ""")

    print("""
            <form action="/index.html">
                <p><input type="submit" value="НА ГЛАВНУЮ"> </p>
            </form>
       </body>
   </html>""")

main()