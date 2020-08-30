import pandas as pd
import numpy as np

from .query import experience
from .query import rank
from .query import location
from .query import bench_aging
from .query import technical_skill
from .query import functional_skill
from .query import process_skill

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

    scores = pd.DataFrame(list(zip(employee_ID.tolist(), location_scores, rank_scores, exp_scores, aging_scores,
                                   tech_skill_scores, func_skill_scores, process_skill_scores)),
                                   columns=['Employee_ID', 'Location', 'Rank', 'Experience', 'Bench Aging', 
                                    'Technical Skill','Functional Skill', 'Process Skill'], index=employee_ID.tolist())

    scores['Fitment_Score'] = scores.iloc[1:,:].sum(axis=1)

    scores.sort_values('Fitment_Score', inplace=True, ascending=False, ignore_index = True)
    scores['Fitment Rank'] = scores.index.tolist()
    scores['Fitment Rank'] += 1

    scores['Fitment Segment'] = 'No Segment'
    scores['Fitment Segment'] = scores['Fitment Segment'].where(scores['Fitment_Score']<60,other='Best Bet')
    scores['Fitment Segment'] = scores['Fitment Segment'].where(scores['Fitment_Score']<70,other='Stretched Fit Fit')
    scores['Fitment Segment'] = scores['Fitment Segment'].where(scores['Fitment_Score']<85,other='Best Fit')

    return scores

def scores(demands, weights):
    score_df = scoring(demands, weights)
    scores = []
    for i in list(range(score_df.shape[0])):
        scores.append((score_df.iloc[i,0], score_df.iloc[i,10], score_df.iloc[i,9]))
    return scores