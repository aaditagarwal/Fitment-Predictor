import numpy as np
import pandas as pd
from re import sub

supply_non_skills = pd.read_excel('data.xlsx', sheet_name=1, index_col=0, header=0)
supply_skills = pd.read_excel('data.xlsx', sheet_name=2, header=0)

def camelCase(string):
  string = sub(r"(_|-)+", " ", string).title().replace(" ", "")
  return (string[0].upper() + string[1:]).lstrip()

def get_skills(employee_id,units):
    skill_set = []
    supply = supply_skills.where(supply_skills['Name/ID'] == employee_id).dropna()
    for unit in units:
        sheet = supply.where(supply.Primary_Unit==unit).dropna()
        for i in list(range(sheet.shape[0])):
            skill_set.append((camelCase(sheet.iloc[i,5]),sheet.iloc[i,6]))
    return skill_set

def location_list():
    locations = []
    for index,employee in supply_non_skills.iterrows():
        locations.append(employee['City']+', '+employee['Country'])
    unique = np.array(locations)
    unique = np.unique(unique)
    return unique.tolist()

class employee():
    def __init__(self,employee_id):
        self.id = employee_id
        self.SL = supply_non_skills.loc[self.id,'Service_Line']
        self.SSL = supply_non_skills.loc[self.id, 'Sub_Service_Line']
        self.SMU = supply_non_skills.loc[self.id, 'SMU']
        self.experience = supply_non_skills.loc[self.id, 'Experience']
        self.rank = supply_non_skills.loc[self.id, 'Rank']
        self.location = supply_non_skills.loc[self.id,'City'] + ', ' + supply_non_skills.loc[self.id,'Country']
        self.bench_aging = supply_non_skills.loc[self.id,'Bench Ageing (weeks)']
        self.technical_skills = get_skills(self.id,['Unit 1','Unit 2','Unit 3'])
        self.functional_skills = get_skills(self.id,['Unit 4','Unit 5','Unit 6'])
        self.process_skills = get_skills(self.id,['Unit 7'])

def get_data(employee_id):
    person = employee(employee_id)
    data = {}
    data['ID'] = person.id
    data['Experience'] = person.experience
    data['Rank'] = person.rank
    data['Location'] = person.location
    data['Bench Aging'] = person.bench_aging
    data['Technical Skills'] = person.technical_skills
    data['Functional Skills'] = person.functional_skills
    data['Process Skills'] = person.process_skills
    return data

def get_employee_data(employee_id,scores):
    person = employee(employee_id)
    data = {}
    data['ID'] = person.id
    data['Service Line'] = person.SL
    data['Sub Service Line'] = person.SSL
    data['SMU'] = person.SMU
    data['Experience'] = person.experience
    data['Experience Score'] = scores.loc[employee_id, 'Experience']
    data['Rank'] = person.rank
    data['Rank Score'] = scores.loc[employee_id,'Rank']
    data['Location'] = person.location
    data['Location Score'] = scores.loc[employee_id,'Location']
    data['Bench_Aging'] = person.bench_aging
    data['Bench_Aging Score'] = scores.loc[employee_id,'Bench Aging']
    data['Technical Skill'] = person.technical_skills
    data['Technical Skill Score'] = scores.loc[employee_id, 'Technical Skill']
    data['Functional Skill'] = person.functional_skills
    data['Functional Skill Score'] = scores.loc[employee_id, 'Functional Skill']
    data['Process Skill'] = person.process_skills
    data['Process Skill Score'] = scores.loc[employee_id, 'Process Skill']
    data['Fitment Score'] = scores.loc[employee_id,'Fitment Score']
    data['Fitment Rank'] = scores.loc[employee_id,'Rank']
    data['Fitment Segment'] = scores.loc[employee_id, 'Fitment Segment']
    return data

def employee_details(employee_id, demand, scores):
    person = []
    information = {}
    data = get_employee_data(employee_id,scores)
    keys = ['Service Line', 'Sub Service Line', 'SMU',
             'Location', 'Rank', 'Experience', 'Technical Skill',
             'Functional Skill', 'Process Skill']
    
    for key in keys:
        if key in ['Service Line', 'Sub Service Line', 'SMU']:
            person.append([key,data[key],demand[key],None])
        else:
            person.append([key,data[key],demand[key],data[key+' Score']])
    
    information['Fitment Score'] = data['Fitment Score']
    information['Fitment Rank'] = data['Fitment Rank']
    information['Fitment Segment'] = data['Fitment Segment']

    return person, information