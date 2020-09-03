from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

from .alert import Alert

class Input_Page(GridLayout):
    def __init__(self, ey_root, **kwargs):
        super().__init__(**kwargs)
        self.ey_root = ey_root
        self.cols = 2
        self.input_keys = ['Service Line','Sub Service Line','SMU',
                        'Location','Rank','Experience','Technical Skill',
                        'Functional Skill','Process Skill']
        self.input_holder = {}
        
        self.add_widget(Label(text="Key"))
        self.add_widget(Label(text="Inputs"))

        for key in self.input_keys:
            self.input_holder[key] = TextInput(text="", multiline=False)
            if key in ['Service Line', 'Sub-Service Line', 'SMU']:
                self.add_widget(Label(text=key+" (Integer between 1-4)"+" ->"))
            elif key == 'Rank':
                self.add_widget(Label(text=key+" (Integer between 1-5)"+" ->"))
            elif key == 'Experience':
                self.add_widget(Label(text=key+" (Integer)"+" ->"))
            elif 'Skill' in key:
                self.add_widget(Label(text=key+" (Seperate Skills by ',')"+" ->"))
            elif key == 'Location':
                self.add_widget(Label(text=key+" (City, Country)"+" ->"))
            self.add_widget(self.input_holder[key])

        self.submit_input_button = Button(text="Submit")
        self.submit_input_button.bind(on_press=self.submit_demand)

        self.reset_input_holder = Button(text="Clear")
        self.reset_input_holder.bind(on_press=self.reset_inputs)

        self.add_widget(self.reset_input_holder)
        self.add_widget(self.submit_input_button)
    
    def reset_inputs(self, *_):
        for key in self.input_keys:
            self.input_holder[key].text = ""  

    def preprocess_input(self):
        demand = {}
        demand['Location'] = self.input_holder['Location'].text
        for key in self.input_keys:
            if key in ['Experience' , 'Rank' , 'Service Line' , 'Sub-Service Line' , 'SMU']:
                try:
                    demand[key] = int(self.input_holder[key].text)
                except ValueError:
                    Alert(title='Invalid Inputs!', text='One or More Inputs are invalid.')
                    return None
            elif key in ['Service Line', 'Sub-Service Line', 'SMU']:
                if (demand[key]<1) or (demand[key]>4) :
                    Alert(title='Invalid Inputs!', text='One or More Inputs are invalid.')
                    return None
            elif key == 'Rank':
                if (demand[key]<1) or (demand[key]>5) :
                    Alert(title='Invalid Inputs!', text='One or More Inputs are invalid.')
                    return None
            elif 'Skill' in key:
                try:
                    demand[key] = self.input_holder[key].text.split(',')
                except ValueError:
                    Alert(title='Invalid Inputs!', text='One or More Inputs are invalid.')
                    return None
        return demand
    
    def submit_demand(self, instance):
        demand = self.preprocess_input()
        if demand:
            self.ey_root.weightage_page_.update_demand(demand)
            self.ey_root.go_weightage()
        # else:
        #     self.ey_root.reset_app()
