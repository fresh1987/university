#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, check_fac_spec, print_body_head, get_values_from_address_bar

def add_to_base(faculty, specialty):
    cur.execute("INSERT INTO specialties (faculty,specialty) VALUES (%s, %s);", [faculty, specialty])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    [faculty, specialty] = get_values_from_address_bar(form, "faculty", "specialty")



    print_head("Добавление")
    if not check_fac_spec(cur, faculty, specialty):
        add_to_base(faculty, specialty)
        print_body_head("ИНФОРМАЦИЮ О НОВОМ НАПРАВЛЕНИИ ПОДГОТОВКИ ВНЕСЕНА УСПЕШНО", "yes")
    else:
        print_body_head("УКАЗАННАЯ СПЕЦИАЛЬНОСТЬ УЖЕ ЕСТЬ НА ВЫБРАННОМ ФАКУЛЬТЕТЕ", "yes")

    print("""
       </body>
   </html>""")

main()