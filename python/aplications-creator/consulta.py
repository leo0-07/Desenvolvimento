#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dStorage.core import dStorage

tb = "equipe"
db = "info"
c = dStorage([], [])
c.setdb(db, tb)
c.l_pdindex()
print("registros disponíveis")
print(c.litems())
r = input("registro a ser visualizado? ")
c.loaddata(r)
c.show()
