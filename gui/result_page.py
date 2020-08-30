from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from scripts.scoring import scores

class Result_Page(GridLayout):
    def __init__(self, ey_root, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.ey_root = ey_root
        
        # Pipeline from previous pages
        self.demands = None
        self.weights = None

        self.add_widget(Label(text="Employee"))
        self.add_widget(Label(text="Fitment Segment"))
        self.add_widget(Label(text="Fitment Rank"))
        
        self.reset_button = Button(text="Restart")
        self.reset_button.bind(on_press=self.restart_app)
        self.exit_button = Button(text="Exit")
        self.exit_button.bind(on_press=self.ey_root.stop)

    def restart_app(self, instance):
        self.clear_widgets()
        self.ey_root.reset_app()

    def update_pipeline(self, demands, weights):
        self.demands = demands
        self.weights = weights
        employees_with_fitment, score_df = scores(demands, weights)
        # score_df.to_csv("outputs/Current_Output.csv")
        self.update_results(employees_with_fitment)
        
        #From Employee data call Get_Employee_Data

    def update_results(self, employees_with_fitment):
        for dp in employees_with_fitment:
            for t in dp:
                self.add_widget(Label(text=str(t)))
        
        self.add_widget(self.reset_button)
        self.add_widget(self.exit_button)
