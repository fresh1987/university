#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
cgitb.enable()

from common_function import check_fac_spec, conn, cur, print_head, print_body_head, get_values_from_address_bar

def get_marks_base(faculty, specialty):
    discipline_id_mas = []
    discipline_name_mas = []
    cur.execute("SELECT discipline_id, discipline_name FROM disciplines WHERE faculty=%s AND specialty=%s;", [faculty, specialty])
    mas = cur.fetchall()
    for i in mas:
        discipline_id_mas.append(i[0])
        discipline_name_mas.append(i[1])

    mas = []
    for counter, i in enumerate(discipline_id_mas):
        cur.execute("SELECT mark_id, mark, stud_id, discipline_id FROM marks WHERE discipline_id=%s;", [i])
        for j in cur.fetchall():
            list_j = list(j)
            list_j.append(discipline_name_mas[counter])
            mas.append(list_j)
        #print(mas)
    return [mas]



def main():
    form = cgi.FieldStorage()

    [faculty, specialty] = get_values_from_address_bar(form, "faculty", "specialty")

    print_head("Оценки")
    if not check_fac_spec(cur, faculty, specialty):
        print_body_head("НА ФАКУЛЬТЕТЕ НЕТ ВЫБРАННОЙ СПЕЦИАЛЬНОСТИ", "yes")
    else:
        [mas] = get_marks_base(faculty, specialty)

        print_body_head("ОЦЕНКИ СТУДЕНТОВ", "yes")
        print("""
            <tr>
                <td>
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
            print("""<td>""", i[4], "</td>")
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
            print(i[4], end='')

            print("""\"         >
                                <input type="hidden" name="discipline_id" value=\"""", end='')
            print(i[3], end='')

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