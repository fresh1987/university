#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()

db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

def get_discipline_id(faculty, specialty):
    cur.execute("SELECT DISTINCT discipline_id from disciplines WHERE faculty=%s AND specialty=%s ORDER BY discipline_id;", [faculty, specialty])
    return cur.fetchall()

def get_stud_from_specialty(faculty, specialty):
    cur.execute("SELECT stud_id from students WHERE stud_faculty=%s AND stud_specialty=%s ORDER BY stud_id;", [faculty, specialty])
    return cur.fetchall()

from common_function import marks_mas

def main():
    form = cgi.FieldStorage()
    faculty = form.getfirst("faculty", "не задано")
    specialty = form.getfirst("specialty", "не задано")

    disciplines = get_discipline_id(faculty, specialty)
    stud_id_mas = get_stud_from_specialty(faculty, specialty)

    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
	    	<html lang="en">
		    <head>
    		    <!-- Meta Tag -->
	    	    <meta charset="UTF-8">
       		    <title>Добавление оценки</title>
    		</head>
            <body>
                <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
                <h3>ВВЕДИТЕ ИНФОРМАЦИЮ О ОЦЕНКЕ</h3>
                <h3>
                <form action="/cgi-bin/mark_add_finish.py">
                    <table border="1">
                        <tr>
                            <td width="100px"><nobr>N студентческого билета</nobr></td>
                            <td width="200px">№ дисциплины</td>
                            <td width="100px">Оценка</td>
                        </tr>
                        <tr>
                            <td>
                               <select name="stud_id">""")
    for f in stud_id_mas:
        print(                   "<option>" + str(f[0] )+ "</option>")
    print("""                   </select>
                              </td>
                			<td>
                                <select name="discipline_id">""")
    for f in disciplines:
        print(                    "<option>" + str(f[0]) + "</option>")
    print("""                   </select>
            			    </td>
                            <td>
                                <select name="mark">""")
    for f in marks_mas:
        print(                     "<option>" + f + "</option>")
    print("""                   </select>
                			</td>
                        </tr>
                        <tr>
                			<td colspan="3" align="center">
                			    <p><input type="submit" value="Добавить запись"></p>
                			</td>
                        </tr>
                    </table>
                </form>
                </h3>
                
                <form action="/index.html">
                    <input type="submit" value="НА ГЛАВНУЮ">
                </form>
            </body>
            </html>""")

main()