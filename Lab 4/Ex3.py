#Identify and explain the strategy used to grow arrays when full, with
#references to specific lines of code in the file above. What is the
#growth factor?

#When the array is full. the compiler allocates more space than what is 
#needed to prepare incase more space is required in the future. this is referenced
#in line 70. it shows that the The growth factor is (newsize >> 3) + 6

import sys
import timeit
import matplotlib.pyplot as plt
# Initial capacity of an empty list
initial_capacity = sys.getsizeof([])

my_list = []

# capacity at start
current_capacity = initial_capacity // 4  # Dividing by 4 bytes because an int is 4 bytes
S = 0
for i in range(64):
    my_list.append(i)
    
    # if capacity changes 
    if sys.getsizeof(my_list)//4 != current_capacity:
        S = i
        # Prints when capacity of list changes
        print(f"Capacity changed at {i+1} elements: {current_capacity * 4} -> {sys.getsizeof(my_list)}")
        
        # Update the current capacity
        current_capacity = sys.getsizeof(my_list) //4 #4 because an integer is 4 bytes


#help from chat gpt
def S_to_S_plus_1(S):
    my_list = list(range(S))
    current_capacity = initial_capacity // 4  # Dividing by 4 bytes because an int is 4 bytes
    time_taken = timeit.timeit(lambda: my_list.append(0), number=1000)
    return time_taken

def S_minus_1_to_S(S):
    my_list = list(range(S-1))
    current_capacity = initial_capacity // 4  # Dividing by 4 bytes because an int is 4 bytes
    time_taken = timeit.timeit(lambda: my_list.append(0), number=1000)
    return time_taken

# Largest array size is 53


# Measure the time taken to grow array from size 53 to 54
time_measurements_plus_1 = [S_to_S_plus_1(S) for i in range(1000)]

# Measure the time taken to grow array from size 52 to 53
time_measurements_minus_1 = [S_minus_1_to_S(S) for i in range(1000)]


plt.hist(time_measurements_plus_1,  alpha=0.5, label='S to S+1')
plt.hist(time_measurements_minus_1, alpha=0.5, label='S-1 to S')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Time vs frequency to add element to an array.')
plt.legend()
plt.show()

# the plot is very similar. this is because it does not take that much time 
#to change the size of the array because there are no other variables 
#taking up space in memory so it doesnt have to copy the array to another space in memory.