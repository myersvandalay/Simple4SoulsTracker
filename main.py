import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random


class IsaacGridLayout(BoxLayout):
    def roll(self):
        print(self.d6.background_color)
        if self.d6.background_color == [1.0, 0.0, 0.1, 1.0]:
            self.d6.background_color = (0.0, 1.0, .1, 1.0)
        elif self.d6.background_color == [0.0, 1.0, .1, 1.0]:
            self.d6.background_color = (0.0, 0.0, 1.0, 1.0)
        else:
            self.d6.background_color = (1.0, 0.0, 0.1, 1.0)
        return str(random.randint(1, 6))

class IsaacApp(App):
    def build(self):
        return IsaacGridLayout()

IsaacApp = IsaacApp()
IsaacApp.run()