import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MyGrid(Widget):
    pass


class test3App(App): # <- Main Class
    def build(self):
        dat = [ ]
        for l in ["comercial", "feijoada", "picanha"]:
            dat.insert(0,{'item':l})

        self.rv.data = dat
        return MyGrid()

    def btn(self):
        print('botão pressionado!')


if __name__ == "__main__":
    test3App().run()
