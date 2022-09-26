from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
    
    def gen_numb(self):
        self.random_label.text = str(random.randint(0,10000))

class Base(App):
    
    def build(self):
        return MyRoot() 

b = Base()
b.run()