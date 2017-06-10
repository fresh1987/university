#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, check_fac_spec, print_body_head, get_values_from_address_bar


def update_base(stud_id, surname, name, patronymic, group_no, stud_faculty, stud_specialty):
    cur.execute("UPDATE students SET surname=%s, name=%s, patronymic=%s, group_no=%s, stud_faculty=%s, stud_specialty=%s WHERE stud_id = %s;", \
                [surname, name, patronymic, group_no, stud_faculty, stud_specialty, stud_id])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    [stud_id, surname, name, patronymic, group_no, stud_faculty, stud_specialty] = get_values_from_address_bar(form,"stud_id", "surname", "name", "patronymic", "group_no", "stud_faculty", "stud_specialty")

    print_head("Редактировнаие")
    if check_fac_spec(cur, stud_faculty, stud_specialty):
        update_base(stud_id, surname, name, patronymic, group_no, stud_faculty, stud_specialty)
        print_body_head("РЕДАКТИРОВАНИЕ ВЫПОЛНЕНО УСПЕШНО", "yes")
    else:
        print_body_head("НА ФАКУЛЬТЕТЕ НЕТ ТАКОЙ СПЕЦИАЛЬНОСТИ", "yes")
        print("""
    
            </body>
        </html>""")

main()