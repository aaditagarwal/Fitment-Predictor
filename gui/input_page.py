from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown 
from kivy.uix.slider import Slider 


from .alert import Alert
from scripts.employee_data import location_list
import scripts.skills, scripts.employee_data, scripts.query, scripts.ranking, scripts.scoring

class Input_Page(GridLayout):
    def __init__(self, ey_root, **kwargs):
        super().__init__(**kwargs)
        self.ey_root = ey_root
        self.cols = 2
        self.input_keys = ['Service Line','Sub Service Line','SMU',
                        'Location','Rank','Experience','Technical Skill',
                        'Functional Skill','Process Skill']
        self.input_holder = {}

        self.slider_values = {}
        
        self.add_widget(Label(text="Demand Heuristics"))
        self.add_widget(Label(text="Inputs"))

        for key in self.input_keys:
            self.input_holder[key] = TextInput(text="", multiline=False)
            if key == 'Service Line':
                self.slider_values[key] = Label(text=key+" (Integer between 1-4)"+" ->")
                self.add_widget(self.slider_values[key])
                self.input_holder[key] = Slider(min = 1, max = 4, step=1)
                self.input_holder[key].bind(value=lambda instance, x: self.on_slider('Service Line', instance.value, True))
            elif key == 'Sub Service Line':
                self.slider_values[key] = Label(text=key+" (Integer between 1-4)"+" ->")
                self.add_widget(self.slider_values[key])
                self.input_holder[key] = Slider(min = 1, max = 4, step=1)
                self.input_holder[key].bind(value=lambda instance, x: self.on_slider('Sub Service Line', instance.value, True))
            elif key == 'SMU':
                self.slider_values[key] = Label(text=key+" (Integer between 1-4)"+" ->")
                self.add_widget(self.slider_values[key])
                self.input_holder[key] = Slider(min = 1, max = 4, step=1)
                self.input_holder[key].bind(value=lambda instance, x: self.on_slider('SMU', instance.value, True))
            elif key == 'Rank':
                self.slider_values[key] = Label(text=key+" (Integer between 1-5)"+" ->")
                self.add_widget(self.slider_values[key])
                self.input_holder[key] = Slider(min = 1, max = 5, step=1)
                self.input_holder[key].bind(value=lambda instance, x: self.on_slider("Rank", instance.value, True))
            elif key == 'Experience':
                self.add_widget(Label(text=key+" (Integer)"+" ->"))
            elif 'Skill' in key:
                self.add_widget(Label(text=key+" (Seperate Skills by ',')"+" ->"))
            elif key == 'Location':
                self.add_widget(Label(text=key+" (City, Country)"+" ->"))

                self.dropdown = DropDown()
                for location in location_list(): 
                    # Adding button in drop down list 
                    btn = Button(text=location, size_hint_y=None)
                    #  height = 40) 
                
                    # binding the button to show the text when selected 
                    btn.bind(on_release = lambda btn: self.dropdown.select(btn.text)) 
                
                    # then add the button inside the dropdown 
                    self.dropdown.add_widget(btn)
                self.location_button = Button(text ='Select Location')
                self.location_button.bind(on_release = self.dropdown.open) 
                self.dropdown.bind(on_select = lambda instance, x: setattr(self.location_button, 'text', x)) 
                self.input_holder[key] = self.location_button

            self.add_widget(self.input_holder[key])

        self.submit_input_button = Button(text="Submit")
        self.submit_input_button.bind(on_press=self.submit_demand)

        self.reset_input_holder = Button(text="Clear")
        self.reset_input_holder.bind(on_press=self.reset_inputs)

        self.add_widget(self.reset_input_holder)
        self.add_widget(self.submit_input_button)
    
    def on_slider(self, key, value, change=False):
        if change:
            self.slider_values[key].text = f"{key} (Current: {value})->"

    def reset_inputs(self, *_):
        for key in self.input_keys:
            if key == "Location":
                self.input_holder[key].text = "Select Location"
            elif key in ['Service Line', 'Sub Service Line', 'SMU']:
                self.slider_values[key].text = key + " (Integer between 1-4) ->"
                self.input_holder[key].value = 1
            elif key == "Rank":
                self.slider_values[key].text = key + " (Integer between 1-5) ->"
                self.input_holder[key].value = 1
            else:
                self.input_holder[key].text = ""  

    def preprocess_input(self):
        demand = {}
        demand['Location'] = self.input_holder['Location'].text
        if demand['Location'] == "Select Location":
            Alert(title='Invalid Inputs!', text='Select a location.')
            return None
        for key in self.input_keys:
            if key == 'Experience':
                try:
                    demand[key] = int(self.input_holder[key].text)
                except ValueError:
                    Alert(title='Invalid Inputs!', text='Experience input is invalid.')
                    return None
            elif 'Skill' in key:
                try:
                    demand[key] = self.input_holder[key].text.lower().replace(" ","").split(',')
                except ValueError:
                    Alert(title='Invalid Inputs!', text='One or more Skill inputs are invalid.')
                    return None
            elif key != 'Location':
                demand[key] = self.input_holder[key].value
        return demand
    
    def submit_demand(self, instance):
        demand = self.preprocess_input()
        if demand:
            self.ey_root.weightage_page_.update_demand(demand)
            self.ey_root.go_weightage()
