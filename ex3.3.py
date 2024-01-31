import timeit
import json
from matplotlib import pyplot as plt
import numpy as np

def load_json(file_path, new_size=35,num_records=1):
    try:
        # Load JSON data from file
        with open(file_path, 'r') as file:
            data = json.load(file)[:num_records]
        
         for record in data:
            record['size'] = new_size

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON in file - {file_path}")
    except Exception as e:
        print(f"Error: {e}")

file_path = 'large-file.json'

elapsed_time = []

for i in range(1000):
    elapsed_time.append(timeit.timeit(lambda: load_json(file_path, num_records=1000), number=1))

plt.hist(elapsed_time)
plt.title("Histogram of Processing Time ")
plt.ylabel("Occurance")
plt.xlabel("Processing Time")

plt.show()
