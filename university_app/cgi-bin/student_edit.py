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

    form = cgi.FieldStorage()
    stud_id = form.getfirst("stud_id", "не задано")
    surname = form.getfirst("surname", "не задано")
    name = form.getfirst("name", "не задано")
    patronymic = form.getfirst("patronymic", "не задано")
    group_no = form.getfirst("group_no", "не задано")
    stud_faculty = form.getfirst("stud_faculty", "не задано")
    stud_specialty = form.getfirst("stud_specialty", "не задано")

    [faculties, specialties] = get_faculties_specialties_mas(cur)

    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
	    	<html lang="en">
		    <head>
    		    <!-- Meta Tag -->
	    	    <meta charset="UTF-8">
       		    <title>Редактирование</title>
    		</head>""")
    print("""
        <body>
            <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
            <h3>РЕДАКТИРОВАНИЕ ИНФОРМАЦИИ О СТУДЕНТЕ</h3>
            <h3>
            <table border="0" width="1800px" align="left"  cellpadding="5">
                <tr>
                    <td> Данные из БД:</td>
                </tr>
                <tr>
                    <td>
                        <table border="1" align="left"  cellpadding="5">
                            <tr align="center" height="30px">
                                <td width="100px">Фамилия</td>
                                <td width="100px">Имя</td>
                                <td width="100px">Отчество</td>
                                <td width="50px"><nobr>№ группы</nobr></td>
                                <td width="300px">Факультет</td>
                                <td width="300px">Специальность</td>
                            </tr>
                            <tr>   """)
    print(     """              <td width="300px">""", surname, "</td>" )
    print(     """              <td width="300px">""", name, "</td>" )
    print(     """              <td width="300px">""", patronymic, "</td>" )
    print(     """              <td width="300px">""", group_no, "</td>" )
    print(     """              <td width="300px">""", stud_faculty, "</td>" )
    print(     """              <td width="300px">""", stud_specialty, "</td>" )

    print("""             </tr>
                        </table>
                    </td>
                </tr>
                <tr height="30px">
                    <td colspan="2">Введите данные для замены:</td>
                </tr>
                <tr>
                    <td>
                        <table border="1" align="left"  cellpadding="5">
                            <tr>
                                <td width="300px">Фамилия</td>
                                <td width="300px">Имя</td>
                                <td width="300px">Отчество</td>
                                <td width="300px"><nobr>№ группы</nobr></td>
                                <td width="300px">Факультет</td>
                                <td width="300px">Специальность</td>
                            </tr>
                            
                            <tr>
                                <td>
                                    <form action="/cgi-bin/student_edit_finish.py">
                                        <input type="hidden" name="stud_id" value=\"""", end='')

    print(stud_id, end='')



    print("""\"                     >
                                        <input  size="30px" type="text" name="surname" value=\"""", end='')
    print(surname, end='')
    print("""\"                     >
                                   </td>
                                   <td>
                                        <input  size="30px" type="text" name="name" value=\"""", end='')
    print(name, end='')
    print("""\"                     >
                                   </td>
                                   <td>
                                        <input  size="30px" type="text" name="patronymic" value=\"""", end='')
    print(patronymic, end='')
    print("""\"                     >
                                   </td>
                                   <td>
                                        <input  size="30px" type="text" name="group_no" value=\"""", end='')
    print(group_no, end='')
    print("""\"                     >
                                   </td>
                                  <td>
                                        <select name="stud_faculty">""")
    for s in faculties:
        print(                              "<option>" + s[0] + "</option>")
    print("""                           </select>
                                    </td>
                                    <td>
                                        <select name="stud_specialty">""")
    for s in specialties:
        print(                              "<option>" + s[0] + "</option>")
    print("""                           </select>
                            </tr>
                            <tr>
                                <td colspan="6">
                                        <p align="center"><input type="submit" value="Применить изменения"> </p>
                                    </form>
                               </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table> 
       </body>
   </html>""")

main()