from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from alert import Alert

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
        self.add_widget(Label(text="Key"))
        self.add_widget(Label(text="Weights"))

        self.weight_holder = {}
        for key in self.weight_keys:
            self.weight_holder[key] = TextInput(text="", multiline=False)
            self.add_widget(Label(text=key+" ->"))
            self.add_widget(self.weight_holder[key])

        self.reset_button = Button(text="Restart")
        self.reset_button.bind(on_press=self.restart_app)
        self.add_widget(self.reset_button)

        self.submit_weights_button = Button(text="Submit")
        self.submit_weights_button.bind(on_press=self.submit_weights)
        self.add_widget(self.submit_weights_button)
        
    def update_demand(self, demand):
        self.demands = demand
    
    def restart_app(self, instance):
        for key in self.weight_keys:
            self.weight_holder[key].text = ""
        self.ey_root.reset_app()

    def preprocess_weights(self):
        weights = {}
        total_sum = 0

        for key in self.weight_keys:
                try:
                    weights[key] = int(self.weight_holder[key].text)
                    total_sum += weights[key]
                except ValueError:
                    Alert(title='Invalid Inputs!', text='One or More Inputs are invalid.')
                    return None

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
