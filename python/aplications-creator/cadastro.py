#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dStorage.core import dStorage

tb = "equipe"
db = "info"
c = dStorage([], [])
c.setdb(db, tb)
c.l_pdindex()
print(c.pindex)
c.registrar()
c.show()
t = input("salvar registro? (s/n) ")
if t == "s":
    c.savedata()
    print("dados armazenados...")


