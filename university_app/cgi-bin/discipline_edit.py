#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, print_body_head, get_examination_form_mas, get_values_from_address_bar


def main():

    form = cgi.FieldStorage()
    [discipline_id, discipline_name, examination_form, faculty, specialty] = get_values_from_address_bar(form, "discipline_id", "discipline_name", "examination_form", "faculty", "specialty")
    examination_form_mas = get_examination_form_mas(cur)

    print_head("Редактирование")
    print_body_head("РЕДАКТИРОВАНИЕ ДИСЦИПЛИНЫ", "yes")
    print("""
            <table border="0" width="1200px" align="left"  cellpadding="5">
                <tr>
                    <td> Данные из БД:</td>
                </tr>
                <tr>
                    <td>
                        <table border="1" align="left"  cellpadding="5">
                            <tr align="center" height="30px">
                                <td width="300px">Дисциплина</td>
                                <td width="300px">Форма аттестации</td>
                                <td width="300px">Факультет</td>
                                <td width="300px">Специальность</td>
                            </tr>
                            <tr>   """)
    print(     """              <td width="300px">""", discipline_name, "</td>" )
    print(     """              <td width="300px">""", examination_form, "</td>" )
    print(     """              <td width="300px">""", faculty, "</td>" )
    print(     """              <td width="300px">""", specialty, "</td>" )

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
                                <td width="280px">Название дисциплины</td>
                                <td width="280px">Форма аттестации</td>
                            </tr>
                            
                            <tr>
                                <td>
                                    <form action="/cgi-bin/discipline_edit_finish.py">
                                        <input type="hidden" name="discipline_id" value=\"""", end='')

    print(discipline_id, end='')
    print("""\"                     >
                                       <input type="hidden" name="faculty" value=\"""", end='')

    print(faculty, end='')
    print("""\"                     >
                                        <input type="hidden" name="specialty" value=\"""", end='')
    print(specialty, end='')
    print("""\"                     >
                                           <input  size="30px" type="text" name="discipline_name" value=\"""", end='')
    print(discipline_name, end='')
    print("""\"                     >
                                   </td>
                                   <td>
                                        <select name="examination_form">""")
    for s in examination_form_mas:
        print(                              "<option>" + s[0] + "</option>")
    print("""                           </select>
                                    </td>
                            </tr>
                            <tr>
                                <td colspan="4">
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