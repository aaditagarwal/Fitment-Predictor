# from kivy.config import Config
# Config.set('graphics', 'fullscreen', '0')
# Config.write()

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

from gui.alert import Alert
from gui.input_page import Input_Page
from gui.weightage_page import Weightage_Page
from gui.result_page import Result_Page

class EY_Hack(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.input_page_ = Input_Page(ey_root)
        screen = Screen(name="Input_Page")
        screen.add_widget(self.input_page_)
        self.screen_manager.add_widget(screen)
        
        self.weightage_page_ = Weightage_Page(ey_root)
        screen = Screen(name="Weightage_Page")
        screen.add_widget(self.weightage_page_)
        self.screen_manager.add_widget(screen)

        self.result_page_ = Result_Page(ey_root)
        screen = Screen(name="Result_Page")
        screen.add_widget(self.result_page_)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    def reset_app(self, *_):
        print("RESET CALLED")
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = "Input_Page"
    
    def go_weightage(self, *_):
        print("GOING TO WEIGHTAGE")
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = "Weightage_Page"
    
    def go_result(self, *_):
        print("GOING TO RESULT")
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = "Result_Page"

if __name__ == "__main__":
    ey_root = EY_Hack()
    ey_root.run()
