# 1. Compare advantages and disadvantages of arrays vs linked list (complexity of task completion) [0.1 pts]

# Arrays are indexable, this means you can easily access elements at any point in the array allowing for efficient random access
# In some languages, array length is fixed upon instantiation which creates situation in which arrays are limited, or take 
# excess space. Additionally, a counter-effect of arrays being indexable is that their positions are significant, therefore,
# adding or removing elements involves shifting subsequent elements right or left respectively. As a result, adding or removing
# the first element can create a considerably high complexity task.

# Linked Lists are not indexable making random access to elements quite difficult. Moreover, even access to the last element can 
# be a costly operation without the inclusion of a tail pointer. However, due to the sequence based nature of Linked Lists, 
# inserting and deleting elements is a much less complex task as it simply requires a re-assignment of pointers (of the predecessor
# and successor) rather than a complete shift of elements- in regards to the previous point regarding tail pointers, without this, 
# inserting or deleting the last element is a scenario in which insertion or deletion is less complex in Arrays. Lastly, 
# linked lists can be expanded or shrunk without restrictions 


# 2. For arrays, we are interested in implementing a replace function
# that acts as a deletion followed by insertion. How can this function
# be implemented to minimize the impact of each of the standalone
# tasks? [0.1 pts]
