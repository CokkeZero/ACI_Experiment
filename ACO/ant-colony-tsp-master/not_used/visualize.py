import matplotlib.pyplot as plt
import json
import numpy as np

filename = "./data/output/output.json"
listObj = []

# Read JSON file
with open(filename) as fp:
  listObj = json.load(fp)
values = []

# some example data
threshold = listObj[0]["target"]
for x in listObj:
    values.append(x["mean_aco"])

values2 = np.array(values)
print(values)
print(threshold)

x = range(len(values2))

# split it up
above_threshold = np.maximum(values2 - threshold, 0)
below_threshold = np.minimum(values2, threshold)

# and plot it
fig, ax = plt.subplots()
ax.bar(x, below_threshold, 0.35, color="g")
ax.bar(x, above_threshold, 0.35, color="r",
        bottom=below_threshold)

# horizontal line indicating the threshold
ax.plot([0., 4.5], [threshold, threshold], "k--")

plt.show()

# x = np.linspace(-10, 1, 10)
# y1 = 2*x + 1
# y2 = 2**x + 1

# plt.figure(num = 3, figsize=(8, 5))
# plt.plot(x, y2)
# plt.plot(x, y1, 
#          color='red',   
#          linewidth=1.0,  
#          linestyle='--' 
#         )

# plt.show()




