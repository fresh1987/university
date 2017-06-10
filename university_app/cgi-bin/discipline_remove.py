#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
cgitb.enable()


from common_function import conn, cur, print_head, print_body_head

def del_from_base(discipline_id):
    cur.execute("DELETE FROM disciplines WHERE discipline_id = %s;", [discipline_id])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    discipline_id = form.getfirst("discipline_id", "не задано")

    del_from_base(discipline_id)

    print_head("Удаление")
    print_body_head("УДАЛЕНИЕ ВЫПОЛНЕНО УСПЕШНО", "yes")
    print("""
       </body>
   </html>""")

main()