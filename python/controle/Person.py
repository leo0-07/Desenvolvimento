#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
from dStorage import *
import tkinter as tk
from random import *
class Person:
    def __init__(self):
        self.Info = dStorage((),())
        self.Address = dStorage((),())
        wnd =tk.Tk()
        wnd.title("Clientes")
        wnd.configure(background='blue')
        self.lstid = tk.Listbox(wnd, background="white")
        self.Info.setdb("pessoas","pessoas")
        self.Address.setdb("Address","Address")
        self.Info.l_pdindex()
        self.Address.l_pdindex()
        btncli = tk.Button(wnd, text="cadastra informações",command=self.caddata)
        btncli.grid(row=4,column=1)
        btnend = tk.Button(wnd, text="cadastra endereço",command=self.cadend)
        btnend.grid(row=5, column=1)
        btnvcli = tk.Button(wnd, text="visualiza informações",command=self.display)
        btnvend = tk.Button(wnd,text="visualiza endereço", command=self.dend)
        btnvcli.grid(row=4, column=0)
        btnvend.grid(row=5, column=0)
        btnsalt = tk.Button(wnd,text="salvar alterações", command=self.save)
        btnsalt.grid(row=6, column=0)
        btnexit = tk.Button(wnd, text="sair",command=wnd.destroy)
        btnexit.grid(row=6, column=1)
        self.lstid.grid(row=0, column=1)
        self.lstid.bind('<Double-1>',self.dbclick)
        self.updtl()
        wnd.mainloop()

    def display(self):
        pessoa = dStorage((),())
        pessoa.setdb("pessoas","pessoas")
        pessoa.l_pdindex()
        selection =self.lstid.get(ACTIVE)
        reg = str(selection[0])
        rid = self.Info.getid(reg)
        print (rid[0])
        print (rid[0])
        self.Info.loaddata(rid[0])
        pessoa.loaddata(rid[0])
        pessoa.display()


    def dend(self):
        end = dStorage((),())
        end.setdb("Address","Address")
        end.l_pdindex()
        selection =self.lstid.get(ACTIVE)
        reg = str(selection[0])
        rid = self.Info.getid(reg)
        print (rid[0])
        end.loaddata(rid[0])
        end.display()



    def dbclick(self, event):
        pessoa = dStorage((),())
        end = dStorage((),())
        pessoa.setdb("pessoas","pessoas")
        pessoa.l_pdindex()
        end.setdb("Address","Address")
        end.l_pdindex()
        selection =self.lstid.get(ACTIVE)
        reg = str(selection[0])
        rid = pessoa.getid(reg)
        print (rid[0])
        print (rid[0])
        pessoa.loaddata(rid[0])
        end.loaddata(rid[0])
        self.Info = pessoa
        self.Address = end
       #self.show()

    def show(self):
        self.Info.show()
        self.Address.show()
        
    def save(self):
        self.Info.savedata("pessoas")
        self.Address.savedata("Address")

    def load(self, reg):
        self.Info.loaddata(reg)
        self.Address.loaddata(reg)
        

    def caddata(self):
        self.Info.cad()


    def cadend(self):
        self.Address.cad()

    def updtl(self):
        lista = self.Info.lnames(1)
        for item in lista:
            self.lstid.insert(END, item)

        self.lstid.update_idletasks()
            



