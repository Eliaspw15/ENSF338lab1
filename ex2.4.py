import timeit

def avg_vowels(arr):
    
    vowel = 0
    avg = 0
    words = 0
    for i in range(len(line_array)):
        if i >= 842: #finds line 842 then starts operation
            for x in range(len(line_array[i])): #goes through each charachter in string
                if line_array[i][x] not in consonants: #if consonant increase count
                    vowel+=1            
                if line_array[i][x] == " ": #space indicates the word count 
                    words += 1

    avg = vowel/words

consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWZ" #initialized all consonants

line_array = [] #line
#need to start recording once CHAPTER 1. Loomings which is at position 843 so 842 since starting at 0
with open ('pg2701.txt') as my_file:
    line_array = my_file.readlines()


avg_vowels(line_array)


elapsed_time = []

elapsed_time.append(timeit.timeit(lambda: avg_vowels(line_array), number=100))

avg_time = elapsed_time[0]/100
print(f'Average time to compute average number of vowels per word: {avg_time} seconds')


