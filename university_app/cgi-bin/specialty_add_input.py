#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import psycopg2

import cgitb
cgitb.enable()

def main():
    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
	    	<html lang="en">
		    <head>
    		    <!-- Meta Tag -->
	    	    <meta charset="UTF-8">
       		    <title>Добавление</title>
    		</head>""")
    print("""
        <body>
            <h2>ГЛАВНЫЙ УНИВЕРСИТЕТ</h2>
            <h3>ВВЕДИТЕ ИНФОРМАЦИЮ О НОВОМ НАПРАВЛЕНИИ ПОДГОТОВКИ</h3>
            <form action="/cgi-bin/specialty_add_finish.py">
                <table>
                    <tr>
                        <td>Факультет</td>
                        <td>Специальность</td>
                    </tr>
                    <tr>
                        <td>
                           <input type="text" name="faculty">
                        </td>
                        <td>
                            <input type="text" name="specialty">
                        </td>
                    </tr>
                </table>
                <p><input type="submit" value="Добавить запись"> </p>
            </form>
                
            <form action="/index.html">
                <p><input type="submit" value="НА ГЛАВНУЮ"> </p>
            </form>
       </body>
   </html>""")

main()