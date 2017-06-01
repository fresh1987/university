#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()

db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

def update_base(mark, mark_id):
    cur.execute("UPDATE marks SET mark=%s WHERE mark_id = %s;",[mark, mark_id])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    mark = form.getfirst("mark", "не задано")
    mark_id = form.getfirst("mark_id", "не задано")

    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
        	    	<html lang="en">
    	    	    <head>
        	    	    <!-- Meta Tag -->
    	    	        <meta charset="UTF-8">
           		        <title>Изменение оценки</title>
            		</head>""")
    print("""
                <body>
                    <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2> """)

    update_base(mark, mark_id)
    print(""" <h3>РЕДАКТИРОВАНИЕ ВЫПОЛНЕНО УСПЕШНО</h3> """)
    print("""  
                <form action="/index.html">
                    <p><input type="submit" value="НА ГЛАВНУЮ"> </p>
                </form>

            </body>
        </html>""")

main()