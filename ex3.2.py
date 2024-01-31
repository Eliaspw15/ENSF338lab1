import timeit
import json
from matplotlib import pyplot as plt
import numpy as np

def load_json(file_path, num_records=1):
    try:
        # Load JSON data from file
        with open(file_path, 'r') as file:
            data = json.load(file)[:num_records]

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON in file - {file_path}")
    except Exception as e:
        print(f"Error: {e}")

file_path = 'large-file.json'

elapsed_time = []
avg_times = []
elapsed_time.append(timeit.timeit(lambda: load_json(file_path, num_records=1000), number=100))
elapsed_time.append(timeit.timeit(lambda: load_json(file_path, num_records=2000), number=100))
elapsed_time.append(timeit.timeit(lambda: load_json(file_path, num_records=5000), number=100))
elapsed_time.append(timeit.timeit(lambda: load_json(file_path, num_records=10000), number=100))

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
