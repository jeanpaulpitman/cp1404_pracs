"""
CP1404/CP5632 Practical
Kivy GUI program convert miles to kilometers
Jean-Paul Pitman
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

RATE = 0.6213

__author__ = 'Jean-Paul Pitman'


class ConvertMilesToKiloApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 400)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        self.handle_convert(self.root.ids.input_number.text)
        return self.root

    def handle_convert(self, value):
        """ handle convert miles to km """
        try:
            kilometers = int(value) / RATE
            self.root.ids.output_label.text = "{:.2f}".format(kilometers)
        except ValueError:
            self.root.ids.output_label.text = "0.0"

    def handle_increment(self, value):
        """handle up and down buttons"""
        try:
            current_value = int(self.root.ids.input_number.text)
        except ValueError:
            current_value = 0
        new_value = current_value + value
        self.root.ids.input_number.text = str(new_value)


if __name__ == '__main__':
    ConvertMilesToKiloApp().run()
