from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    md_bg_color: 1, 1, 1, 1  # Set background color to white

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            id: label
            text: "Hello"
            halign: "center"
            theme_text_color: "Primary"

        Button:
            text: "Change Text"
            pos_hint: {"center_x": 0.5}
            on_release: app.change_text()
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def change_text(self):
        label = self.root.ids.label
        if label.text == "Hello":
            label.text = "World"
        else:
            label.text = "Hello"

MyApp().run()
