# 1. Compare advantages and disadvantages of arrays vs linked list (complexity of task completion) [0.1 pts]

# Arrays are indexable, this means you can easily access elements at any point in the array allowing for efficient random access. In some languages, array length is fixed upon instantiation which creates situation in which arrays are limited, or take excess space. Additionally, a counter-effect of arrays being indexable is that their positions are significant, therefore,adding or removing elements involves shifting subsequent elements right or left respectively. As a result, adding or removingthe first element can create a considerably high complexity task.

# Linked Lists are not indexable making random access to elements quite difficult. Moreover, even access to the last element can be a costly operation without the inclusion of a tail pointer. However, due to the sequence based nature of Linked Lists, inserting and deleting elements is a much less complex task as it simply requires a re-assignment of pointers (of the predecessorand successor) rather than a complete shift of elements- in regards to the previous point regarding tail pointers, without this, inserting or deleting the last element is a scenario in which insertion or deletion is less complex in Arrays. Lastly, linked lists can be expanded or shrunk without restrictions thus eliminating the problem of inadequate/excessive space allocated.


# 2. For arrays, we are interested in implementing a replace function that acts as a deletion followed by insertion. How can this function be implemented to minimize the impact of each of the standalone tasks? [0.1 pts]

# While it may function as a deletion followed by an insertion, it should not actually call those operations as it would be needlessly complex. Instead, it should take advantage of array indices and be a search and update function where the target element is found then the value is changed. 

# 3. Assuming you are tasked to implement a doubly linked list with a sort function, given the list of sort functions below, state the feasibility of using each one of them and elaborate why is it possible or not to use them.

# 3.1: An insertion sort is feasible as insertion sort requires access to an elements predecessor which a doubly-linked list would conveniently have access to.

# 3.2: A merge sort is feasible as dividing and conquering is entirely possible and not complex with a linked list as it does not require random access, the access required is precisely the middle. Additionally, the process of merging subarrays would be made simply by the aforementioned bidirectional access of doubly linked lists.

# 4.

# Insertion sort: The complexity would be O(n^2) in the worst and average case, where the input list is in the reverse or random order. These cases would result in each insertion requiring traversing up to the entire sorted portion of the list. Moreover, the worst case complexity would be the same for an array as the bidirectional access of the doubly-linked list makes its functionally similar to an array and the insertion sort algorithm inherently requires repeated traversal so indexability does not provide any advantage to an array implementation. For both implementations, the complexity would be O(n) in the best case (input is sorted) because this case eliminates the need for multiple iterations once the whole list has been traversed and none of the elements are identified to be out of order.

# Merge sort: The complexity would be O(n log n) in all cases. As previously mentioned the bidirectional access of the doubly-linked list gives it functional similarities to the array in some sorting cases. For merge sort, the process dividing the data into its individual elements (O(log n)) then merging them back together (O(n)) is consistent between the doubly linked list and array. However, it can be noted that the linked list does not require additional memory while the array would. This would not effect the time complexity but in regards to the overall nature of the respective implementations, demonstrates the advantage of the linked list implementation.


