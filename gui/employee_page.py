from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from scripts.scoring import scores
from scripts.employee_data import employee_details

class Employee_Page(GridLayout):
    def __init__(self, ey_root, **kwargs):
        super().__init__(**kwargs)
        self.ey_root = ey_root
        self.cols = 4


    def update_results_employee(self, employee, demands, scores):
        table_data, information = employee_details(employee, demands, scores)
        for k,v in information.items():
            self.add_widget(Label(text=str(k)))
            if 'Skill' in k:
                for skill in v:
                    self.add_widget(Label(text=str(skill)))
            else:
                self.add_widget(Label(text=str(v)))    

        self.add_widget(Label(text="---"))
        self.add_widget(Label(text="---"))
        self.add_widget(Label(text="---"))
        self.add_widget(Label(text="---"))

        self.add_widget(Label(text="Attribute"))
        self.add_widget(Label(text="Supply"))
        self.add_widget(Label(text="Demand"))
        self.add_widget(Label(text="Score"))
        
        self.add_widget(Label(text="---"))
        self.add_widget(Label(text="---"))
        self.add_widget(Label(text="---"))
        self.add_widget(Label(text="---"))

        for row in table_data:
            for value in row:
                if "." in str(value):
                    self.add_widget(Label(text="{0:.2f}".format(value)))
                else:
                    self.add_widget(Label(text=str(value)))

        self.btn = Button(text="Go Back")
        self.btn.bind(on_press=self.go_back)

        self.add_widget(self.btn)

    def go_back(self, instance):
        self.clear_widgets()
        self.ey_root.go_result()