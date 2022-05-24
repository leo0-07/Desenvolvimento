#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import os
import sys
import pymysql

# class gui
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import  filedialog as fd
import os
class olbset(Tk):
    
    def __init__(self):
        os.system('echo "asl-lab (Academia do Software Livre)." &')
        super().__init__()
        super().geometry("480x520")
        self.ets = StringVar()
        self.nts = StringVar()
        self.desc = ""
        self.pchave = ""
        self.file_path = ""
        self.fcontent = ""
        self.title("Cadastro de anotações")
        self.leTitle = Label(self, text='Anotações existentes')
        self.len = Listbox(self, background="white", height=10, listvariable=self.ets)
        self.lnTitle = Label(self, text='Novas anotações')
        self.adTitle = Label(self, text='Descrição')
        self.lnn = Listbox(self, background="white", height=5, listvariable=self.nts)
        self.inputdesc = Text(self, background="white", height = 8,  width = 50)
        self.bbtn = Button(self, text=" Salvar", command=self.save_n)
        self.cbtn = Button(self, text=" Criar", command=self.create_n)
        self.sbtn = Button(self, text=" Salvar", command=self.save_n)
        self.abtn = Button(self, text=" Anexar conteúdo", command=self.add_c)
        self.adTitle.place(x=78,y=226)
        self.inputdesc.place(x=42, y=256)
        self.cbtn.place(x=84, y=420)
        self.sbtn.place(x=160, y=420)
        self.abtn.place(x=240, y=420)
        self.leTitle.place(x=64, y=14)
        self.len.place(x=48, y=36)
        self.len.bind('<Double-1>',self.s_ents)
        self.lnTitle.place(x=294, y=14)
        self.lnn.place(x=250, y=36)
        self.l_nts()


    def create_n(self):
        self.inputdesc.delete(1.0,END)
        self.pchave = simpledialog.askstring(title="Cadastro de anotação", prompt="Palavra chave a ser cadastrada?")
        self.lnn.insert(END, self.pchave)
        pass

    def save_n(self):
            self.desc = self.inputdesc.get("1.0",END)
            print(self.desc)
            con = pymysql.connect(host="asl-sl.com.br", user="waiter", password="11224477", db="asldb")
            print('connectado!\n')
            cur = con.cursor()
            sql = "INSERT INTO notas (pchave, descrição, conteúdo) VALUES ('"+self.pchave+"','"+self.desc+"', '"+self.fcontent+"')"
            print(sql)
            cur.execute(sql)
            con.commit()
            cur.close()
            con.close()
            messagebox.showinfo(title="informação",message="registro adicionado")
            print('desconectado!\n')
            pass

    def add_c(self):
        self.file_path = fd.askopenfilename()
        self.desc = self.inputdesc.get("1.0",END)
        with open(self.file_path, 'r') as file:
            self.fcontent = file.read().replace('\n', '')
            
        self.txtwnd = Toplevel(self)
        self.txtwnd.title("conteúdo a ser adicionado")
        self.txtwnd.geometry("640x480")
        self.txtcbox = Text(self.txtwnd, background="white")
        self.txtcbox.grid(row=1, column=0, columnspan=4, sticky=W+E)
        self.txtcbox.insert(END, self.fcontent)
        
        pass


    def desc(self):
        
        pass

    def l_nts(self):
            con = pymysql.connect(host="asl-sl.com.br", user="waiter", password="11224477", db="asldb")
            print('connectado!\n')
            cur = con.cursor()
            cur.execute("select pchave from notas")
#           print(cur.description)
            for row in cur:
                self.len.insert(END, row)
                
            cur.close()
            con.close()
            print('desconectado!\n')
    pass


    def s_ents(self, evt):
            con = pymysql.connect(host="asl-sl.com.br", user="waiter", password="11224477", db="asldb")
            print('connectado!\n')
            cur = con.cursor()
            #
            selection = evt.widget.curselection()
            index = selection[0]
            value = evt.widget.get(index)
            #
            sql = "select descrição from notas where pchave='"  + value[0] + "'"
#           print(sql)
            self.inputdesc.delete(1.0,END)
            cur.execute(sql)
#           print(cur.description)
            for row in cur:
                self.inputdesc.insert(END,row)
                
            cur.close()
            con.close()
            print('desconectado!\n')
            
    pass
        


# main application function...

def main():
    
    gui() 

# graphic interface build...

def gui():
    my_gui = olbset()
    my_gui.mainloop()
        

if __name__ == "__main__":
    main()
