import pandas as pd
import numpy as np

from .scripts.query import experience
from .scripts.query import rank
from .scripts.query import location
from .scripts.query import bench_aging
from .scripts.query import technical_skill
from .scripts.query import functional_skill
from .scripts.query import process_skill

employee_ID = pd.read_excel('./../data.xlsx',header=0,sheet_name=1)
employee_ID = employee_ID.Name/ID

def scoring(demands, weights):
    exp_scores = experience(demands['Experience'], employee_ID, weights['Experience'])
    rank_scores = rank(demands['Rank'], employee_ID, weights['Rank'])
    location_scores = location(demands['Location'], employee_ID, weights['Location'])
    aging_scores = bench_aging(employee_ID, weights['experience'])
    tech_skill_scores = technical_skill(demands['Technical Skill'], employee_ID, weights['Technical Skill'])
    func_skill_scores = functional_skill(demands['Functional Skill'], employee_ID, weights['Functional Skill'])
    process_skill_scores = process_skill(demands['Process Skill'], employee_ID, weights['Process Skill'])

    scores = pd.DataFrame(list(zip(employee_ID.tolist(), location_scores, rank_scores, exp_scores, aging_scores,
                                   tech_skill_scores, func_skill_scores, process_skill_scores)),
                                   columns=['Employee_ID', 'Location', 'Rank', 'Experience', 'Bench Aging', 
                                    'Technical Skill','Functional Skill', 'Process Skill'], index=employee_ID.tolist())

    scores['Fitment_Score'] = score.loc[1:,:].sum(axis=1)

    scores.sort_value('Fitment_Scores', inplace=True, ascending=False, ignore_index = True)
    scores['Fitment Rank'] = scores.index.tolist() + 1

    scores['Fitment Segment'] = 'No Segment'
    scores['Fitment Segment'] = scores['Fitment Segment'].where(scores.Fitment_Score<60,other='Best Bet')
    scores['Fitment Segment'] = scores['Fitment Segment'].where(scores.Fitment_Score<70,other='Stretched Fit Fit')
    scores['Fitment Segment'] = scores['Fitment Segment'].where(scores.Fitment_Score<85,other='Best Fit')

    return scores

def scores(demands, weights):
    score_df = scoring(demands, weights)
    scores = []
    for employee in score_df;
        scores.append((employee['Employee_ID'], employee['Fitment Segment'], employee['Fitment Rank']))
    return scores