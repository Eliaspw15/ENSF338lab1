import json
import time
import matplotlib.pyplot as plt

def binary_search(arr, target, initial_mid_ratio=0.5):
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    initial_mid = int(left + (right - left) * initial_mid_ratio)
    
    if arr[initial_mid] == target:
        return initial_mid
    elif arr[initial_mid] < target:
        left = initial_mid + 1
    else:
        right = initial_mid - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def time_searches(data, tasks):
    midpoints = [0, 0.25, 0.5, 0.75, 1.0]  # Different ratios to test
    results = []

    for task_id, target in enumerate(tasks):
        numbers = sorted(data)  # Ensure data is sorted
        task_results = {'task_id': task_id, 'best_time': float('inf'), 'best_midpoint': None}

        for midpoint in midpoints:
            start_time = time.time()
            binary_search(numbers, target, initial_mid_ratio=midpoint)
            elapsed_time = time.time() - start_time

            if elapsed_time < task_results['best_time']:
                task_results['best_time'] = elapsed_time
                task_results['best_midpoint'] = midpoint
        
        results.append(task_results)
    return results

# Load your data and tasks from the JSON files
data = load_json_file('/Users/josh.geng/code/ENSF338/ENSF338lab1/ENSF338lab1/Lab 3/ex7data.json')
tasks = load_json_file('/Users/josh.geng/code/ENSF338/ENSF338lab1/ENSF338lab1/Lab 3/ex7tasks.json')

# Time the searches and find the best midpoint for each task
results = time_searches(data, tasks)

# Example: Print the results
for result in results:
    print(f"Task ID: {result['task_id']}, Best Midpoint: {result['best_midpoint']}, Time: {result['best_time']}")

# Extract data for plotting
task_ids = [result['task_id'] for result in results]
best_midpoints = [result['best_midpoint'] for result in results]

# Plotting the scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(task_ids, best_midpoints, marker='o')
plt.xlabel('Task ID')
plt.ylabel('Best Midpoint')
plt.title('Best Midpoint for Each Task')
plt.xticks(task_ids)
plt.grid(True)
plt.show()

#Question 4. 
#The scatter plot depicting each task and its corresponding chosen midpoint reveals some variability in the performance 
# sensitivity to the initial midpoint choice. While there are discernible fluctuations in the best midpoint chosen for 
# different tasks, the overall impact on performance seems to vary. Several factors likely contribute to this 
# observation, including the distribution of data within each task, the size of the arrays, and the nature of the target 
# values. Data distribution could influence the optimal midpoint choice, especially if the target value is situated closer 
# to one end of the array. Furthermore, smaller arrays might be less sensitive to the initial midpoint choice compared to 
# larger arrays. The nature of the targets, whether uniformly distributed or randomly scattered, could also influence the 
# impact of the initial midpoint choice on performance. Further analysis and experimentation could provide deeper insights 
# into the relationship between the initial midpoint choice and search performance.
