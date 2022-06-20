# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
KW = '''
<ScreenManagement>:
    MainScreen:
        name: "screen_main"

    MenuScreen:
        name: "screen_menu"


    CardScreen:
        name: "screen_card"

<MainScreen>:
    BoxLayout:
        id: layout
        size_hint: 1, None
        size: "280dp", "180dp"

        Button:
            text:"menu"
            font_size: 20
            on_press:root.manager.current = "screen_menu"

<MenuScreen>:
    BoxLayout:
        id: layout
        size_hint: 1, None
        size: "280dp", "120dp"

        Button:
            text:"Prato"
            font_size: 20
            on_press:root.s_card()

        Button:
            text:"Bebida"
            font_size: 20

        Button:
            text:"Mesa"
            font_size: 20

<CardScreen>:
    BoxLayout:
        id: layout
        size_hint: 1, None
        size: "720dp", "340dp"
        orientation:'vertical'
        '''
M = ['comercial', 'filé com fritas', 'feijoada', 'picanha a moda', 'picanha brasileira', 'trutas grelhadas']
card = ''
cString = '''
                     
        Button:
            font_size: 20
            size_hint: 1, .6
            text:'''
        
for i in M:
    card += cString+'"' + i+ '"'
KW += card 
endString = '''

        Button:
            font_size: 20
            size_hint: 1, .6
            text:"Início"
            on_press:root.manager.current = "screen_menu"'''
KW += endString
Builder.load_string( KW)
class MainScreen(Screen): 
        def init(self,kwargs):
            super(MainScreen,self).init(kwargs)
            pass

class MenuScreen(Screen):

        def s_card(self):
            print('mostrar cardápio')
            self.manager.current = 'screen_card'
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
       
class ScreenManagement(ScreenManager):
    pass

class tpWaiter(App):
        icon = 'mys3lf-light256.png'
        title = 'kWaiter'

        def build(self):
            return ScreenManagement()

if __name__ == '__main__':
    tpWaiter().run()
