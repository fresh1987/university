#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2

db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("SELECT faculty, specialty from specialties")
rows = cur.fetchall()
faculties = []
specialties = []
for row in rows:
   if row[0] not in faculties:
      faculties.append(row[0])
   specialties.append(row[1])
faculties.sort()
specialties.sort()


print("Content-type: text/html\n")
print("""<!DOCTYPE html>
		<html lang="en">
		<head>
		    <!-- Meta Tag -->
		    <meta charset="UTF-8">
		    <title>Форма поиска студентов</title>
		</head>""")

print("""
<body>
   <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
   <h3>ФОРМА ПОИСКА СТУДНТОВ</h3>
   <form action="/cgi-bin/handler.py">
   <table>
       <tr>
           <td><h3>Факультет</h3></td>
	       <td><select name="faculty">""")

print("<option>не задано</option>")
for f in faculties:
   print("<option>" + f + "</option>")
print("""      </select>
			</td>
      	</tr>
     	<tr>
		    <td><h3> Специальность </h3></td>
		    <td><select name="specialty">""")
print("<option>не задано</option>")
for s in specialties:
   print("<option>" + s + "</option>")
print("""   	</select>
		    </td>
        </tr>                                    	
       	<tr>
            <td><h3> Группа </h3></td>
       		<td><input type="text" name="group_nom" size="50"></td>
        </tr>  
        <tr>
            <td><h3> Фамилия </h3></td>
            <td><input type="text" name="surname" size="50"></td>
        </tr>
        <tr>
            <td><h3> Имя </h3></td>
            <td><input type="text" name="name" size="50"></td>
        </tr>  
        <tr>
            <td><h3> Отчество </h3></td>
            <td><input type="text" name="patronymic" size="50"></td>
        </tr>
        <tr>
            <td></td>
      		<td><h1><input type="submit" value="НАЙТИ"></h1></td>
        </tr>
    </table>
    </form>
</body>
</html>""")