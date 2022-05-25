#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dStorage.core import dStorage
import os

class creator():
    def __init__(self):
            self.info = "pyCreator, aplicativo para construção de softwares."
            self.desc = "Este aplicativo utiliza a metaclasse dStorage para construção de interfaces, CLI, GUI e ambiente de dados."
            self.itype = 0
            self.db = ""
            self.tb = ""
                 
    def cadastro(self):
        c = dStorage([], [])
        c.setdb(self.db, self.tb)
        c.l_pdindex()
        print(c.pindex)
        print("testando registro de dados no novo aplicativo...")
        print("tipo de interface", self.itype)
        if self.itype == 1:
            c.cad()

        else:
            c.registrar()
            c.show()
            t = input("salvar registro? (s/n) ")
            if t == "s":
                c.savedata()

        print("dados armazenados...")

    def consulta(self):
        c = dStorage([], [])
        c.setdb(self.db, self.tb)
        c.l_pdindex()
        print("testando consulta de dados no novo aplicativo...")
        print("registros disponíveis")
        print(c.litems())
        r = input("registro a ser visualizado? ")
        c.loaddata(r)
        if self.itype == 0:
            c.show()

        else:
            c.display()
            
    def start(self):
        print("tipo de interface: ", self.itype)
        print("Este é: ", self.info)
        print("Bem vindo ao menu inicial!")
        print("1 - registrar, 2 - consultar")
        e = input()
        print(e)
        if e == "1":
            print("cadastrar...")
            self.cadastro()
            exit("espero ter ajudado!")

        if e == "2":
            print("consultar...")
            self.consulta()
            exit("espero ter ajudado!")
            
        else:
            exit("espero ter ajudado!")

def main():
    tb = "equipe"
    db = "info"
    term = os.ttyname(0)
    print("terminal: ",term[5:8])
    if term[5:8] == "pts":
        itype = 1
    else:
        itype = 0
        
    print("tipo de interface:", itype)
    c = creator()
    c.info = "Meu aplicativo."
    print("base de dados: ", db)
    c.tb = tb
    c.db = db
    c.itype = itype
    c.start()
    
main()
