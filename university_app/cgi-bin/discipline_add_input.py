#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2
import cgitb
cgitb.enable()

from common_function import get_faculties_specialties_mas, get_examination_form_mas

db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

def main():
    [faculties, specialties] =  get_faculties_specialties_mas(cur)
    examination_form = get_examination_form_mas(cur)

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
            <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
            <h3>ВВЕДИТЕ ИНФОРМАЦИЮ О НОВОМ ДИСЦИПЛИНЕ</h3>
            <form action="/cgi-bin/discipline_add_finish.py">
                <table>
                    <tr>
                        <td>Название дисциплины</td>
                        <td>Факультет</td>
                        <td>Специальность</td>
                        <td>Форма аттестации</td>
                    </tr>
                    <tr>
                        <td>
                           <input type="text" name="discipline_name">
                        </td>
                        <td>
                            <select name="faculty">""")
    #print(                  "<option>не задано</option>")
    for f in faculties:
       print(               "<option>" + f[0] + "</option>")
    print("""               </select>
            			</td>
                        <td>
                            <select name="specialty">""")
    #print(                  "<option>не задано</option>")
    for s in specialties:
        print(               "<option>" + s[0] + "</option>")
    print("""               </select>
                        </td>
                        <td>
                            <select name="examination_form">""")
    #print(                  "<option>не задано</option>")
    for ef in examination_form:
        print(               "<option>" + ef[0] + "</option>")
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