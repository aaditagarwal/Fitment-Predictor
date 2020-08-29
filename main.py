from scripts.input import demand_input
from scripts.input import weights
from scripts.input import SL_weights
from scripts.query import experience
from scripts.query import rank
from scripts.query import location
from scripts.query import bench_aging
from scripts.ranking import ranking

import pandas as pd

demand = pd.read_excel('./../data.xlsx',sheet_name=0,header=0)
supply_non_skills = pd.read_excel('./../data.xlsx',sheet_name=1,header=0)
supply_skills = pd.read_excel('./../data.xlsx',sheet_name=2,header=0)
skill_tree = pd.read_excel('./../data.xlsx',sheet_name=3,header=0)

demand = demand_input()

while True:
    choice = input('Service Line wise weights (Yes/No): ')
    if choice.lower() == 'yes':
        weights = SL_weights()
    elif choice.lower == 'no':
        weights = weights()
    else:
        print('Invalid Input.')
        continue
    break

