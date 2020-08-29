import numpy as np
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
geolocator = Nominatim(user_agent="AI_capacity_management")

def experience(demand_exp, supply_exp, weights_exp):
    employee_experience = []
    for employee in supply_exp:
        exp_value = demand_exp - employee
        employee_experience.append([exp_value*i] for i in weights_exp)
    return np.array(employee_experience)

def experience(demand_rank, supply_rank, weights_rank):
    employee_rank = []
    for employee in supply_rank:
        rank_value = demand_rank - employee
        employee_rank.append([rank_value*i] for i in weights_rank)
    return np.array(employee_rank)

def bench_aging(supply_aging, weights_aging):
    employee_aging = []
    for employee in supply_aging:
        employee_aging.append(([-employee*i]) for i in weights_aging)
    return np.array(employee_aging)

def location(demand_location, supply_location, weights_location):
    demand_location = geolocator.geocode(demand_location)
    demand_location = (demand_location.latitude, demand_location.longitude)
    employee_location = []
    for employee in supply_location:
        employee = geolocator.geocode(employee)
        employee = (employee.latitude,employee.longitude)
        location_value = great_circle(demand_location,employee).km
        employee_location.append([location_value*i] for i in weights_location)
    return np.array(employee_location)