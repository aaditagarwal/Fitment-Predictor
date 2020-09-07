from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from scripts.scoring import scores

class Result_Page(GridLayout):
    def __init__(self, ey_root, **kwargs):
        super().__init__(**kwargs)
        self.cols = 4
        self.ey_root = ey_root
        
        # Pipeline from previous pages
        self.demands = None
        self.weights = None
        self.scores_df = None

        self.employees = []
        
        self.reset_button = Button(text="Restart")
        self.reset_button.bind(on_press=self.restart_app)
        self.exit_button = Button(text="Exit")
        self.exit_button.bind(on_press=self.ey_root.stop)

    def restart_app(self, instance):
        self.clear_widgets()
        self.ey_root.go_weightage()

    def update_pipeline(self, demands, weights):
        self.demands = demands
        self.weights = weights
        employees_with_fitment, scores_df = scores(demands, weights)
        self.scores_df = scores_df
        self.scores_df.set_index("Employee_ID", inplace=True)

        # score_df.to_csv("outputs/Current_Output.csv")
        self.update_results(employees_with_fitment)
        
        #From Employee data call Get_Employee_Data

    def update_results(self, employees_with_fitment):
        self.add_widget(Label(text="Fitment Rank"))
        self.add_widget(Label(text="Employee"))
        self.add_widget(Label(text="Fitment Segment"))
        self.add_widget(Label(text="Fitment Score"))
        
        for dp in employees_with_fitment:
            for t in dp:
                if str(t)[:8] == "Employee":
                    # print("SHOWING FOR:", t)
                    btn = Button(text=str(t))
                    self.employees.append(btn)
                    btn.bind(on_press=self.employee_show)
                    # lambda x: self.ey_root.show_employee(idx=str(t), demands=self.demands, scores=self.scores_df))
                    self.add_widget(btn)
                elif '.' in str(t):
                    self.add_widget(Label(text="{0:.2f}".format(t)))
                else:
                    self.add_widget(Label(text=str(t)))
  
        self.add_widget(self.reset_button)
        self.add_widget(Label(text=""))
        self.add_widget(Label(text=""))
        self.add_widget(self.exit_button)

    def employee_show(self, instance):
        # print(instance.text)
        self.ey_root.show_employee(idx=instance.text, demands=self.demands, scores=self.scores_df)

