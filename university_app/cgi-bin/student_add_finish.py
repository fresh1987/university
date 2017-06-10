#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, print_body_head, check_fac_spec, get_values_from_address_bar

def add_to_base(surname, name, patronymic, group_no, stud_faculty, stud_specialty):
    cur.execute("INSERT INTO students (surname, name, patronymic, group_no, stud_faculty, stud_specialty) VALUES (%s, %s, %s, %s, %s, %s);", [surname, name, patronymic, group_no, stud_faculty, stud_specialty])
    conn.commit()
    conn.close()


def main():
    form = cgi.FieldStorage()
    [surname, name, patronymic, group_no, stud_faculty, stud_specialty] = get_values_from_address_bar(form, "surname", "name", "patronymic", "group_no", "stud_faculty", "stud_specialty")

    print_head("Добавление")
    if check_fac_spec(cur, stud_faculty, stud_specialty):
        add_to_base(surname, name, patronymic, group_no, stud_faculty, stud_specialty)
        print_body_head("ИНФОРМАЦИЯ О НОВОМ СТУДЕНТЕ ВНЕСЕНА" , "yes")
    else:
        print_body_head("НА УКАЗАННОМ ФАКУЛЬТЕТЕ НЕТ УКАЗАННОЙ СПЕЦИАЛЬНОСТИ", "yes")
    print("""  
            </body>
        </html>""")

main()