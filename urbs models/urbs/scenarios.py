import pandas as pd

# SCENARIO GENERATORS
# In this script a variety of scenario generator functions are defined to
# facilitate scenario definitions.


def scenario_base(data):
    # do nothing
    return data


def scenario_stock_prices(data):
    # change stock commodity prices
    co = data['commodity']
    stock_commodities_only = (co.index.get_level_values('Type') == 'Stock')
    co.loc[stock_commodities_only, 'price'] *= 1.5
    return data


def scenario_co2_limit_50(data):
    # change global CO2 limit
    global_prop = data['global_prop']
    for stf in global_prop.index.levels[0].tolist():
        global_prop.loc[(stf, 'CO2 limit'), 'value'] = 2.2e6
    return data

def scenario_co2_limit_80(data):
    # change global CO2 limit
    global_prop = data['global_prop']
    for stf in global_prop.index.levels[0].tolist():
        global_prop.loc[(stf, 'CO2 limit'), 'value'] = 8e5
    return data

def scenario_co2_limit_07(data):
    # change global CO2 limit
    global_prop = data['global_prop']
    for stf in global_prop.index.levels[0].tolist():
        global_prop.loc[(stf, 'CO2 limit'), 'value'] =7e5
    return data

def scenario_co2_limit_0(data):
    # change global CO2 limit
    global_prop = data['global_prop']
    for stf in global_prop.index.levels[0].tolist():
        global_prop.loc[(stf, 'CO2 limit'), 'value'] =1
    return data


# def scenario_CO2pricenorth(data): #in actual it should be scenario_CO2pricemid
#     #change CO2 price in Mid
#     co = data['commodity']
#     for stf in data['global_prop'].index.levels[0].tolist():
#         co.loc[(stf, 'NorthGermany', 'CO2', 'Env'), 'price'] = 50   #Original Value Mid
#     return data
#
# def scenario_CO2pricesouth(data):
#     #change CO2 price in South
#     co = data['commodity']
#     for stf in data['global_prop'].index.levels[0].tolist():
#         co.loc[(stf, 'SouthGermany', 'CO2', 'Env'), 'price'] = 50
#     return data
def scenario_CO2price300(data):      #Original Scenario = north and south
    #change CO2 price in Mid
    co = data['commodity']
    for stf in data['global_prop'].index.levels[0].tolist():

        co.loc[(stf, 'DEU', 'CO2', 'Env'), 'price'] = 300  # Original Value North Germany/SouthGermany

    return data

def scenario_CO2price5(data):      #Original Scenario = north and south
    #change CO2 price in Mid
    co = data['commodity']
    for stf in data['global_prop'].index.levels[0].tolist():

        co.loc[(stf, 'DEU', 'CO2', 'Env'), 'price'] = 5  # Original Value North Germany/SouthGermany

    return data

def scenario_CO2price10(data):      #Original Scenario = north and south
    #change CO2 price in Mid
    co = data['commodity']
    for stf in data['global_prop'].index.levels[0].tolist():

        co.loc[(stf, 'DEU', 'CO2', 'Env'), 'price'] = 10  # Original Value North Germany/SouthGermany

    return data

def scenario_CO2price20(data):      #Original Scenario = north and south
    #change CO2 price in Mid
    co = data['commodity']
    for stf in data['global_prop'].index.levels[0].tolist():

        co.loc[(stf, 'DEU', 'CO2', 'Env'), 'price'] = 20  # Original Value North Germany/SouthGermany

    return data

def scenario_CO2price30(data):      #Original Scenario = north and south
    #change CO2 price in Mid
    co = data['commodity']
    for stf in data['global_prop'].index.levels[0].tolist():

        co.loc[(stf, 'DEU', 'CO2', 'Env'), 'price'] = 30  # Original Value North Germany/SouthGermany

    return data

def scenario_CO2price35(data):      #Original Scenario = north and south
    #change CO2 price in Mid
    co = data['commodity']
    for stf in data['global_prop'].index.levels[0].tolist():
        co.loc[(stf, 'DEU', 'CO2', 'Env'), 'price'] = 35  # Original Value North Germany/SouthGermany
    return data

def scenario_CO2price45(data):      #Original Scenario = north and south
    #change CO2 price in Mid
    co = data['commodity']
    for stf in data['global_prop'].index.levels[0].tolist():

        co.loc[(stf, 'DEU', 'CO2', 'Env'), 'price'] = 45  # Original Value North Germany/SouthGermany
    return data
    
def scenario_CO2price40(data):      #Original Scenario = north and south
    #change CO2 price in Mid
    co = data['commodity']
    for stf in data['global_prop'].index.levels[0].tolist():

        co.loc[(stf, 'DEU', 'CO2', 'Env'), 'price'] = 40  # Original Value North Germany/SouthGermany

    return data


def scenario_CO2price50(data):      #Original Scenario = north and south
    #change CO2 price in Mid
    co = data['commodity']
    for stf in data['global_prop'].index.levels[0].tolist():

        co.loc[(stf, 'DEU', 'CO2', 'Env'), 'price'] = 50  # Original Value North Germany/SouthGermany

    return data

def scenario_CO2price100(data):      #Original Scenario = north and south
    #change CO2 price in Mid
    co = data['commodity']
    for stf in data['global_prop'].index.levels[0].tolist():

        co.loc[(stf, 'DEU', 'CO2', 'Env'), 'price'] = 300  # Original Value North Germany/SouthGermany

    return data

def scenario_CO2price150(data):      #Original Scenario = north and south
    #change CO2 price in Mid
    co = data['commodity']
    for stf in data['global_prop'].index.levels[0].tolist():

        co.loc[(stf, 'DEU', 'CO2', 'Env'), 'price'] = 300  # Original Value North Germany/SouthGermany

    return data

def scenario_CO2price200(data):      #Original Scenario = north and south
    #change CO2 price in Mid
    co = data['commodity']
    for stf in data['global_prop'].index.levels[0].tolist():

        co.loc[(stf, 'DEU', 'CO2', 'Env'), 'price'] = 300  # Original Value North Germany/SouthGermany

    return data

def scenario_CO2price250(data):      #Original Scenario = north and south
    #change CO2 price in Mid
    co = data['commodity']
    for stf in data['global_prop'].index.levels[0].tolist():

        co.loc[(stf, 'DEU', 'CO2', 'Env'), 'price'] = 300  # Original Value North Germany/SouthGermany

    return data

def scenario_LowElecPrice(data):      #Original Scenario = north and south
    #change CO2 price in Mid
    co = data['commodity']
    for stf in data['global_prop'].index.levels[0].tolist():

        co.loc[(stf, 'DEU', 'Elec', 'Stock'), 'price'] *= .75  # Original Value North Germany/SouthGermany

    return data



def scenario_unbounded_caps(data):
    pro = data['process']
    for stf in data['global_prop'].index.levels[0].tolist():
        pro.loc[(stf, 'DEU', ), 'cap-up'] = 1e78
    return data

# def scenario_europe_process_caps(data):          

# #Original def scenario_north_process_caps(data):
#     #change maximum installable capacity
#     pro = data['process']
#     for stf in data['global_prop'].index.levels[0].tolist():
#         # pro.loc[(stf, 'NorthGermany', 'Hydro plant'), 'cap-up'] *= 0.5  #Original Value North
#         # pro.loc[(stf, 'NorthGermany', 'Biomass plant'), 'cap-up'] *= 0.25   #Original Value North
#         pro.loc[(stf, 'AUT', 'Hydro'), 'cap-up'] *= 0.5  # Original Value NorthGermany
#         pro.loc[(stf, 'AUT', 'Biomass'), 'cap-up'] *= 0.25   # Original Value NorthGermany
#         pro.loc[(stf, 'BEL', 'Hydro'), 'cap-up'] *= 0.5  # Original Value NorthGermany
#         pro.loc[(stf, 'BEL', 'Biomass'), 'cap-up'] *= 0.25  # Original Value NorthGermany
#         pro.loc[(stf, 'CHE', 'Hydro'), 'cap-up'] *= 0.5  # Original Value NorthGermany
#         pro.loc[(stf, 'CHE', 'Biomass'), 'cap-up'] *= 0.25  # Original Value NorthGermany
#         pro.loc[(stf, 'CZE', 'Hydro'), 'cap-up'] *= 0.5  # Original Value NorthGermany
#         pro.loc[(stf, 'CZE', 'Biomass'), 'cap-up'] *= 0.25  # Original Value NorthGermany
#         pro.loc[(stf, 'DEU', 'Hydro'), 'cap-up'] *= 0.5  # Original Value NorthGermany
#         pro.loc[(stf, 'DEU', 'Biomass'), 'cap-up'] *= 0.25  # Original Value NorthGermany
#         pro.loc[(stf, 'DNK', 'Hydro'), 'cap-up'] *= 0.5  # Original Value NorthGermany
#         pro.loc[(stf, 'DNK', 'Biomass'), 'cap-up'] *= 0.25  # Original Value NorthGermany
#         pro.loc[(stf, 'FRA', 'Hydro'), 'cap-up'] *= 0.5  # Original Value NorthGermany
#         pro.loc[(stf, 'FRA', 'Biomass'), 'cap-up'] *= 0.25  # Original Value NorthGermany
#         pro.loc[(stf, 'LUX', 'Hydro'), 'cap-up'] *= 0.5  # Original Value NorthGermany
#         pro.loc[(stf, 'LUX', 'Biomass'), 'cap-up'] *= 0.25  # Original Value NorthGermany
#         pro.loc[(stf, 'NLD', 'Hydro'), 'cap-up'] *= 0.5  # Original Value NorthGermany
#         pro.loc[(stf, 'NLD', 'Biomass'), 'cap-up'] *= 0.25  # Original Value NorthGermany
#         pro.loc[(stf, 'POL', 'Hydro'), 'cap-up'] *= 0.5  # Original Value NorthGermany
#         pro.loc[(stf, 'POL', 'Biomass'), 'cap-up'] *= 0.25  # Original Value NorthGermany
#     return data

def scenario_no_ccs(data):
    #set max cap up of CCS plants to zero
    pro=data['process']
    for stf in data['global_prop'].index.levels[0].tolist():
        pro.loc[(stf, 'DEU', 'procAmm_Coal_CCS'), 'cap-up'] = 0
        pro.loc[(stf, 'DEU', 'procAmm_NG_CCS'), 'cap-up'] = 0
    return data

def scenario_no_dsm(data):
    # empty the DSM dataframe completely
    data['dsm'] = pd.DataFrame()
    return data


def scenario_all_together(data):
    # combine all other scenarios
    data = scenario_stock_prices(data)
    data = scenario_co2_limit(data)
    #data = scenario_europe_process_caps(data)
    return data
