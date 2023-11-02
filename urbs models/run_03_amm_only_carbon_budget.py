import os
import shutil
import urbs
from datetime import date


input_files = "DE_amm_only_CB.xlsx"
input_dir = 'Input'
input_path = os.path.join(input_dir, input_files)

result_name = 'Amm_only_CB'
result_dir = urbs.prepare_result_directory(result_name)  # name + time stamp

#get year
#year = 2050
year = date.today().year

# copy input file to result directory
try:
    shutil.copytree(input_path, os.path.join(result_dir, input_dir))
except NotADirectoryError:
    shutil.copyfile(input_path, os.path.join(result_dir, input_files))
# copy run file to result directory
shutil.copy(__file__, result_dir)

# objective function
objective = 'cost'  # set either 'cost' or 'CO2' as objective

# Choose Solver (cplex, glpk, gurobi, ...)
solver = 'gurobi'

# simulation timesteps
(offset, length) = (0, 8760)  # time step selection
timesteps = range(offset, offset+length+1)
dt = 1  # length of each time step (unit: hours)

# detailed reporting commodity/sitesd
report_tuples = [
    (2050, 'DEU', 'Elec'),
    (2050, 'DEU', 'H2'),
    # (2050, 'DEU', 'Heat_Q1'),
    # (2050, 'DEU', 'Heat_Q2'),
    # (2050, 'DEU', 'Heat_Q3'),
    # (2050, 'DEU', 'Heat_Q4'),
    # (2050, 'DEU', 'HeatTokamak'),
    # (2050, 'DEU', 'HeatStellarator'),
    (2050, 'DEU', 'CO2'),
    (2050, 'DEU', 'Ammonia')
    # (2050, 'DEU', 'pt_car_pkm'),
    # (2050, 'DEU', 'pt_bus_pkm'),
    # (2050, 'DEU', 'ft_road_tkm')
]

# optional: define names for sites in report_tuples
#report_sites_name = { }
report_sites_name = {

}

# plotting commodities/sites
plot_tuples = [

]
# optional: define names for sites in plot_tuples
plot_sites_name = {
   
    }

# plotting timesteps
plot_periods = {
    #'all': timesteps[1:]
}

# add or change plot colors
my_colors = {

    }
for country, color in my_colors.items():
    urbs.COLORS[country] = color

# select scenarios to be run
scenarios = [
             urbs.scenario_base,
             urbs.scenario_co2_limit_50,
             urbs.scenario_co2_limit_80,
             urbs.scenario_co2_limit_0
            #  urbs.scenario_stock_prices,
             # urbs.scenario_co2_limit,

            ]

for scenario in scenarios:
    prob = urbs.run_scenario(input_path, solver, timesteps, scenario,
                             result_dir, dt, objective,
                             plot_tuples=plot_tuples,
                             plot_sites_name=plot_sites_name,
                             plot_periods=plot_periods,
                             report_tuples=report_tuples,
                             report_sites_name=report_sites_name)
