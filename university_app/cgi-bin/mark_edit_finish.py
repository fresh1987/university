#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, print_body_head, get_values_from_address_bar

def update_base(mark, mark_id):
    cur.execute("UPDATE marks SET mark=%s WHERE mark_id = %s;",[mark, mark_id])
    conn.commit()
    conn.close()

def main():
    form = cgi.FieldStorage()
    [mark, mark_id] = get_values_from_address_bar(form, "mark", "mark_id")

    print_head("Изменение оценки")
    update_base(mark, mark_id)
    print_body_head("РЕДАКТИРОВАНИЕ ВЫПОЛНЕНО УСПЕШНО", "yes")
    print("""  
            </body>
        </html>""")

main()