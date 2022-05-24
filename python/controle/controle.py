#!/usr/bin/env python3
import os, sys
from dStorage import *
from Person import *
from Produto import *
from PServiços import *
from PVenda import *
import tkinter as tk
from PIL import ImageTk
from random import *
class controle:

        def cli(self):
            dadu= Person()

        def prod(self):
              roupa = Produto()

        def serviço(self):
                      serviço = Serviço()

        def venda(self):
                    venda = Venda()
                    venda.cdBase()

        def __init__(self):
                file = sys.argv[0]
                pathname = os.path.dirname(file)
                print ('running from %s' % os.path.abspath(pathname))
                print ('file is %s' % file)
                rwin = tk.Tk()
                rwin.title("Controle comercial v1.0a")
                rwin.config(width=750, height=160)
                bcli = ImageTk.PhotoImage(file=(str(os.path.abspath(pathname)))+"/cliumg.gif")
                bquit = ImageTk.PhotoImage(file=(str(os.path.abspath(pathname)))+"/quit.gif")
                bprod = ImageTk.PhotoImage(file=(str(os.path.abspath(pathname)))+"/produtos.gif")
                btncli=tk.Button(rwin,image=bcli,height=124, width=124, command=self.cli)
                btnprod = tk.Button(rwin, image=bprod,height= 124, width=124,  command=self.prod)
                bserviço = ImageTk.PhotoImage(file=(str(os.path.abspath(pathname)))+"/serviço.jpeg")
                btnserviço = tk.Button(rwin, image=bserviço, height =124, width = 124, command = self.serviço)
                bvenda = ImageTk.PhotoImage(file=(str(os.path.abspath(pathname)))+"/venda.jpeg")
                btnvenda = tk.Button(rwin, image = bvenda, height = 124, width = 124, command = self.venda)
                btnquit = tk.Button(rwin, image=bquit, height = 124, width= 124, command=rwin.destroy)
                btncli.grid(row=0, column=0)
                btnprod.grid(row=0,column=1)
                btnserviço.grid(row=0, column=2)
                btnvenda.grid(row=0, column=3)                            
                btnquit.grid(row=0, column=4)
                rwin.config(background="blue")
                rwin.mainloop()



c = controle()

                                            
