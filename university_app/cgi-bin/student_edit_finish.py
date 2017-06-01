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


def update_base(stud_id, surname, name, patronymic, group_no, stud_faculty, stud_specialty):
    db_name = "university"
    conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("UPDATE students SET surname=%s, name=%s, patronymic=%s, group_no=%s, stud_faculty=%s, stud_specialty=%s WHERE stud_id = %s;", \
                [surname, name, patronymic, group_no, stud_faculty, stud_specialty, stud_id])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    stud_id = form.getfirst("stud_id", "не задано")
    print(stud_id)
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
           		        <title>Редактировнаие</title>
            		</head>""")
    print("""
                <body>
                    <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2> """)

    if check_fac_spec(cur, stud_faculty, stud_specialty):
        update_base(stud_id, surname, name, patronymic, group_no, stud_faculty, stud_specialty)
        print(""" <h3>РЕДАКТИРОВАНИЕ ВЫПОЛНЕНО УСПЕШНО</h3> """)
    else:
        print(""" <h3>НА ФАКУЛЬТЕТЕ НЕТ ТАКОЙ СПЕЦИАЛЬНОСТИ</h3>""")
    print("""            <form action="/index.html">
                    <p><input type="submit" value="НА ГЛАВНУЮ"> </p>
                </form>

            </body>
        </html>""")

main()