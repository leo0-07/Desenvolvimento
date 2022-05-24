#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import os
import sys
import pymysql
from datetime import datetime
import time
## Server: my db server
## DB: db
## id: login
## passwd: password


def test():
        os.system('clear')
        print(datetime.now())
        con = pymysql.connect(
            host='xxxxxxxxx',
            user='xxxx', 
            password = "xxxxx",
            db='xxxxx',
            )
        with    con.cursor() as cur:
            cur.execute('select * from pedidos')
            lptos = cur.fetchall()

            for  rst in lptos:
                print(rst[1])

        con.close()
        time.sleep(5)
opt = ""
while opt == opt:
        test()
                
quit(0)
