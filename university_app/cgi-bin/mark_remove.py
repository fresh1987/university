#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, print_body_head

def del_from_base(mark_id):
    cur.execute("DELETE FROM marks WHERE mark_id = %s;", [mark_id])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    del_from_base(form.getfirst("mark_id", "не задано"))

    print_head("Удаление")
    print_body_head("УДАЛЕНИЕ ВЫПОЛНЕНО УСПЕШНО", "yes")
    print("""
       </body>
   </html>""")

main()