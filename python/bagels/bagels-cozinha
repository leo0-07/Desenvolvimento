#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import os
import sys
import pymysql
from datetime import datetime
import sched, time

def test(sc):
        os.system('clear')
        print(datetime.now())
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

        con.close()
        s.enter(1, 1, test, (sc,))

s = sched.scheduler(time.time, time.sleep)    

s.enter(1, 1, test, (s,))
s.run()
