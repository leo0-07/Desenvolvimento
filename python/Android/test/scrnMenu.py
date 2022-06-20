from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


items = [
    {"color":(1, 1, 1, 1), "font_size": "20sp", "text": "salada",     "input_data": 1},
    {"color":(.5,1, 1, 1), "font_size": "20sp", "text": "comercial", "input_data": 2},
    {"color":(.5,.5,1, 1), "font_size": "20sp", "text": "picanha",      "input_data": 3},
    {"color":(.5,.5,.5,1), "font_size": "20sp", "text": "feijoada",      "input_data": 4},
    {"color":(1,.5,.5, 1), "font_size": "20sp", "text": "churrasco",    "input_data": 5},
    {"color":(1, 1,.5, 1), "font_size": "20sp", "text": "prato feito",    "input_data": 6}
]


class MyButton(Button):

    def print_data(self,data):
        print(data)

KV = '''
<pButton>:
    on_release:
        root.spedido()

<MyButton>:
    on_release:
        root.print_data(self.input_data)

RecycleView:
    data: []
    viewclass: 'MyButton'
    RecycleBoxLayout:
        default_size_hint: 1, None
        orientation: 'vertical'


'''


class Test(App):
    def build(self):
        root = Builder.load_string(KV)
        root.data = [item for item in items]
        return root


Test.title = 'pWaiter'
Test().run()
