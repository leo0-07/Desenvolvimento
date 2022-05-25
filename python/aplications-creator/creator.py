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
          
    def start(self):
        print("tipo de interface: ", self.itype)
        self.tmpi = []
        self.tmpd = []
        print("Adicionando propriedades a nova classe.")
        print("Lembre de adicionar o indexador como propriedade inicial (id).")        
        print("Quantas propriedades serão adicionadas?")
        np = input()
        for i in range(int(np)):
            print("entre com o nome da propriedade dados ", i)
            data = input()
            if data > "":
                 self.tmpi.append(data)

            for a in range(len(self.tmpi)-1):
                tmpv = "info-",self.tmpi[a]
                self.tmpd.append(tmpv)
                
        print("lista de propriedades da classe a ser gerada:", self.tmpi)
        print("número de propriedades da classe:", len(self.tmpi))
        print("nome da base de dados a ser criada? ")
        self.db = input()
        self.tb = input("nome da tabela de dados? ")

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

    def construct(self):
        t = input("criar aplicativo (s/n)")
        if t == "s":
            print("Constrindo aplicativo...")
            self.cadastro()
            self.consulta()
            print("Aplicativo criado com sucesso!")

    def create(self):
        print("criando classe,  banco de dados SQLITE associado com propriedades de dados da nova classe.")
        print("propriedades:", self.tmpi)
        print("valores iniciais:", self.tmpd)
        myClass = dStorage(self.tmpd, self.tmpi)
        print("classe criada com sucesso!")
        print(myClass.pindex)
        print("banco de dados: "+self.db+" e tabela: "+self.tb+" serão criados.")
        t = input("realmente construir? (s/n)")
        if t == "s":
            myClass.setdb(self.db, self.tb)
            myClass.cdBase()
            print("base de dados criada!")

    def checkenv(self):
        '''
        print("Terminal device associated with:")
        print("Standard input:", os.ttyname(0))
        print("Standard output:", os.ttyname(1))
        '''
            
    
def main():
    term = os.ttyname(0)
    print("terminal: ",term[5:8])
    if term[5:8] == "pts":
        itype = 1
    else:
        itype = 0

    print("tipo de interface:", itype)
    c = creator()
    c.itype = itype
    c.start()
    c.create()
    c.construct()
    
main()
