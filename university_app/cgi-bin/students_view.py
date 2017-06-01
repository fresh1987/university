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
    cur.execute("SELECT  stud_id, surname, name, patronymic, group_no, stud_faculty, stud_specialty FROM students ORDER BY surname;")
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
       		    <title>Студенты</title>
    		</head>""")
    print("""
        <body>
            <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
            <h3>СТУДЕНТЫ</h3>
            <h3>
                <form action="/cgi-bin/student_add_input.py">
                    <p><input type="submit" value="Добавить новую запись"> </p>
                </form>

            <table border="1" align="left"  cellpadding="5">
                <tr align="center" height="30px">
                    <td width="100px"><nobr>№ студентческого билета</nobr></td>
                    <td width="100px">Фамилия</td>
                    <td width="100px">Имя</td>
                    <td width="100px">Отчество</td>
                    <td width="50px"><nobr>№ группы</nobr></td>
                    <td width="300px">Факультет</td>
                    <td width="300px">Специальность</td>
                    <td></td>
                    <td></td>
                </tr>""")
    for i in mas:
        print("""
                <tr>   """)
        print(     """<td>""", i[0], "</td>" )
        print(     """<td>""", i[1], "</td>" )
        print(     """<td>""", i[2], "</td>" )
        print(     """<td>""", i[3], "</td>" )
        print(     """<td>""", i[4], "</td>" )
        print(     """<td>""", i[5], "</td>" )
        print(     """<td>""", i[6], "</td>" )

        print("""   <td>
                        <form action="/cgi-bin/student_edit.py">
                            <input type="hidden" name="stud_id" value=\"""", end='')
        print(i[0], end='')
        print("""\"         >
                            <input type="hidden" name="surname" value=\"""", end='')
        print(i[1], end='')
        print("""\"         >
                             <input type="hidden" name="name" value=\"""", end='')
        print(i[2], end='')

        print("""\"         >
                            <input type="hidden" name="patronymic" value=\"""", end='')
        print(i[3], end='')

        print("""\"         >
                            <input type="hidden" name="group_no" value=\"""", end='')
        print(i[4], end='')

        print("""\"         >
                             <input type="hidden" name="stud_faculty" value=\"""", end='')
        print(i[5], end='')

        print("""\"         >
                             <input type="hidden" name="stud_specialty" value=\"""", end='')
        print(i[6], end='')
        print("""\"         >
                            <p><input type="submit" value="Редактировать"> </p>
                        </form>
                    </td> """)
        print("""   <td>
                        <form action="/cgi-bin/student_remove.py">
                            <input type="hidden" name="stud_id" value=\"""", end='')
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