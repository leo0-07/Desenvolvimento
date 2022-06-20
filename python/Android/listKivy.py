from kivy.uix.modalview import ModalView
from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.factory import Factory

Builder.load_string("""
#:import lv kivy.uix.listview
#:import la kivy.adapters.listadapter
<ListViewModal>:
    list_view: list_view_id
    size_hint: None,None
    size: 400,400
    ListView:
        id: list_view_id
        size_hint: .8,.8
        adapter:
            la.ListAdapter(
            data=["Item #{0}".format(i) for i in xrange(100)],
            selection_mode='single',
            allow_empty_selection=False,
            cls=lv.ListItemButton)
""")

class ListViewModal(ModalView):
    selected_item = StringProperty('no selection')
    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)
        self.list_view.adapter.bind(on_selection_change=self.selection_changed)

    def selection_changed(self, *args):
        print('    args when selection changes gets you the adapter', args)
        self.selected_item = args[0].selection[0].text


    def on_selected_item(self, *args):
        print ('    args when selection changes gets you the adapter')
        self.selected_item = args[0].selection[0].text


class MainView(GridLayout):
    """
    Implementation of a ListView using the kv language.
    """

    def __init__(self, **kwargs):
        kwargs['cols'] = 1
        kwargs['size_hint'] = (1.0, 1.0)
        super(MainView, self).__init__(**kwargs)

        listview_modal = ListViewModal()

        self.add_widget(listview_modal)


if __name__ == '__main__':
    from kivy.base import runTouchApp
    runTouchApp(MainView(width=800))
