def demand_input():
    demand = {}
    keys = ['Service Line','Sub-Service Line','Business Unit','Location','Rank','Experience','Technical Skill','Functional Skill','Process Skill']
    print('Enter demand hueristics: ')
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
    print('\n',demand)
    return demand

def weights():
    weights = []
    weights_dict = {}
    keys = ['Location','Rank','Experience','Bench Aging','Technical Skill','Functional Skill','Process Skill']
    print('Enter weightage of demand hueristics (Percentages): ')
    for key in keys:
        weights_dict[key] = input(f'Enter weightage for {key}:')
        try:
            weights_dict[key] = int(weights_dict[key])
        except:
            weights_dict[key] = 0
    weights.append(weights_dict)
    return weights

def SL_weights():
    weights = []
    service_lines = 4 
    keys = ['Location','Rank','Experience','Bench Aging','Technical Skill','Functional Skill','Process Skill']
    for i in range(service_lines):
        weights_dict = {}
        print('\n')
        print("Enter weights for Service Line",i+1,"(Percentages):")
        for key in keys:
            weights_dict[key] = input(f'Enter weightage for {key}:')
            try:
                weights_dict[key] = int(weights_dict[key])
            except:
                weights_dict[key] = 0
    weights.append(weights_dict)
    return weights