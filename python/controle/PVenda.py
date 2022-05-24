#!/usr/bin/env python3
import os, sys
from dStorage import *
from Person import *
import tkinter as tk
from random import *
class Venda:
    def __init__(self):
        self.Info=dStorage(("0","Venda","Produto","0","Envelope","12/06/2018","20/06/2018","100,00"),("id","categoria","tipo","id_cliente","nome", "data", "recebimento","valor"))
        self.Info.setdb("Dados","Vendas")
        self.Info.l_pdindex()
        self.cli = Person
        self.wnd = tk.Tk()
        self.wnd.geometry("320x280")
        self.wnd.configure(background="blue")
        self.lstitems = tk.Listbox(self.wnd, background="white")
        self.gui()



    def cdBase(self):
            self.Info.cdBase()



    def saveinit(self):
            self.Info.savedata()


    def cadastra(self):
        self.Info.cad()
    # realizar consulta ao id ou e cadastro e consulta ao id do cliente.


    def display(self):
        work = dStorage((),())
        work.setdb("Dados","Vendas")
        work.l_pdindex()
        selection = self.lstitems.get(ACTIVE)
        reg =str(selection[0])
        print ("registro:",reg)
        rid = self.Info.getid(reg)
        print("id reg:",rid[0])
        self.Info.loaddata(rid[0])
        self.Info.display()

    def gui(self):
        self.wnd.title("Vendas")
        self.wnd.configure(background="blue")
        btncad = tk.Button(self.wnd,text="cadastra", command=self.cadastra)
        btnd = tk.Button(self.wnd, text="visualizar Informações", command=self.display)
        btnexit = tk.Button(self.wnd, text="sair", command=self.wnd.destroy)
        lblitems = tk.Label(self.wnd)
        self.lstitems.configure(background="white")
        self.lstitems.grid(row=0,column=0)
        btncad.grid(row=2,column=0)
        btnd.grid(row=3, column=0)
        btnexit.grid(row=4, column=0)
        self.updtl()

    def updtl(self):
        lista = self.Info.lnames(4)
        for item in lista:
            self.lstitems.insert(END, item)
