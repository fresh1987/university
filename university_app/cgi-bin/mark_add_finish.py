#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
cgitb.enable()

from common_function import conn, cur, print_head, check_mark_by_stud_id_and_discipline_id,print_body_head, get_values_from_address_bar

def add_to_base(mark, stud_id, discipline_id):
    cur.execute("INSERT INTO marks (mark, stud_id, discipline_id) VALUES (%s, %s, %s);", [mark, stud_id, discipline_id])
    conn.commit()
    conn.close()


def get_discipline_id(discipline_name, faculty, specialty):
    cur.execute("SELECT discipline_id from disciplines WHERE discipline_name=%s AND faculty=%s AND specialty=%s;", [discipline_name,faculty, specialty])
    return (cur.fetchall()[0][0])

def chech_mark(discipline_id, mark):
    cur.execute("SELECT examination_form from disciplines WHERE discipline_id=%s;", [str(discipline_id)])
    examination_form = cur.fetchall()[0][0]
    if (examination_form == "Зачет" and mark in ['Не аттест.', 'Не удовл.', 'Удовл.', 'Хорошо', 'Отлично']) or \
            (examination_form == "Экзамен" and mark in ['Не зачтено', 'Зачтено']):
        return 0
    else:
        return 1


def main():
    form = cgi.FieldStorage()
    [stud_id, discipline_name, mark, faculty, specialty] = get_values_from_address_bar(form, "stud_id", "discipline_name", "mark", "faculty", "specialty")

    discipline_id = get_discipline_id(discipline_name, faculty, specialty)

    print_head("Добавление")

    if not chech_mark(discipline_id, mark):
        print_body_head("Оценка не соотвествует форме аттестации выбранной дисциплины", "yes")
    else:
        if not check_mark_by_stud_id_and_discipline_id(cur, stud_id, discipline_id):
            add_to_base(mark, stud_id, discipline_id)
            print_body_head("ИНФОРМАЦИЯ О НОВОЙ ОЦЕНКЕ ВНЕСЕНА", "yes")
        else:
            print_body_head("НЕЛЬЗЯ ДОБАВИТЬ, Т.К. У СТУДЕНТА УЖЕ ЕСТЬ ОЦЕНКА ПО ЭТОЙ ДИСЦИПЛИНЕ", "yes")

    print("""  
            </body>
        </html>""")

main()