#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()

from common_function import get_faculties_specialties_mas

db_name = "university"
conn = psycopg2.connect(database=db_name, user="admin", password="admin", host="localhost", port="5432")
cur = conn.cursor()


def main():
    (faculties, specialties)  = get_faculties_specialties_mas(cur)
    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
	    	<html lang="en">
		    <head>
    		    <!-- Meta Tag -->
	    	    <meta charset="UTF-8">
       		    <title>Оценки</title>
    		</head>""")
    print("""
        <body>
            <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
            <h3>Выберите факультет и спецальность </h3>
            <table border="0" align="left"  cellpadding="5">
                <form action="/cgi-bin/marks_view_finish.py">
                    <tr>
                        <td>
                            <table border="1" align="left"  cellpadding="5">
                                <tr align="center" height="30px">
                                    <td width="300px">Факультет</td>
                                    <td width="300px">Специальность</td>
                                </tr>
                                <tr>
                                    <td>
                                        <select name="faculty">""")
    for f in faculties:
       print(                               "<option>" + f[0] + "</option>")
    print("""                           </select>
                		            </td>
                                    <td>
                                        <select name="specialty">""")
    for f in specialties:
       print(                               "<option>" + f[0] + "</option>")
    print("""                           </select>
                	            	</td>                	            	
                        	    </tr>
                        	</table>
              	        </td>
                    </tr>
                    <tr>
                        <td align="center">
                            <input type="submit" value="ПРОСМОТР И РЕДАКТИРОВАНИЕ ОЦЕНОК">
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <h4> </h4>
                         </td>
                    </tr> 
                </form>
            </table>                
        </body>
    </html>""")

main()