import kivy
from tkinter import *
from tkinter.ttk import *
import pymysql
class Root(Tk):
     def __init__(self):
        super().__init__()
        self.display_text = StringVar()
        self.app_title = StringVar()
        self.mtext = StringVar()
        self.ptext = StringVar()
        self.btext = StringVar()
        self.msg = StringVar()
        
        self.app_title.set('Paçoquinha - Waiter')
        self.display_text.set('pedido')
        self.mtext.set('Mesa:')
        self.ptext.set('Prato:')
        self.btext.set('Bebida:')
        self.title = Label(self, textvariable=self.app_title)
        self.label = Label(self, textvariable=self.display_text)
        self.llm = Label(self, textvariable=self.mtext)
        self.llb = Label(self, textvariable=self.btext)
        self.llp = Label(self, textvariable=self.ptext)
        self.lmsg = Label(self, textvariable=self.msg)
        self.title.grid(row=22, column=10)
        self.label.grid(row=23, column=10)
        self.cPrato= Combobox(self)
        self.cPrato['values']=('comercial','picanha completa','feijoada')
        self.cBebida= Combobox(self)
        self.cBebida['values']=('suco','refrigerante','cerveja')
        self.cMesa= Combobox(self)
        self.cMesa['values']=('1','2','3','4')
        self.btnOk = Button(self, text='enviar', command=self.show)
        self.llp.grid(row=24, column=10)
        self.cPrato.grid(row=25, column=10)
        self.llb.grid(row=26, column=10)
        self.cBebida.grid(row=27, column=10)
        self.llm.grid(row=28, column=10)
        self.cMesa.grid(row=29,  column=10)
        self.btnOk.grid(row=30,   column=10)
        self.lmsg.grid(row=31, column=10)
     
     def show(self):
        	self.mpedido = self.cMesa.get()
        	self.display_text.set('pedido mesa: '+ self.mpedido+ ' realizado.')
        	self.query()
        	
     def query(self):
        	self.dbcon = pymysql.connect(host='db.asl-sl.com.br', user='leo0-07', password='linux77', db='asldb')
        	self.msg.set('conectado')
        	self.dbcon.close()
        	
root = Root()
root.mainloop()
