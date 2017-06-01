#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()

db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

def get_from_base():
    cur.execute("SELECT specialty_id, faculty, specialty FROM specialties ORDER BY faculty, specialty;")
    rows = cur.fetchall()
    return rows

def main():

    mas = get_from_base()
    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
	    	<html lang="en">
		    <head>
    		    <!-- Meta Tag -->
	    	    <meta charset="UTF-8">
       		    <title>Направления подготовки</title>
    		</head>""")
    print("""
        <body>
            <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
            <h3>НАПРАВЛЕНИЯ ПОДГОТОВКИ</h3>
            <h3>
                <form action="/cgi-bin/specialty_add_input.py">
                    <p><input type="submit" value="Добавить новую запись"> </p>
                </form>

            <table border="1" width="950px" align="left"  cellpadding="5">
                <tr align="center" height="30px">
                    <td width="300px">Факультет</td>
                    <td width="300px">Специальность</td>
                    <td></td>
                    <td></td>
                </tr>""")
    for i in mas:
        print("""
                <tr>   """)
        print(     """<td width="400px">""", i[1], "</td>" )
        print(     """<td width="400px">""", i[2], "</td>" )

        print("""   <td>
                        <form action="/cgi-bin/specialty_edit.py">
                            <input type="hidden" name="specialty_id" value=\"""", end='')
        print(i[0], end='')
        print("""\"         >
                            <input type="hidden" name="faculty" value=\"""", end='')
        print(i[1], end='')
        print("""\"         >
                            <input type="hidden" name="specialty" value=\"""", end='')
        print(i[2], end='')
        print("""\"         >

                            <p><input type="submit" value="Редактировать"> </p>
                        </form>
                    </td> """)
        print("""   <td>
                        <form action="/cgi-bin/specialty_remove.py">
                            <input type="hidden" name="specialty_id" value=\"""", end='')
        print(i[0], end='')
        print("""\"         >
                            <p><input type="submit" value="Удалить"> </p>
                        </form>
                    </td>

                </tr>   """)

    print("""
            </table> 
       </body>
   </html>""")

main()