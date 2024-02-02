def func(n):
if n == 0 or n == 1:
return n
else:
return func(n-1) + func(n-2) 
#this is fibonacci sequence

#yes this is a divide and conquer algorithm. it is just innefficient
#this has a time complexity of O(n^2) and is therefore quadratic

array = []

