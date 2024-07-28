from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        self.names = ["Alice", "Bob", "Charlie", "Diana"]  # List of names
        root = self.root
        main_layout = root.ids.main

        # Create a Label for each name in the list and add it to the main_layout
        for name in self.names:
            label = Label(text=name)
            main_layout.add_widget(label)

        return root


DynamicLabelsApp().run()
