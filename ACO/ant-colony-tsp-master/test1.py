from statistics import mean, median
import numpy as np
from main_aco import main_aco
from getFiles import getFiles
from datetime import datetime
from main_anneal import main_anneal
from main_genetic import main_genetic


# define folder where the files should be collected from
folderPath = "./data/small/";
files = getFiles(folderPath)
log = [];

a_file = open("./data/output/output.txt", "a")
a_file.truncate()
a_file.close()

aco = []
aco_duration = []
ga = []
ga_duration = []
sim = []
sim_duration = []

for file in files:
    for x in range(2):
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
    localLog.append(file)
    localLog.append(mean(aco))
    localLog.append(mean(sim))
    localLog.append(mean(ga))
    localLog.append(str(mean(aco_duration)))
    localLog.append(str(mean(sim_duration)))
    localLog.append(str(mean(ga_duration)))
    a_file = open("./data/output/output.txt", "a")
    content = str(localLog)
    a_file.write(content + "\n")
    a_file.close()

for entry in log:
    print(str(entry))

print(log)
