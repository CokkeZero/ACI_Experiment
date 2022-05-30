import numpy as np
from main import main
from getFiles import getFiles
from datetime import datetime

# define folder where the files should be collected from
folderPath = 'data/small/';
files = getFiles(folderPath)
log = [];

a_file = open("data/output/output.txt", "a")
a_file.truncate()
a_file.close()


for file in files:
    print(folderPath + file)

    localLog = [];

    # record timestamp as soon as alg. started
    start = datetime.utcnow();

    # run ACO algorithm for the current file
    costACO = main(folderPath + file)

    # run GA algorithm for the current file
    costGA = 'unknown' # main(folderPath + file)

    # record timestamp as soon as the alg. ended
    end = datetime.utcnow();

    # add log information to localLog
    localLog.append(file)
    localLog.append(str(costACO))
    localLog.append(str(costGA))

    duration = end - start
    localLog.append(str(duration.total_seconds()))

    a_file = open("data/output/output.txt", "a")
    content = str(localLog)
    a_file.write(content + "\n")
    a_file.close()

    # add localLog to log array
    log.append(localLog)


for entry in log:
    print(str(entry))


print(log)
