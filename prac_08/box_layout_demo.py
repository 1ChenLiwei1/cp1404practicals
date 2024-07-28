from kivy.app import App
from kivy.lang import Builder


class BoxlayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file("box_layout.kv")
        return self.root

    def handle_greet(self):
        print('test')
        self.root.ids.output_label.text = "Hello"
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_boxlayout(self):
        self.root.ids.output_label.text = "Enter your name "
        self.root.ids.input_name.text = " "


BoxlayoutDemo().run()
