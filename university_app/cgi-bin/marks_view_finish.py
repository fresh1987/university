#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()

from common_function import check_fac_spec


db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

def get_marks_base(faculty, specialty):
    cur.execute("SELECT discipline_id FROM disciplines WHERE faculty=%s AND specialty=%s;", [faculty, specialty])
    discipline_id_mas = cur.fetchall()

    mas = []
    for i in discipline_id_mas:
        cur.execute("SELECT mark_id, mark, stud_id, discipline_name, discipline_id FROM marks WHERE discipline_id=%s;", [i[0]])
        mas.extend(cur.fetchall())
    return mas



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
                   	<title>Оценки</title>
            	</head>""")
    if not check_fac_spec(cur, faculty, specialty):
        print(""" 
                <h3>НА ФАКУЛЬТЕТЕ НЕТ ВЫБРАННОЙ СПЕЦИАЛЬНОСТИ</h3>
                    <form action="/cgi-bin/marks_view.py">
                        <p><input type="submit" value="НАЗАД"> </p>
                    </form>""")
    else:
        mas = get_marks_base(faculty, specialty)

        print("""
            <body>
                <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
                <h3>ОЦЕНКИ СТУДЕНТОВ </h3>
                <h4>ФАКУЛЬТЕТА: """)
        print(faculty)
        print("""</h4>
                <h4>СПЕЦИАЛЬНОСТИ: """)
        print(specialty)
        print("""</h4>
                <form action="/cgi-bin/mark_add_input.py">
                    <input type="hidden" name="faculty" value=\"""", end='')
        print(faculty, end='')
        print("""\"         >
                    <input type="hidden" name="specialty" value=\"""", end='')
        print(specialty, end='')
        print("""\"         >
                    <p><input type="submit" value="Добавить новую запись"> </p>
                </form>

                <table border="1" align="left"  cellpadding="5">
                    <tr align="center" height="30px">
                        <td width="100px"><nobr>N студентческого билета</nobr></td>
                        <td width="200px">Название дисциплины</td>
                        <td width="100px">Оценка</td>
                        <td></td>
                        <td></td>
                    </tr>""")

        for i in mas:
            print("""
                        <tr>   """)
            print("""<td>""", i[2], "</td>")
            print("""<td>""", i[3], "</td>")
            print("""<td>""", i[1], "</td>")
            print("""   <td>
            
                            <form action="/cgi-bin/mark_edit.py">
                                <input type="hidden" name="mark_id" value=\"""", end='')
            print(i[0], end='')
            print("""\"         >
                                <input type="hidden" name="mark" value=\"""", end='')
            print(i[1], end='')
            print("""\"         >
                                <input type="hidden" name="stud_id" value=\"""", end='')
            print(i[2], end='')
            print("""\"         >
                                <input type="hidden" name="discipline_name" value=\"""", end='')
            print(i[3], end='')

            print("""\"         >
                                <input type="hidden" name="discipline_id" value=\"""", end='')
            print(i[4], end='')

            print("""\"         >
                                <input type="submit" value="Редактировать">
                            </form>
                        </td> """)
            print("""   <td>
                            <form action="/cgi-bin/mark_remove.py">
                                <input type="hidden" name="mark_id" value=\"""", end='')
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