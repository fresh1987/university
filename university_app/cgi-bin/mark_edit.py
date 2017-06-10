#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, marks_mas, examination_form_mas, print_body_head, get_values_from_address_bar

def get_examination_form(discipline_id):
    cur.execute("SELECT examination_form FROM disciplines WHERE discipline_id=%s;", [discipline_id])
    examination_form = cur.fetchall()[0][0]
    if examination_form=="Экзамен":
        return marks_mas[2:]
    else:
        return marks_mas[:2]



def main():

    form = cgi.FieldStorage()
    [mark_id, mark, stud_id, discipline_name, discipline_id] = get_values_from_address_bar(form, "mark_id", "mark", "stud_id", "discipline_name", "discipline_id")

    examination_form_mas = get_examination_form(discipline_id)
    print_head("Редактирование")
    print_body_head("РЕДАКТИРОВАНИЕ ОЦЕНКИ", "yes")
    print("""<table border="0" width="1800px" align="left"  cellpadding="5">
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