"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create labels based on content of list
Jean-Paul Pitman
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty

__author__ = 'Jean-Paul Pitman'


class LabelLoopApp(App):
    """ Main program - Kivy app to demo dynamic widget creation from a list """
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        self.names = ["Fred", "Jim", "Bob", "Harry", "Albert"]

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Dynamic Widgets from list"
        self.root = Builder.load_file('label_loop.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create labels from list entries and add them to the GUI
        :return: None
        """
        for name in self.names:
            # create a label for each names entry
            temp_label = Label(text=name)
            # add the label to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_label)

LabelLoopApp().run()
