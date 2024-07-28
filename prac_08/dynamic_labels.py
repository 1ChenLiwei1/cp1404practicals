from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

NEW_COLOUR = (1, 5, 7, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)  # RGBA for magenta


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self):
        super().__init__()
        self.names = ["Alice", "Bob", "Jon", "Diana", "Eve", "Fred", "Ginny"]

    def build(self):
        self.title = "Dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.color = (1, 0.75, 0.8, 1)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
