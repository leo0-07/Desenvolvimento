
from datetime import datetime
import pymysql
from datetime import datetime
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
plist = []
blist = []
mlist = []
con = pymysql.connect(
        host='asl-sl.com.br',
        user='waiter', 
        password = "11224477",
        db='asldb',
        )
with con.cursor() as cur:
    cur.execute('select prato from pratos')
    lptos = cur.fetchall()
    for  rst in lptos:
        plist.append(rst[0])
        print(rst[0])


with con.cursor() as cur:
    cur.execute('select bebida from bebidas')
    lpbeb = cur.fetchall()
    for rst in lpbeb:
        blist.append(rst[0])
        print(rst[0])
        

with con.cursor() as cur:
    cur.execute('select num from mesas')
    lpmes = cur.fetchall()
    for rst in lpmes:
        mlist.append(rst[0])
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
    MesaScreen:
        name: "screen_mesa"
        id:scrbeb
    

<MainScreen>:
    BoxLayout:
        orientation:'vertical'
        size_hint: 1, None
        size: "800dp", "600dp"

        Button:
            text:"início"
            font_size: 20
            on_press:pedido = root.start(app.pedido)

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
            on_press:root.s_mesa()

        Button:
            text:"Enviar"
            font_size: 20
            on_press:root.epedido(app.pedido)

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
    beb += cString+'"' + b + '"'
KW += beb + '''

        Button:
            font_size: 20
            size_hint: 1, .8
            text:"Voltar"
            on_press:root.manager.current = "screen_menu"

<MesaScreen>:
    BoxLayout:
        orientation:'vertical'
        '''
mesa = ''
cString = '''
                     
        Button:
            font_size: 20
            size_hint: 1, .8
            on_press:app.hpedido(self)
            text:'''
for m in mlist:
    mesa += cString+'" Mesa :--> ' + str(m) + '"'
KW += mesa + ''
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

        def start(self, comanda):
            comanda.clear()
            self.manager.current = 'screen_menu'
            comanda.clear()


class MenuScreen(Screen):
        
        def s_card(self):
            '''print('mostrar cardápio')'''
            self.manager.current = 'screen_card'
            pass

        def s_beb(self):
            self.manager.current = 'screen_drinks'
            pass
        
        def s_mesa(self):
            self.manager.current = 'screen_mesa'
            pass

        def spedido(self, instance):
            print(self.msgpop)
            con = pymysql.connect(
                host='asl-sl.com.br',
                user='waiter',
                password = "11224477",
                db='asldb',
                )
            with con.cursor() as cur:
                sql = 'insert into pedidos (pedido) values (%s)'
                cur.execute(sql, (self.msgpop))
                lptos = con.commit()
                con.close()
                
            instance.parent.parent.parent.parent.dismiss()
            self.manager.current = 'screen_main'
            pass

        def epedido(self, comanda):
            con = pymysql.connect(
                host='asl-sl.com.br',
                user='waiter',
                password = "11224477",
                db='asldb',
                )
            with con.cursor() as cur:
                cur.execute('select max(id) from pedidos')
                lptos = cur.fetchall()
                num_p = lptos[0]
                con.close()
                pnum = num_p[0]
                if pnum is None:
                    pnum = 1
                    
                nped = "número do pedido: " + str(pnum)
                if len(comanda) > 0:
                    self.msgpop = ""
                    self.msgpop += nped + "\n"
                    tempo = datetime.now()
                    ptime = tempo.strftime("%H:%M:%S")
                    self.msgpop += ptime + "\n"
                    for i in comanda:
                        self.msgpop += i + "\n"

                    self.lblpedido = Label(text=str(self.msgpop))
                    self.btnpedido = Button(text='Enviar')
                    self.btnpedido.bind(on_press=self.spedido)
                    self.boxpedido =  BoxLayout(padding=10)
                    self.boxpedido.add_widget(self.lblpedido)
                    self.boxpedido.add_widget(self.btnpedido)
                    self.popup = Popup(content=self.boxpedido, auto_dismiss=False)
                    self.popup.open()
                    
                else:
                    self.manager.current = 'screen_main'
                    
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

class MesaScreen(Screen):
        def init(self,kwargs):
            super(MenuScreen,self).init(kwargs)
            print('mesa init')
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
            instance.parent.parent.manager.current ='screen_menu'

        def build(self):
            return ScreenManagement()

if __name__ == '__main__':
    tpWaiter().run()
