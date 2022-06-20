import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
items = [
    {"color":(1, 1, 1, 1), "font_size": "20sp", "text": "salada",     "input_data": 1},
    {"color":(.5,1, 1, 1), "font_size": "20sp", "text": "comercial", "input_data": 2},
    {"color":(.5,.5,1, 1), "font_size": "20sp", "text": "picanha",      "input_data": 3},
    {"color":(.5,.5,.5,1), "font_size": "20sp", "text": "feijoada",      "input_data": 4},
    {"color":(1,.5,.5, 1), "font_size": "20sp", "text": "churrasco",    "input_data": 5},
    {"color":(1, 1,.5, 1), "font_size": "20sp", "text": "prato feito",    "input_data": 6}
]

Builder.load_string( '''
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
            on_press:root.s_menu()

<MenuScreen>:
    BoxLayout:
        id: layout
        size_hint: 1, None
        size: "280dp", "120dp"

        Button:
            text:"Prato"
            on_press:root.s_card()

        Button:
            text:"Bebida"

        Button:
            text:"Mesa"

<CardScreen>:
    BoxLayout:
        id: layout
        size_hint: 1, None
        size: "280dp", "180dp"
        orientation:'vertical'

        Button:
            font_size:16
            text:"comercial"
            
        Button:
            font_size:16
            text:"picanha a brasileira"
            
        Button:
            font_size:16
            text:"churrasco"
            
             
        Button:
            font_size:16
            text:"feijoada completa"
            
        
        ''')
     
class MainScreen(Screen):

        def s_menu(self):
            print('mostrar menu')
            self.manager.current = 'screen_menu'
            pass
        
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

class ScreenManagement(ScreenManager):
    pass

class tpWaiter(App):
        icon = 'mys3lf-light256.png'
        title = 'kWaiter'

        def build(self):
            return ScreenManagement()

if __name__ == '__main__':
    tpWaiter().run()
