# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def check_fac_spec(cur, faculty, specialty):
    cur.execute("SELECT faculty from specialties WHERE faculty=%s AND specialty=%s;",[faculty, specialty])
    rows = cur.fetchall()
    if rows == []:
        return 0
    else:
        return 1

def check_discipline_on_faculty(cur, faculty,  discipline_name, specialty):
    cur.execute("SELECT discipline_name from  disciplines WHERE faculty=%s AND  discipline_name=%s AND specialty=%s;",[faculty,  discipline_name, specialty])
    rows = cur.fetchall()
    if rows == []:
        return 0
    else:
        return 1

def check_mark_by_stud_id_and_discipline_id(cur, stud_id, discipline_id):
    cur.execute("SELECT mark from  marks WHERE stud_id=%s AND discipline_id=%s;",[stud_id, discipline_id])
    rows = cur.fetchall()
    if rows == []:
        return 0
    else:
        return 1





def get_and_check_examination_form(cur, stud_id, discipline_id):
    cur.execute("SELECT faculty, specialty from students WHERE stud_id=%s", [stud_id])
    mas1 = cur.fetchall()
    cur.execute("SELECT faculty, specialty, examination_form from disciplines WHERE discipline_id=%s", [discipline_id])
    mas2 = cur.fetchall()
    if mas1[0] != mas2[0] or mas1[1] != mas2[1] :
        return 0
    else:
        return mas2[2]



def get_faculties_specialties_mas(cur):
    cur.execute("SELECT DISTINCT faculty from specialties")
    faculties = cur.fetchall()
    cur.execute("SELECT DISTINCT specialty from specialties")
    specialties = cur.fetchall()
    faculties.sort()             # TODO: потом убрать сортировку и сделать так, чтобы факультетам соотвествовали специальности.
    specialties.sort()
    return [faculties, specialties]



def get_examination_form_mas(cur):
    cur.execute("SELECT DISTINCT examination_form from disciplines")
    examination_form = cur.fetchall()
    examination_form.sort()
    return examination_form



marks_mas = ['Не зачтено', 'Зачтено', 'Не аттест.', 'Не удовл.', 'Удовл.', 'Хорошо', 'Отлично'] # TODO реализовать отдельную БД с разными типами оценок, в завиисимотси от формы аттестиции
examination_form_mas = ['Зачет', 'Экзамен']

