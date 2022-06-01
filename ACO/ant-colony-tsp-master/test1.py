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


for file in files:
    print(folderPath + file)
    localLog = [];

    # record timestamp as soon as alg. started
    start_aco = datetime.utcnow();
    # run ACO algorithm for the current file
    cost_aco = main_aco(folderPath + file)
    # record timestamp as soon as the alg. ended
    end_aco = datetime.utcnow();

    # record timestamp as soon as alg. started
    start_sim = datetime.utcnow();
    # run simulated annealing algorithm for the current file
    cost_sim = main_anneal(folderPath + file)
    # record timestamp as soon as the alg. ended
    end_sim = datetime.utcnow();

    # record timestamp as soon as alg. started
    start_ga = datetime.utcnow();
    # run simulated annealing algorithm for the current file
    cost_ga = main_genetic(folderPath + file)
    # record timestamp as soon as the alg. ended
    end_ga = datetime.utcnow();

    # add log information to localLog
    localLog.append(file)
    localLog.append(str(cost_aco))
    localLog.append(str(cost_sim))
    localLog.append(str(cost_ga))

    duration_aco = end_aco - start_aco
    localLog.append(str(duration_aco.total_seconds()))

    duration_sim = end_sim - start_sim
    localLog.append(str(duration_sim.total_seconds()))

    duration_ga = end_ga - start_ga
    localLog.append(str(duration_ga.total_seconds()))

    a_file = open("./data/output/output.txt", "a")
    content = str(localLog)
    a_file.write(content + "\n")
    a_file.close()

    # add localLog to log array
    log.append(localLog)


for entry in log:
    print(str(entry))


print(log)
