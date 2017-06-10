#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, print_body_head, get_values_from_address_bar

def del_from_base(stud_id):
    cur.execute("DELETE FROM students WHERE stud_id = %s;", [stud_id])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    [stud_id] = get_values_from_address_bar(form, "stud_id")
    del_from_base(stud_id)

    print_head("Удаление")
    print_body_head("УДАЛЕНИЕ ВЫПОЛНЕНО УСПЕШНО", "yes")
    print("""
       </body>
   </html>""")

main()