import numpy as np
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
geolocator = Nominatim(user_agent="AI_capacity_management")

def experience(demand_exp, supply_exp, weights_exp):
    employee_experience = []
    for employee in supply_exp:
        exp_value = demand_exp - employee
        if exp_value == 0:
            exp_value = weights_exp
        elif exp_value < 0:
            exp_value = weights_exp * (1 - exp_value/10) # Requirement not met, affect is larger
        else:
            exp_value = weights_exp * (1 + exp_value/100) # Exceeds requirement, affect is smaller
        employee_experience.append(exp_value)
    return np.array(employee_experience)

def rank(demand_rank, supply_rank, weights_rank):
    employee_rank = []
    for employee in supply_rank:
        rank_value = demand_rank - employee
        if rank_value == 0:
            rank_value = weights_rank
        elif rank_value < 0:
            rank_value = weights_rank * (1 - rank_value/10)
        else:
            rank_value = weights_rank * (1 + rank_value/100)
        employee_rank.append(rank_value)
    return np.array(employee_rank)

def bench_aging(supply_aging, weights_aging):
    employee_aging = []
    for employee in supply_aging:
        employee_aging.append(-(employee*weights_aging)/10)
    return np.array(employee_aging)

def location(demand_location, supply_location, weights_location):
    demand_location = geolocator.geocode(demand_location)
    demand_location = (demand_location.latitude, demand_location.longitude)
    employee_location = []
    for employee in supply_location:
        employee = geolocator.geocode(employee)
        employee = (employee.latitude,employee.longitude)
        location_value = great_circle(demand_location,employee).km
        if location_value == 0:
            location_value = weights_location
        else:
            location_value = weights_location * (1 - location_value/1000)
        employee_location.append(location_value)
    return np.array(employee_location)

def technical_skill(demand_tech, supply_tech, weights_tech):
    employee_technical_skill = []
    for employee in supply_tech:
        skill_set = []
        for skill in demand_tech:
            skill_set.append(skill_match(skill,employee))
        skill_value = sum(skill_set)/len(skill_set)
        employee_technical_skill.append(skill_value*weights_tech)
    return  np.array(employee_technical_skill)


def functional_skill(demand_func, supply_func, weights_func):
    employee_functional_skill = []
    for employee in supply_func:
        skill_set = []
        for skill in demand_func:
            skill_set.append(skill_match(skill, employee))
        skill_value = sum(skill_set)/len(skill_set)
        employee_functional_skill.append(skill_value*weights_func)
    return np.array(employee_functional_skill)

def process_skill(demand_process, supply_process, weights_process):
    employee_process_skill = []
    for employee in supply_process:
        skill_set = []
        for skill in demand_process:
            skill_set.append(skill_match(skill,employee))
        skill_value = sum(skill_set)/len(skill_set)
        employee_process_skill.append(skill_value*weights_process)
    return  np.array(employee_process_skill)