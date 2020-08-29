import numpy as np
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
geolocator = Nominatim(user_agent="AI_capacity_management")

def experience(demand_exp, supply_exp, weights_exp):
    employee_experience = []
    for employee in supply_exp:
        exp_value = demand_exp - employee
        employee_experience.append(exp_value*weights_exp)
    return np.array(employee_experience)

def rank(demand_rank, supply_rank, weights_rank):
    employee_rank = []
    for employee in supply_rank:
        rank_value = demand_rank - employee
        employee_rank.append(rank_value*weights_rank)
    return np.array(employee_rank)

def bench_aging(supply_aging, weights_aging):
    employee_aging = []
    for employee in supply_aging:
        employee_aging.append(-employee*weights_aging)
    return np.array(employee_aging)

def location(demand_location, supply_location, weights_location):
    demand_location = geolocator.geocode(demand_location)
    demand_location = (demand_location.latitude, demand_location.longitude)
    employee_location = []
    for employee in supply_location:
        employee = geolocator.geocode(employee)
        employee = (employee.latitude,employee.longitude)
        location_value = great_circle(demand_location,employee).km
        employee_location.append(location_value*weights_location)
    return np.array(employee_location)

def technical_skill(demand_tech, supply_tech, weights_tech):
    employee_technical_skill = []
    for employee in supply_tech:
        skill_value, count = 0, 0
        for skill in demand_tech:
            skill_value += skill_match(skill,employee)
            count += 1
        skill_value /= count
        employee_technical_skill.append(skill_value*weights_tech)
    return  np.array(employee_technical_skill)


def functional_skill(demand_func, supply_func, weights_func):
    employee_functional_skill = []
    for employee in supply_func:
        skill_value, count = 0, 0
        for skill in demand_func:
            skill_value += skill_match(skill, employee)
            count += 1
        skill_value /= count
        employee_functional_skill.append(skill_value*weights_func)
    return np.array(employee_functional_skill)

def process_skill(demand_process, supply_process, weights_process):
    employee_process_skill = []
    for employee in supply_process:
        skill_value, count = 0, 0
        for skill in demand_process:
            skill_value += skill_match(skill,employee)
            count += 1
        skill_value /= count
        employee_process_skill.append(skill_value*weights_process)
    return  np.array(employee_process_skill)