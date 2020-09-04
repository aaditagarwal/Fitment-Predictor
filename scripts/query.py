import numpy as np
import pandas as pd

from geopy.geocoders import Nominatim
from geopy.distance import great_circle
geolocator = Nominatim(user_agent="AI_capacity_management")

from .employee_data import get_data
from .skills import match_skill

def experience(demand_exp, employee_ID, weights_exp):
    employee_experience = []
    for employee in employee_ID:
        employee_data = get_data(employee)['Experience']
        exp_value = employee_data - demand_exp
        if exp_value == 0:
            exp_value = weights_exp
        elif exp_value < 0:
            exp_value = weights_exp * (1 - np.abs(exp_value)/10) # Requirement not met, affect is larger
        else:
            exp_value = weights_exp * (1 + exp_value/50) # Exceeds requirement, affect is smaller
        employee_experience.append(exp_value)
    return np.array(employee_experience)

def rank(demand_rank, employee_ID, weights_rank):
    employee_rank = []
    for employee in employee_ID:
        employee_data = get_data(employee)['Rank']
        rank_value = int(employee_data[-1]) - demand_rank
        if rank_value == 0:
            rank_value = weights_rank
        elif rank_value < 0:
            rank_value = weights_rank * (1 + np.abs(rank_value)/50)
        else:
            rank_value = weights_rank * (1 - rank_value/10)
        employee_rank.append(rank_value)
    return np.array(employee_rank)

def bench_aging(employee_ID, weights_aging):
    employee_aging = []
    for employee in employee_ID:
        employee_data = get_data(employee)['Bench Aging']
        employee_aging.append(-(employee_data*weights_aging)/10)
    return np.array(employee_aging)

def location(demand_location, employee_ID, weights_location):
    demand_location = geolocator.geocode(demand_location)
    demand_location = (demand_location.latitude, demand_location.longitude)
    employee_location = []
    for employee in employee_ID:
        employee_data = get_data(employee)['Location']
        try:
            employee_data = geolocator.geocode(employee_data)
            employee_data = (employee_data.latitude,employee_data.longitude)
            location_value = great_circle(demand_location,employee_data).km
        except:
            location_value = -1
        if location_value == 0:
            location_value = weights_location
        elif location_value > 0:
            location_value = weights_location * (1 - location_value/1000)
        else:
            location_value = 0
        employee_location.append(location_value)
    return np.array(employee_location)

def technical_skill(demand_tech, employee_ID, weights_tech):
    employee_technical_skill = []
    for employee in employee_ID:
        employee_data = get_data(employee)['Technical Skills']
        skill_set = []
        for skill in demand_tech:
            skill_set.append(match_skill(skill,employee_data))
        skill_value = max(skill_set)
        employee_technical_skill.append(skill_value*weights_tech)
    return  np.array(employee_technical_skill)


def functional_skill(demand_func, employee_ID, weights_func):
    employee_functional_skill = []
    for employee in employee_ID:
        employee_data = get_data(employee)['Functional Skills']
        skill_set = []
        for skill in demand_func:
            skill_set.append(match_skill(skill, employee_data))
        skill_value = max(skill_set)
        employee_functional_skill.append(skill_value*weights_func)
    return np.array(employee_functional_skill)

def process_skill(demand_process, employee_ID, weights_process):
    employee_process_skill = []
    for employee in employee_ID:
        employee_data = get_data(employee)['Process Skills']
        skill_set = []
        for skill in demand_process:
            skill_set.append(match_skill(skill,employee_data))
        skill_value = max(skill_set)
        employee_process_skill.append(skill_value*weights_process)
    return  np.array(employee_process_skill)
