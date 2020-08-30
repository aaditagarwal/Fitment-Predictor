import numpy as np
import pandas as import pd
from re import sub

supply_non_skills = pd.read_excel('./../data.xlsx', sheet_name=1, index_col=0, header=0)
supply_skills = pd.read_excel('./../data.xlsx', sheet_name=2, header=0)

def camelCase(string):
  string = sub(r"(_|-)+", " ", string).title().replace(" ", "")
  return string[0].upper() + string[1:]

def get_skills(employee_id,units):
    skill_set = []
    supply_skills = supply_skills.where(supply_skills.Name/ID == employee_id).dropna()
    for unit in units:
        sheet = supply_skills.where(supply_skills.Primary_Unit==unit.dropna())
        for skill in sheet:
            skill_set.append((camelCase(skill.Skill.text),skill.Skill_level))
    return skill_set

class employee(employee_id):
    def __init__(self,employee_id):
        self.id = employee_id
        self.experience = supply_non_skills.loc[self.id, 'Experience']
        self.rank = supply_non_skills.loc[self.id, 'Rank']
        self.location = supply_non_skills.loc[self.id,'City'].text + ', ' + supply_non_skills.loc[self.id,'Country'].text
        self.bench_aging = supply_non_skills.loc[self.id,'Bench Ageing (weeks)']
        self.technical_skills = get_skills(self.id,['Unit 1','Unit 2','Unit 3'])
        self.functional_skills = get_skills(self.id,['Unit 4','Unit 5','Unit 6'])
        self.process_skills = get_skills(self.id,['Unit 7'])

    def get_data(self,employee_id):
        person = employee(employee_id)
        data = {}
        data['ID'] = person.id
        data['Experience'] = person.experience
        data['Rank'] = person.rank
        data['Location'] = person.location
        data['Bench_Aging'] = person.bench_aging
        data['Technical Skills'] = person.technical_skills
        data['Functional Skills'] = person.functional_skills
        data['Process Skill'] = person.process_skills
        return data

    def get_employee_data(self,employee_id,scores):
        person = employee(employee_id)
        data = {}
        data['ID'] = person.id
        data['Experience'] = person.experience
        data['Rank'] = person.rank
        data['Location'] = person.location
        data['Bench_Aging'] = person.bench_aging
        data['Technical Skills'] = person.technical_skills
        data['Functional Skills'] = person.functional_skills
        data['Process Skill'] = person.process_skills
        data['Fitment Score'] = scores.loc[employee_id,'Score']
        data['Fitment Rank'] = scores.loc[employee_id,'Rank']
        if data['Fitment Score'] >= 85:
            data['Fitment Segment'] = 'Best Fit'
        elif (data['Fitment Score']>=70) and (data['Fitment Score']<85):
            data['Fitment Segment'] = 'Stretched Fit'
        elif (data['Fitment Score']>=60) and (data['Fitment Score']<70):
            data['Fitment Segment'] = 'Best Bet'
        else
            data['Fitment Segment'] = 'No Segment'
        return data