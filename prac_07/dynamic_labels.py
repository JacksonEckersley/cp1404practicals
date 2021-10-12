
from kivy.app import App
from kivy.lang import Builder
import kivy.uix.label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.names = {"Bob Brown", "Cat Cyan", "Oren Ochre"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = kivy.uix.label.Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
