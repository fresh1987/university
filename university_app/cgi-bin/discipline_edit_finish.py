#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, print_body_head, check_discipline_on_faculty, check_discipline_name_and_Id, get_values_from_address_bar


def update_base(discipline_id, discipline_name, examination_form):
    cur.execute("UPDATE disciplines SET discipline_name = %s, examination_form = %s WHERE discipline_id = %s;", [discipline_name, examination_form, discipline_id])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    [discipline_id, discipline_name, examination_form, faculty, specialty] = get_values_from_address_bar(form, "discipline_id", "discipline_name", "examination_form", "faculty", "specialty")

    print_head("Редактирование")
    if not check_discipline_name_and_Id(cur, discipline_name, discipline_id) and check_discipline_on_faculty(cur, faculty, discipline_name, specialty):
        print_body_head("ДИСЦИПЛИНА С ТАКИМ ИМЕНЕМ УЖЕ ЕСТЬ НА УКАЗАННОЙ СПЕЦИАЛЬНОСТИ ВЫБРАННОГО ФАКУЛЬТЕТА", "yes")
    else:
        update_base(discipline_id, discipline_name, examination_form)
        print_body_head("РЕДАКТИРОВАНИЕ ВЫПОЛНЕНО УСПЕШНО", "yes")
    print(""" 
       </body>
   </html>""")

main()