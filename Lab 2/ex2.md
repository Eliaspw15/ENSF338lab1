def interpolation_search(arr, x):
low = 0
high = len(arr) - 1
while low <= high and x >= arr[low] and x <= arr[high]:
pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
if arr[pos] == x:
return pos
if arr[pos] < x:
low = pos + 1
else:
high = pos - 1
return -1

1.) Interpolation search is better when array is sorted and uniformly distributed. average time complexity of interpolation search is O(log log n) whereas Binary's average time complexity is O(Log n), meaning interpolation is faster under the right conditions.

2.) if the array is not uniformily distributed then the efficiency will most likely decrease.
This is because it cant estimate target position precisely if its not uniformly distributed, this means that it would take
longer to find result or give wrong result

3.)line 5 would be affected

HELP FROM CHAT GPT
4.)Linear search would be your only option if the data is unsorted, interpolation may fail for the reasons in Question 2

5.)Linear will outperform binary and interpolation search when the data set is small. this is because it can go through all items in data set quickly without having a more complex search method like interpolation and binary

6.) It would be better if you could split the dataset into more optimal containers instead of just in half.


