from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class Alert(Popup):

    def __init__(self, title, text):
        super(Alert, self).__init__()

        content = AnchorLayout(anchor_x='center', anchor_y='bottom')
        content.add_widget(
            Label(text=text, halign='left', valign='top')
        )
        ok_button = Button(text='Go Back', size=(Window.width / 12, Window.height / 12), size_hint=(None, None))
        content.add_widget(ok_button)

        popup = Popup(
            title=title,
            content=content,
            size_hint=(None, None),
            size=(Window.width / 2, Window.height / 2),
            auto_dismiss=True,
        )
        ok_button.bind(on_press=popup.dismiss)
        popup.open()