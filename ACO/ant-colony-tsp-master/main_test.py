from statistics import mean, median
import json as np
import json
from main_aco import main_aco
from getFiles import getFiles
from datetime import datetime
from main_anneal import main_anneal
from main_genetic import main_genetic
from convertToCsv import convertCSV


# define folder where the files should be collected from
folderPath = "./data/source_data/";
files = getFiles(folderPath)


filename = "./data/output/output.json"
listObj = []

# Read JSON file
with open(filename) as fp:
  listObj = json.load(fp)

for file in files:
    aco = []
    aco_duration = []
    ga = []
    ga_duration = []
    sim = []
    sim_duration = []

    for x in range(1):
        print(folderPath + file)
        localLog = [];
        # record timestamp as soon as alg. started
        start_aco = datetime.utcnow();
        # run ACO algorithm for the current file
        cost_aco = main_aco(folderPath + file)
        aco.append(cost_aco)
        # record timestamp as soon as the alg. ended
        end_aco = datetime.utcnow();
        # record timestamp as soon as alg. started
        start_sim = datetime.utcnow();
        # run simulated annealing algorithm for the current file
        cost_sim = main_anneal(folderPath + file)
        sim.append(cost_sim)
        # record timestamp as soon as the alg. ended
        end_sim = datetime.utcnow();
        # record timestamp as soon as alg. started
        start_ga = datetime.utcnow();
        # run simulated annealing algorithm for the current file
        cost_ga = main_genetic(folderPath + file)
        ga.append(cost_ga)
        # record timestamp as soon as the alg. ended
        end_ga = datetime.utcnow();
        #calculate duration
        duration_aco = end_aco - start_aco
        aco_duration.append(duration_aco.total_seconds())
        #calculate duration
        duration_sim = end_sim - start_sim
        sim_duration.append(duration_sim.total_seconds())
        #calculate duration
        duration_ga = end_ga - start_ga
        ga_duration.append(duration_ga.total_seconds())
    
    #log to file
    target = 0
    if file == "eil51.txt":
        target = 426
    elif file == "berlin52.txt":
        target = 7542    
    elif file == "eil101.txt":
        target = 629
    elif file == "ch150.txt":
        target = 6528
    elif file == "rd400.txt":
        target = 15281
    elif file == "pcb442.txt":
        target = 50778

    listObj.append({
        "file": file,
        "target": target,
        "mean_aco": mean(aco),
        "mean_sim": mean(sim),
        "mean_ga": mean(ga),
        "dev_abs_aco": abs(target - mean(aco)),
        "dev_abs_sim": abs(target - mean(sim)),
        "dev_abs_ga": abs(target - mean(ga)),
        "dev_percent_aco": (mean(aco) - target) / target * 100,
        "dev_percent_sim": (mean(sim) - target) / target * 100,
        "dev_percent_ga": (mean(ga) - target) / target * 100,
        "duration_aco": str(mean(aco_duration)),
        "duration_sim": str(mean(sim_duration)),
        "duration_ga": str(mean(ga_duration))
    })

with open(filename, 'w') as json_file:
    json.dump(listObj, json_file, 
                        indent=4,  
                        separators=(',',': '))

convertCSV();

