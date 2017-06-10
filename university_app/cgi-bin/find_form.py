#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common_function import conn, cur, print_head, print_body_head

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


print_head("Форма поиска студентов")
print_body_head("ФОРМА ПОИСКА СТУДНТОВ", "no")
print("""
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