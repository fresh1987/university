#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, print_body_head, get_faculties_specialties_mas

def main():
    [faculties, specialties] = get_faculties_specialties_mas(cur)

    print_head("Добавление инфорамции о новом студенте")
    print_body_head("ВВЕДИТЕ ИНФОРМАЦИЮ О НОВОМ СТУДЕНТЕ", "no")
    print("""
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
       </body>
   </html>""")

main()