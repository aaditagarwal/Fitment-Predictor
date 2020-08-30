from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Result_Page(GridLayout):
    def __init__(self, ey_root, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.ey_root = ey_root
        
        # Pipeline from previous pages
        self.demands = None
        self.weights = None

        self.add_widget(Label(text="Employee"))
        self.add_widget(Label(text="Fitment Percentage"))
        
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
        # Call function here
        # employees_with_fitment_percentages = run_pipeline(demands, weights)
        self.update_results()

    def update_results(self):
        employees_with_fitment_percentages = [
            ("Employee1", "90%"),
            ("Employee2", "75%"),
            ("Employee3", "20%"),
            ("Employee4", "0%")
        ]
        for dp in employees_with_fitment_percentages:
            for t in dp:
                self.add_widget(Label(text=t))
        
        self.add_widget(self.reset_button)
        self.add_widget(self.exit_button)
