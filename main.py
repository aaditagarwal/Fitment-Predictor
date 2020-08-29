from scripts.input import demand_input
from scripts.input import weights
# from scripts.input import SL_weights
from scripts.query import experience
from scripts.query import rank
from scripts.query import location
from scripts.query import bench_aging
from scripts.query import technical_skill
from scripts.query import functional_skill
from scripts.query import process_skill
from scripts.ranking import ranking

import pandas as pd

# demand = pd.read_excel('./../data.xlsx',sheet_name=0,header=0)
supply_non_skills = pd.read_excel('./../data.xlsx',sheet_name=1,header=0)
supply_skills = pd.read_excel('./../data.xlsx',sheet_name=2,header=0)
# skill_tree = pd.read_excel('./../data.xlsx',sheet_name=3,header=0)

demand = demand_input()
weights = weights()

#NOTE Location and skills input in Supply need to be changed to tuple  

experience = experience(demand['Experience'],supply_non_skills['Experience'],weights['Experience'])
rank = rank(demand['Rank'],supply_non_skills['Rank'],weights['Rank'])
aging = bench_aging(supply_non_skills['Bench Ageing (weeks)'], weights['Bench Aging'])
location = location(demand['Location'],supply_non_skills['City'],weights['Location'])
technical_skill = technical_skill(demand['Technical Skill'],supply_skills,weights['Technical skill'])
functional_skill = functional_skill(demand['Functional Skill'],supply_skills,weights['Functional skill'])
process_skill = process_skill(demand['Process Skill'],supply_skills,weights['Process skill'])

data = pd.DataFrame(list(zip(experience, rank, aging, location, technical_skill, functional_skill, process_skill)), columns=['Experience','Rank','Location','Bench Aging','Technical Skill','Functional Skill','Process Skill'],index=supply_non_skills.index.tolist())
data['Score'] = data.sum(axis=1)

recommendations = ranking(data,supply_non_skills['Name/ID','Service_line','Sub_Service_Line','SMU'])