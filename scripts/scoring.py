import pandas as pd
import numpy as np

from .query import experience
from .query import rank
from .query import location
from .query import bench_aging
from .query import technical_skill
from .query import functional_skill
from .query import process_skill
from .ranking import ranking

employee_ID = pd.read_excel('data.xlsx',header=0,sheet_name=1)
employee_ID = employee_ID['Name/ID']

def scoring(demands, weights):
    exp_scores = experience(demands['Experience'], employee_ID, weights['Experience'])
    rank_scores = rank(demands['Rank'], employee_ID, weights['Rank'])
    location_scores = location(demands['Location'], employee_ID, weights['Location'])
    aging_scores = bench_aging(employee_ID, weights['Bench Aging'])
    tech_skill_scores = technical_skill(demands['Technical Skill'], employee_ID, weights['Technical Skill'])
    func_skill_scores = functional_skill(demands['Functional Skill'], employee_ID, weights['Functional Skill'])
    process_skill_scores = process_skill(demands['Process Skill'], employee_ID, weights['Process Skill'])

    scores = pd.DataFrame(list(zip(location_scores, rank_scores, exp_scores, aging_scores,
                                   tech_skill_scores, func_skill_scores, process_skill_scores)),
                                   columns=['Location', 'Rank', 'Experience', 'Bench Aging', 
                                    'Technical Skill','Functional Skill', 'Process Skill'], index=employee_ID.tolist())
    scores.index.name = "Employee_ID"

    scores['Fitment Score'] = scores.sum(axis=1)

    scores['Fitment Segment'] = 'No Segment'
    scores['Fitment Segment'] = scores['Fitment Segment'].where(scores['Fitment Score']<60,other='Best Bet')
    scores['Fitment Segment'] = scores['Fitment Segment'].where(scores['Fitment Score']<70,other='Stretched Fit')
    scores['Fitment Segment'] = scores['Fitment Segment'].where(scores['Fitment Score']<85,other='Best Fit')

    scores = ranking(scores,demands)
    scores.reset_index(inplace=True)

    return scores

def scores(demands, weights):
    score_df = scoring(demands, weights)
    scores = []
    for i in list(range(score_df.shape[0])):
        scores.append((score_df.loc[i,'Fitment Rank'], score_df.loc[i,'Employee_ID'], score_df.loc[i,'Fitment Segment'], score_df.loc[i,'Fitment Score']))
    return scores, score_df
