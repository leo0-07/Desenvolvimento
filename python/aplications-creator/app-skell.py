#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dStorage.core import dStorage
from tkinter import Tk, Button, Label, Listbox
import os
import configparser

class creator():
    def __init__(self):
            self.info = "pyCreator, aplicativo para construção de softwares."
            self.desc = "Este aplicativo utiliza a metaclasse dStorage para construção de interfaces, CLI, GUI e ambiente de dados."
            self.itype = 0
            self.db = ""
            self.tb = ""
            self.top = Tk
            self.Lb1 = Listbox
            self.Lbl1 = Label
                 
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


    def visualize(self):
        c = dStorage([], [])
        c.setdb(self.db, self.tb)
        c.l_pdindex()
        c.loaddata(self.Lb1.get(self.Lb1.curselection()))
        c.display()
        
    def consulta(self):
        c = dStorage([], [])
        c.setdb(self.db, self.tb)
        c.l_pdindex()
        print("testando consulta de dados no novo aplicativo...")
        if self.itype == 0:
            print("registros disponíveis")
            print(c.litems())
            r = input("registro a ser visualizado? ")
            c.loaddata(r)
            c.show()

        else:
            self.top = Tk()
            self.top.geometry('320x400')
            self.top.title(self.info)
            self.Lbl1 = Label(self.top, text="registros disponíveis:")
            self.Lb1 = Listbox(self.top)
            self.Btn1 = Button(self.top, text="visualizar", command=self.visualize)
            self.Btn2 = Button(self.top, text="remover", command=self.delete)
            '''c.display()'''
            for i in c.litems():
                c.loaddata(i[0])
                self.Lb1.insert(i[0], i[0])
            self.Lbl1.pack()
            self.Lb1.pack()
            self.Btn1.pack()
            self.Btn2.pack()
            self.top.mainloop()

    def delete(self):
        c = dStorage([], [])
        c.setdb(self.db, self.tb)
        c.l_pdindex()
        if self.itype == 0:
            print("registros disponíveis")
            print(c.litems())
            r = input("registro a ser removido?")
            c.deletedata(r)

        else:
            c.deletedata(self.Lb1.get(self.Lb1.curselection()))

        print("registro removido")
            
    def start(self):
        print("tipo de interface: ", self.itype)
        print("Este é: ", self.info)
        print("Bem vindo ao menu inicial!")
        print("1 - registrar, 2 - consultar, 3 - remover")
        e = input()
        print(e)
        if e == "1":
            print("cadastrar...")
            self.cadastro()

        if e == "2":
            print("consultar...")
            self.consulta()
            
        else:
            self.delete()

        exit("espero ter ajudado!")

    def appgui(self):
        self.top = Tk()
        self.top.geometry('360x400')
        self.top.title(self.info)
        self.Lb1 = Listbox(self.top)
        self.Btn1 = Button(self.top, text="cadastrar", command=self.cadastro)
        self.Btn2 = Button(self.top, text="consultar", command=self.consulta)
        self.Btn1.pack()
        self.Btn2.pack()
        self.top.mainloop()        


def main():
    config = configparser.ConfigParser()
    config.read('app-config')
    db = config.get('Aplicativo', 'DB')
    tb = config.get('Aplicativo', 'TB')
    print("base de dados: ", db)
    print("tabela:", tb)
    term = os.ttyname(0)
    print("terminal: ",term[5:8])
    if term[5:8] == "pts":
        itype = 1
        
    else:
        itype = 0
        
    print("tipo de interface:", itype)
    c = creator()
    c.info = "Meu aplicativo."
    c.tb = tb
    c.db = db
    c.itype = itype
    if itype == 1:
        c.appgui()
    else:
        c.start()
        
main()
