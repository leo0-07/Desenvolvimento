#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import Tk, Text, Button
import os
import sys
import pymysql
from datetime import datetime
import time
## Server: asl-sl.com.br
## DB: asldb
## id: waiter
## passwd: 11224477
fim = False

def sair():
        fim = True
        exit(0)
        dwin.destroy()

dwin = Tk()
dwin.resizable(False, False)
dwin.title("bagels")

#        os.system('clear')
        
def atualiza():
        dwin.txt.delete("1.0", "end")
        con = pymysql.connect(
                host='asl-sl.com.br',
            user='waiter', 
            password = "11224477",
            db='asldb',
            )
        
        with    con.cursor() as cur:
            cur.execute('select * from pedidos')
            lptos = cur.fetchall()

            for  rst in lptos:
                    print(rst[1])
                    dwin.txt.insert('1.0',rst[1])

        con.close()
        dwin.txt.after(1000, atualiza)

dwin.txt = Text(dwin, width=28, height=15)
dwin.btns = Button(dwin, text="sair", command=sair)
dwin.txt.pack()
dwin.btns.pack()

atualiza()
dwin.mainloop()



