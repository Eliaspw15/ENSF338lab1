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
avg_times = []
elapsed_time.append(timeit.timeit(lambda: modify_json_size(data,new_size = 1000), number=100))
elapsed_time.append(timeit.timeit(lambda: modify_json_size(data,new_size = 2000), number=100))
elapsed_time.append(timeit.timeit(lambda: modify_json_size(data,new_size = 5000), number=100))
elapsed_time.append(timeit.timeit(lambda: modify_json_size(data,new_size = 10000), number=100))

avg_times.append(elapsed_time[0]/100)
avg_times.append(elapsed_time[1]/100)
avg_times.append(elapsed_time[2]/100)
avg_times.append(elapsed_time[3]/100)
listlengths = [1000,2000,5000,10000]
print(f'Average time (1000 records): {avg_times[0]} seconds')
print(f'Average time (2000 records): {avg_times[1]} seconds')
print(f'Average time (5000 records): {avg_times[2]} seconds')
print(f'Average time (10000 records): {avg_times[3]} seconds')

slope, intercept = np.polyfit(listlengths, avg_times, 1)
plt.scatter(listlengths,avg_times)
linevalues = [slope * x + intercept for x in listlengths]
plt.plot(listlengths,linevalues,'r')
plt.title("Average Processing Time vs Number of Records")
plt.ylabel("Average Processing Time")
plt.xlabel("Number of Records")

plt.show()

print("the linear model is: t = %.2e * n + %.2e" % (slope, intercept))
