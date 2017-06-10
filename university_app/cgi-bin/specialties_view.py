#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, print_body_head

def get_from_base():
    cur.execute("SELECT specialty_id, faculty, specialty FROM specialties ORDER BY faculty, specialty;")
    rows = cur.fetchall()
    return rows

def main():
    # get list of information of specialities
    mas = get_from_base()

    print_head("Направления подготовки")
    print_body_head("НАПРАВЛЕНИЯ ПОДГОТОВКИ", "no")

    print("""
                <tr>
                    <td>
                        <form action="/cgi-bin/specialty_add_input.py">
                            <p><input type="submit" value="Добавить новую запись"> </p>
                        </form>
                    </td>
                </tr>
            </table>
            </td>
            </tr>

            <tr>
            <td>
            <table border="1" width="800px" align="left"  cellpadding="5">
                <tr align="center" height="30px">
                    <td width="250px">Факультет</td>
                    <td width="250px">Специальность</td>
                    <td></td>
                    <td></td>
                </tr>""")
    for i in mas:
        print("""
                <tr>   """)
        print(     """<td width="250px">""", i[1], "</td>" )
        print(     """<td width="250px">""", i[2], "</td>" )

        print("""   <td>
                        <form action="/cgi-bin/specialty_edit.py">
                            <input type="hidden" name="specialty_id" value=\"""", end='')
        print(i[0], end='')
        print("""\"         >
                            <input type="hidden" name="faculty" value=\"""", end='')
        print(i[1], end='')
        print("""\"         >
                            <input type="hidden" name="specialty" value=\"""", end='')
        print(i[2], end='')
        print("""\"         >

                            <p><input type="submit" value="Редактировать"> </p>
                        </form>
                    </td> """)
        print("""   <td>
                        <form action="/cgi-bin/specialty_remove.py">
                            <input type="hidden" name="specialty_id" value=\"""", end='')
        print(i[0], end='')
        print("""\"         >
                            <p><input type="submit" value="Удалить"> </p>
                        </form>
                    </td>

                </tr>   """)

    print("""
            </table>
            </td>
            </tr>
            </table>
       </body>
   </html>""")

main()