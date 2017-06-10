#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
cgitb.enable()


from common_function import conn, cur, print_head, print_body_head, marks_mas,get_values_from_address_bar

def get_disciplines_list(faculty, specialty):
    cur.execute("SELECT DISTINCT discipline_name from disciplines WHERE faculty=%s AND specialty=%s ORDER BY discipline_name;", [faculty, specialty])
    return cur.fetchall()

def get_stud_from_specialty(faculty, specialty):
    cur.execute("SELECT stud_id from students WHERE stud_faculty=%s AND stud_specialty=%s ORDER BY stud_id;", [faculty, specialty])
    return cur.fetchall()

def main():
    form = cgi.FieldStorage()
    [faculty, specialty] = get_values_from_address_bar(form,"faculty", "specialty")

    disciplines = get_disciplines_list(faculty, specialty)
    stud_id_mas = get_stud_from_specialty(faculty, specialty)

    print_head("Добавление оценки")
    print_body_head("ВВЕДИТЕ ИНФОРМАЦИЮ О ОЦЕНКЕ", "yes")
    print("""   <form action="/cgi-bin/mark_add_finish.py">
                    <table border="1">
                        <tr>
                            <td width="100px"><nobr>N студентческого билета</nobr></td>
                            <td width="200px">Название дисциплины</td>
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
                                <select name="discipline_name">""")
    for f in disciplines:
        print(                    "<option>" + str(f[0]) + "</option>")
    print("""                   </select>
            			    </td>
                            <td>
                                <select name="mark">""")
    for f in marks_mas:
        print(                     "<option>" + f + "</option>")
    print("""                   </select>

                			    <input type="hidden" name="faculty" value=\"""", end='')
    print(faculty, end='')
    print("""\"                 >
                                <input type="hidden" name="specialty" value=\"""", end='')
    print(specialty, end='')
    print("""\"                 >
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
            </body>
            </html>""")

main()