
from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.609


class MilesConvertApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.validate_input()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.validate_input() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def validate_input(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConvertApp().run()
