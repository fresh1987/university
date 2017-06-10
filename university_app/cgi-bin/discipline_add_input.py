#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, print_body_head, get_faculties_specialties_mas, get_examination_form_mas

def main():
    [faculties, specialties] =  get_faculties_specialties_mas(cur)
    examination_form = get_examination_form_mas(cur)

    print_head("Добавление дисциплины")
    print_body_head("ВВЕДИТЕ ИНФОРМАЦИЮ О НОВОЙ ДИСЦИПЛИНЕ", "yes")
    print("""
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

       </body>
   </html>""")

main()