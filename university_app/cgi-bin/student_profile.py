#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
cgitb.enable()

from common_function import conn, cur, print_head,print_body_head, get_values_from_address_bar

# Get information of student by student_id
def get_from_students(stud_id):
    cur.execute("SELECT stud_id, surname, name, patronymic, group_no, stud_faculty, stud_specialty FROM students WHERE stud_id = %s;",  [stud_id])
    row = cur.fetchall()
    return row[0]

# Get discipline_id  and marks by student_id
def get_discipline_and_marks(stud_id):
    discipline_and_marks = []
    cur.execute("SELECT discipline_id, mark FROM marks WHERE stud_id = %s;",  [stud_id])
    rows = cur.fetchall()
    for row in rows:
        mark = row[1]
        cur.execute("SELECT discipline_name FROM disciplines WHERE discipline_id = %s;", [row[0]])
        discip_name = cur.fetchall()[0]
        discipline_and_marks.append([discip_name,mark])
    return discipline_and_marks



def main():
    form = cgi.FieldStorage()
    [stud_id] = get_values_from_address_bar(form, "stud_id")

    student_mas = get_from_students(stud_id)
    discipline_and_marks = get_discipline_and_marks(stud_id)

    print_head("Результат поиска студентов")
    print_body_head("ПРОФИЛЬ СТУДЕНТА", "no")
    print("""
            <table border="0" align="left"  cellpadding="5">
                <tr>
                    <td>
                        <table border="1" width="800px"  >   
                            <tr align="center" height="30px">
                                <td><p><nobr>№ студентческого билета</nobr></p></td>
                                <td>Фамилия</td>
                                <td>Имя</td>
                                <td>Отчество</td>
                                <td><nobr>№ группы</nobr></td>
                                <td>Факультет</td>
                                <td>Специальность</td>
                            </tr>
                            <tr>   """)
    for i in student_mas:
        print("<td>", i, "</td>" )
    print("""               </tr> 
                        </table> 
                    </td>
                </tr>
                <tr>
                    <td>
                        <table border="1" width="500px" >   
                            <tr align="center" height="30px">
                                <td><p><nobr>Название дисциплины</nobr></p></td>
                                <td>Оценка</td>
                            </tr> """)
    for i in discipline_and_marks:
        print("<tr><td>", i[0][0], "</td>")
        print("<td>", i[1], "</td></tr>")

    print("""                    </td>
                            </tr>
                        </table>
                    </td>
                </tr>
           </table>
       </body>
   </html>""")

main()