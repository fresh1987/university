#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()


def del_from_base(mark_id):
    db_name = "university"
    conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("DELETE FROM marks WHERE mark_id = %s;", [mark_id])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    del_from_base(form.getfirst("mark_id", "не задано"))

    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
	    	<html lang="en">
		    <head>
    		    <!-- Meta Tag -->
	    	    <meta charset="UTF-8">
       		    <title>Удаление</title>
    		</head>""")
    print("""
        <body>
            <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
            <h3>УДАЛЕНИЕ ВЫПОЛНЕНО УСПЕШНО</h3>
            <h3>
                <form action="/index.html">
                    <p><input type="submit" value="НА ГЛАВНУЮ"> </p>
                </form>
       </body>
   </html>""")

main()