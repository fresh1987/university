#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgitb
cgitb.enable()

from common_function import print_head, print_body_head

def main():


    print_head("Добавление")
    print_body_head("ВВЕДИТЕ ИНФОРМАЦИЮ О НОВОМ НАПРАВЛЕНИИ ПОДГОТОВКИ", "yes")


    print("""
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
       </body>
   </html>""")

main()