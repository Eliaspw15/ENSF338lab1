def merge_sort(arr, low, high)
    if low < high:
            mid = (low+high)//2
            merge_sort(arr, low, mid)       #low half array
            merge_sort(arr, mid+1, high)    #high half array
            merge(arr, low, mid, high)      #merge the two halves

def merge(a_arr, a_low, a_mid, a_high):     
      
      merge_arr = a_arr[]

      #at the last iter, this should read 2 values
      #read which is higher
      #merge them in order in a new (temp) array of 2
      #return that ordered array of 2
      #future iters with more than two values need to 
      #compare say an array of 3 with an array of 2 and
      #place elements of that both arrays in order but how? 

      #need to track on paper to figure out