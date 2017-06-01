#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()


db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

from common_function import get_faculties_specialties_mas

def main():
    [faculties, specialties] = get_faculties_specialties_mas(cur)

    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
	    	<html lang="en">
		    <head>
    		    <!-- Meta Tag -->
	    	    <meta charset="UTF-8">
       		    <title>Добавление инфорамции о новом студенте</title>
    		</head>""")
    print("""
        <body>
            <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
            <h3>ВВЕДИТЕ ИНФОРМАЦИЮ О НОВОМ СТУДЕНТЕ</h3>
            <form action="/cgi-bin/student_add_finish.py">
                <table border="1">
                    <tr>
                        <td width="100px">Фамилия</td>
                        <td width="100px">Имя</td>
                        <td width="100px">Отчество</td>
                        <td width="50px">№ группы</td>
                        <td width="300px">Факультет</td>
                        <td width="300px">Специальность</td>
                    </tr>
                    <tr>
                        <td>
                           <input type="text" name="surname">
                        </td>
                        <td>
                           <input type="text" name="name">
                        </td>
                        <td>
                           <input type="text" name="patronymic">
                        </td>
                        <td>
                           <input type="text" name="group_no">
                        </td>
                        <td>
                            <select name="stud_faculty">""")
    for f in faculties:
       print(               "<option>" + f[0] + "</option>")
    print("""               </select>
            			</td>
                        <td>
                            <select name="stud_specialty">""")
    for s in specialties:
        print(               "<option>" + s[0] + "</option>")
    print("""               </select>
                        </td>
                    </tr>
                </table>
                <p><input type="submit" value="Добавить запись"> </p>
            </form>
                
            <form action="/index.html">
                <p><input type="submit" value="НА ГЛАВНУЮ"> </p>
            </form>
       </body>
   </html>""")

main()