import json

json_log = json.loads(open("./data/output/output.json", "r").read())
filename = "./data/output/output.json"

listObj = []

# Read JSON file
with open(filename) as fp:
  listObj = json.load(fp)

# listObj.append({
#       "file": "A",
#       "mean_aco": "A",
#       "mean_sim": "s",
#       "mean_ga": "s",
#       "duration_aco": "s",
#       "duration_sim": "s",
#       "duration_ga": "s"
#     }
# )

print(listObj[0])

with open(filename, 'w') as json_file:
    json.dump(listObj, json_file, 
                        indent=4,  
                        separators=(',',': '))

