#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi

import cgitb
cgitb.enable()
from common_function import conn, cur, print_head, check_fac_spec, print_body_head, get_values_from_address_bar

def update_base(specialty_id, faculty, specialty):
    cur.execute("UPDATE specialties SET specialty = %s, faculty = %s WHERE specialty_id = %s;", [specialty, faculty, specialty_id])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    [specialty_id, faculty, specialty] = get_values_from_address_bar(form, "specialty_id", "faculty", "specialty")

    print_head("Редактирование")
    if not check_fac_spec(cur, faculty, specialty):
        update_base(specialty_id, faculty, specialty)
        print_body_head("РЕДАКТИРОВАНИЕ ВЫПОЛНЕНО УСПЕШНО", "yes")
    else:
        print_body_head("УКАЗАННАЯ СПЕЦИАЛЬНОСТЬ УЖЕ ЕСТЬ НА ВЫБРАННОМ ФАКУЛЬТЕТЕ", "yes")

    print("""
       </body>
   </html>""")

main()