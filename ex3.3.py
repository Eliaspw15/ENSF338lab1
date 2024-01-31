import timeit
import json
from matplotlib import pyplot as plt
import numpy as np

file_path = 'large-file.json'  
with open(file_path, 'r') as file:
            data = json.load(file)

def modify_json_size(data, new_size=35):
    for record in data:
        record['size'] = new_size


modify_json_size(data)


elapsed_time = []

for i in range(1000):
    elapsed_time.append(timeit.timeit(lambda: modify_json_size(data, new_size=1000), number=1))

plt.hist(elapsed_time)
plt.title("Histogram of Processing Time ")
plt.ylabel("Occurance")
plt.xlabel("Processing Time")

plt.show()
