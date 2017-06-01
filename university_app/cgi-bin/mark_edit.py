#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()

db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

from common_function import marks_mas, examination_form_mas

def get_examination_form(discipline_id):
    cur.execute("SELECT examination_form FROM disciplines WHERE discipline_id=%s;", [discipline_id])
    examination_form = cur.fetchall()[0][0]
    if examination_form=="Экзамен":
        return marks_mas[2:]
    else:
        return marks_mas[:2]



def main():

    form = cgi.FieldStorage()
    mark_id = form.getfirst("mark_id", "не задано")
    mark = form.getfirst("mark", "не задано")
    stud_id = form.getfirst("stud_id", "не задано")
    discipline_name = form.getfirst("discipline_name", "не задано")
    discipline_id = form.getfirst("discipline_id", "не задано")

    examination_form_mas = get_examination_form(discipline_id)

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
            <h3>РЕДАКТИРОВАНИЕ ОЦЕНКИ</h3>
            <h3>
            <table border="0" width="1800px" align="left"  cellpadding="5">
                <form action="/cgi-bin/mark_edit_finish.py">
                    <tr>
                        <td>
                            <table border="1" align="left"  cellpadding="5">
                                <tr align="center" height="30px">
                                    <td width="100px"><nobr>N студентческого билета</nobr></td>
                                    <td width="300px">Название дисциплины</td>
                                    <td width="100px">Оценка</td>
                                    <td width="100px">Введите оценку для замены</td>
                                </tr>
                                <tr>   """)
    print(     """                  <td width="100px">""", stud_id, "</td>" )
    print(     """                  <td width="300px">""", discipline_name, "</td>" )
    print(     """                  <td width="300px">""", mark, "</td>" )
    print("""                       <td>
                                        <select name="mark">""")
    for ef in examination_form_mas:
        print(                              "<option>" + ef + "</option>")
    print("""                           </select>
                                        <input type="hidden" name="mark_id" value=\"""", end='')
    print(mark_id, end='')
    print("""\"         >
                                    </td>
                               </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="3" align="center">
                            <p><input type="submit" value="ЗАМЕНИТЬ ОЦЕНКУ"> </p>
                        </td>
                    </tr>
                <form>
            </table> 
       </body>
   </html>""")

main()