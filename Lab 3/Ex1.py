def merge_sort(arr, low, high):
    if low < high:
            mid = (low+high)//2
            merge_sort(arr, low, mid)       #low half array
            merge_sort(arr, mid+1, high)    #high half array
            merge(arr, low, mid, high)      #merge the two halves
            

def merge(arr, low, mid, high):     #chatgpt 3.5 was used to understand the tracking of the array and better understand the recursive nature of the merge_sort function and how and when it actually used the merge function
    low_half = arr[low:mid + 1]
    high_half = arr[mid + 1:high + 1]

    i = j = 0
    k = low

    while i < len(low_half) and j < len(high_half):
        if low_half[i] <= high_half[j]: 
            arr[k] = low_half[i]
            i += 1
        else:
            arr[k] = high_half[j]
            j += 1
        k += 1

    while i < len(low_half):
        arr[k] = low_half[i]
        i += 1
        k += 1

    while j < len(high_half):
        arr[k] = high_half[j]
        j += 1
        k += 1

test_arr = [8, 42, 25, 3, 3, 2, 27, 3]
merge_sort(test_arr, 0, 7)
print(test_arr)

