def demand_input():
    demand = {}
    keys = ['Service Line','Sub-Service Line','Business Unit','Location','Rank','Experience','Technical Skill','Functional Skill','Process Skill']
    print('Enter demand hueristics->')
    for key in keys:
        demand[key] = input(f'Enter {key}:')
        if key in ['Experience' , 'Rank' , 'Service Line' , 'Sub-Service Line' , 'Business Unit']:
            try:
                demand[key] = int(demand[key])
            except:
                print('Invalid Entry')
                demand[key] = None
        if 'Skill' in  key:
            demand[key] = demand[key].split(',')
    return demand

def weights():
    weights = {}
    keys = ['Location','Rank','Experience','Bench Aging','Technical Skill','Functional Skill','Process Skill']
    print('Enter weightage of demand hueristics (Percentages)->')
    for key in keys:
        weights[key] = input(f'Enter weightage for {key}:')
        try:
            weights[key] = int(weights[key])
        except:
            weights[key] = 0
    return weights

# def SL_weights():
#     weights = []
#     service_lines = 4 
#     keys = ['Location','Rank','Experience','Bench Aging','Technical Skill','Functional Skill','Process Skill']
#     for i in range(service_lines):
#         weights = {}
#         print('\n')
#         print("Enter weights for Service Line",i+1,"(Percentages):")
#         for key in keys:
#             weights[key] = input(f'Enter weightage for {key}:')
#             try:
#                 weights[key] = int(weights[key])
#             except:
#                 weights[key] = 0
#     weights.append(weights)
#     return weights