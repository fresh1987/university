#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, print_body_head, check_discipline_on_faculty, check_fac_spec, get_values_from_address_bar


def add_to_base(discipline_name, faculty, specialty, examination_form):
    cur.execute("INSERT INTO disciplines (discipline_name, faculty, specialty, examination_form) VALUES (%s, %s, %s, %s);", [discipline_name, faculty, specialty, examination_form])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    [discipline_name, faculty, specialty, examination_form] = get_values_from_address_bar(form,"discipline_name", "faculty", "specialty", "examination_form")

    print_head("Добавление дисциплины")

    if check_fac_spec(cur, faculty, specialty):
        if not check_discipline_on_faculty(cur, faculty,  discipline_name, specialty):
            add_to_base(discipline_name, faculty, specialty, examination_form)
            print_body_head("ИНФОРМАЦИЯ О НОВОЙ ДИСЦИПЛИНЕ ВНЕСЕНА УСПЕШНО", "yes")
        else:
            print_body_head("ДИСЦИПЛИНА С ТАКИМ ИМЕНЕМ УЖЕ ЕСТЬ НА УКАЗАННОЙ СПЕЦИАЛЬНОСТИ ВЫБРАННОГО ФАКУЛЬТЕТА", "yes")
    else:
        print_body_head("НА ВЫБРАННОМ ФАКУЛЬТЕТЕ НЕТ УКАЗАННОЙ СПЕЦИАЛЬНОСТИ", "yes")

    print("""  
            </body>
        </html>""")

main()