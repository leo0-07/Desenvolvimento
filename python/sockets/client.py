# Echo client program
#!/usr/bin/env python
# encoding: utf-8
import os
import sys
from tkinter import *
import socket

HOST = '192.168.1.101'    # The remote host
PORT = 7777              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
sdata='Olá mundo!'
s.sendall(sdata.encode("utf-8"))
msg = "Dados enviados ao servidor", repr(sdata)
rdata = s.recv(1024)
s.close()
msg2=  'Dados recebidos do servidor', repr(rdata.decode("utf-8"))
wnd = Tk()
lblmsg = Label(wnd,text=msg)
lblmsg2 = Label(wnd,text = msg2)
lblmsg.pack()
lblmsg2.pack()
wnd.mainloop()
