#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
cgitb.enable()

from common_function import print_head, get_values_from_address_bar


def main():

    form = cgi.FieldStorage()
    [specialty_id, faculty, specialty] = get_values_from_address_bar(form, "specialty_id", "faculty", "specialty")

    print_head("Редактирование")
    print("""
        <body>
            <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
            <h3>РЕДАКТИРОВАНИЕ НАПРАВЛЕНИЯ ПОДГОТОВКИ</h3>
            <h3>
            <table border="0" width="950px" align="left"  cellpadding="5">
                <tr>
                    <td> Данные из БД:</td>
                </tr>
                <tr>
                    <td>
                        <table border="1" width="950px" align="left"  cellpadding="5">
                            <tr align="center" height="30px">
                                <td width="300px">Факультет</td>
                                <td width="300px">Специальность</td>
                            </tr>
                            <tr>   """)
    print(     """              <td width="400px">""", faculty, "</td>" )
    print(     """              <td width="400px">""", specialty, "</td>" )

    print("""             </tr>
                        </table>
                    </td>
                </tr>
                <tr height="30px">
                    <td colspan="2">Введите данные для замены:</td>
                </tr>
                <tr>
                    <td>
                        <table border="1" width="950px" align="left"  cellpadding="5">
                            <tr>
                                <td>
                                    <form action="/cgi-bin/specialty_edit_finish.py">
                                        <input type="hidden" name="specialty_id" value=\"""", end='')
    print(specialty_id, end='')
    print("""\"                     >
                                        <input type="text" name="faculty" value=\"""", end='')
    print(faculty, end='')
    print("""\"                     >
                                </td>
                                <td>
                                        <input type="text" name="specialty" value =\"""", end='')
    print(specialty, end='')
    print("""\"                     >
                                </td>
                            </tr>
                            <tr>
                                <td colspan="2">
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