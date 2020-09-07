from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider 

from .alert import Alert

class Weightage_Page(GridLayout):
    def __init__(self, ey_root, **kwargs):
        super().__init__(**kwargs)
        self.ey_root = ey_root
        self.cols = 2
        # Demand from input_page
        self.demands = None 
        
        self.weight_keys = ['Location','Rank','Experience',
                            'Bench Aging','Technical Skill',
                            'Functional Skill','Process Skill']
        self.add_widget(Label(text="Heuristics"))
        self.total_weight_label = Label(text="Weights")
        self.add_widget(self.total_weight_label)
        self.slider_values = {}

        self.weight_holder = {}
        for key in self.weight_keys:
            if key == 'Location':
                self.slider_values[key] = Label(text=key+" ->")
                self.add_widget(self.slider_values[key])
                self.weight_holder[key] = Slider(min = 0, max = 100, step=1)
                self.weight_holder[key].bind(value=lambda instance, x: self.on_slider('Location', instance.value))
            elif key == 'Rank':
                self.slider_values[key] = Label(text=key+" ->")
                self.add_widget(self.slider_values[key])
                self.weight_holder[key] = Slider(min = 0, max = 100, step=1)
                self.weight_holder[key].bind(value=lambda instance, x: self.on_slider('Rank', instance.value))
            elif key == 'Experience':
                self.slider_values[key] = Label(text=key+" ->")
                self.add_widget(self.slider_values[key])
                self.weight_holder[key] = Slider(min = 0, max = 100, step=1)
                self.weight_holder[key].bind(value=lambda instance, x: self.on_slider('Experience', instance.value))
            elif key == 'Bench Aging':
                self.slider_values[key] = Label(text=key+" ->")
                self.add_widget(self.slider_values[key])
                self.weight_holder[key] = Slider(min = 0, max = 100, step=1)
                self.weight_holder[key].bind(value=lambda instance, x: self.on_slider('Bench Aging', instance.value))
            elif key == 'Technical Skill':
                self.slider_values[key] = Label(text=key+" ->")
                self.add_widget(self.slider_values[key])
                self.weight_holder[key] = Slider(min = 0, max = 100, step=1)
                self.weight_holder[key].bind(value=lambda instance, x: self.on_slider('Technical Skill', instance.value))
            elif key == 'Functional Skill':
                self.slider_values[key] = Label(text=key+" ->")
                self.add_widget(self.slider_values[key])
                self.weight_holder[key] = Slider(min = 0, max = 100, step=1)
                self.weight_holder[key].bind(value=lambda instance, x: self.on_slider('Functional Skill', instance.value))
            elif key == 'Process Skill':
                self.slider_values[key] = Label(text=key+" ->")
                self.add_widget(self.slider_values[key])
                self.weight_holder[key] = Slider(min = 0, max = 100, step=1)
                self.weight_holder[key].bind(value=lambda instance, x: self.on_slider('Process Skill', instance.value))
            self.add_widget(self.weight_holder[key])

        self.reset_button = Button(text="Restart")
        self.reset_button.bind(on_press=self.restart_app)
        self.add_widget(self.reset_button)

        self.submit_weights_button = Button(text="Submit")
        self.submit_weights_button.bind(on_press=self.submit_weights)
        self.add_widget(self.submit_weights_button)
        
    def on_slider(self, key, value):
        self.slider_values[key].text = f"{key} ({value}%) ->"
        self.update_total()

    def update_total(self):
        total = 0
        for key in self.weight_keys: 
            total += self.weight_holder[key].value
        self.total_weight_label.text = f"Weights (Total={total}%)"

    def update_demand(self, demand):
        self.demands = demand
    
    def restart_app(self, instance):
        for key in self.weight_keys:
            self.weight_holder[key].value = 0
            self.slider_values[key].text = key + " ->"
        self.ey_root.reset_app()

    def preprocess_weights(self):
        weights = {}
        total_sum = 0

        for key in self.weight_keys:
            weights[key] = self.weight_holder[key].value
            total_sum += weights[key]

        if total_sum != 100:
            Alert(title='Invalid Inputs!', text=f'Total weightage ({total_sum}) does not add up to 100%.')
            return None

        return weights

    def submit_weights(self, instance):
        weights = self.preprocess_weights()
        if weights and self.demands:
            print("Successful")
            print(self.demands)
            print(weights)
            self.ey_root.result_page_.update_pipeline(self.demands, weights)
            self.ey_root.go_result()
