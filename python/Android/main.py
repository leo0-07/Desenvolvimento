from datetime import datetime
import pymysql
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button
plist = []
mlist = [1, 2, 3, 4, 5, 6, 7, 8]
blist = ['suco','refrigerante','cerveja','vinho','caipirinha']
con = pymysql.connect('db.asl-sl.com.br', 'leo0-07', 'linux77', 'asldb')
with con.cursor() as cur:
    cur.execute('select prato from pratos')
    lptos = cur.fetchall()
    for  rst in lptos:
        plist.append(rst[0])
        print(rst[0])

    con.close()
KW = '''
<ScreenManagement>:
    MainScreen:
        name: "screen_main"
        id:scrmain

    MenuScreen:
        name: "screen_menu"
        id:scrmenu

    CardScreen:
        name: "screen_card"
        id:scrcard

    BebScreen:
        name: "screen_drinks"
        id:scrbeb
    

<MainScreen>:
    BoxLayout:
        orientation:'vertical'
        size_hint: 1, None
        size: "800dp", "600dp"

        Button:
            text:"início"
            font_size: 20
            on_press:pedido = root.start()
            
        Button:
            text:"efetuar pedido"
            font_size: 20
            on_press:root.epedido(app.pedido)

<MenuScreen>:
    BoxLayout:
        size: "140dp", "60dp"

        Button:
            text:"Prato"
            font_size: 20
            on_press:root.s_card()

        Button:
            text:"Bebida"
            font_size: 20
            on_press:root.s_beb()

        Button:
            text:"Mesa"
            font_size: 20

        Button:
            text:"Encerrar"
            font_size: 20
            on_press:root.manager.current = "screen_main"

<CardScreen>:
    BoxLayout:
        orientation:'vertical'
        '''

card = ''
cString = '''
                     
        Button:
            font_size: 20
            size_hint: 1, .8
            on_press:app.hpedido(self)
            text:'''
for p in plist:
    card += cString+'"' + p+ '"'
KW += card + '''

        Button:
            font_size: 20
            size_hint: 1, .8
            text:"Voltar"
            on_press:root.manager.current = "screen_menu"

<BebScreen>:
    BoxLayout:
        orientation:'vertical'
        '''
beb = ''
cString = '''
                     
        Button:
            font_size: 20
            size_hint: 1, .8
            on_press:app.hpedido(self)
            text:'''
for b in blist:
    beb += cString+'"' + b+ '"'
KW += beb
endString = '''

        Button:
            font_size: 20
            size_hint: 1, .8
            text:"Voltar"
            on_press:root.manager.current = "screen_menu"'''

KW += endString
Builder.load_string( KW)
class MainScreen(Screen):
    
        def init(self,kwargs):
            super(MainScreen,self).init(kwargs)
            pedido = []
            pass

        def start(self):
            self.manager.current = 'screen_menu'

        def epedido(self, comanda):
            print('Enviando pedido!')
            for i in comanda:
                print(i)

            comanda.clear()

class MenuScreen(Screen):

        def s_card(self):
            '''print('mostrar cardápio')'''
            self.manager.current = 'screen_card'
            pass

        def s_beb(self):
            self.manager.current = 'screen_drinks'
            pass
        
        def init(self,kwargs):
                super(MenuScreen,self).init(kwargs)
                pass


class CardScreen(Screen):                

        def init(self,kwargs):
            super(MenuScreen,self).init(kwargs)
            pass

        def s_menu(self):
            print('mostrar menu')
            self.manager.current = 'screen_menu'
            pass

class BebScreen(Screen):
        def init(self,kwargs):
            super(MenuScreen,self).init(kwargs)
            print('beb init')
            pass
        def s_menu(self):
            print('mostrar menu')
            self.manager.current = 'screen_menu'
            pass


class ScreenManagement(ScreenManager):
    pass

class tpWaiter(App):
        pedido = []
        icon = 'mys3lf-light256.png'
        title = 'kWaiter'
        
        def hpedido(self, instance):
            '''print(instance.text)'''
            self.pedido.append(instance.text)

        def build(self):
            return ScreenManagement()

if __name__ == '__main__':
    tpWaiter().run()
