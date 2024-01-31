consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWZ"

line_array = []
#need to start recording once CHAPTER 1. Loomings
with open ('pg2701.txt') as my_file:
    line_array = my_file.readlines()

counter = 0
consonant = 0
avg = 0
words = 0
for i in range(len(line_array)):
    if i >= 843:
        counter += 1
        count = 0
        for x in range(len(line_array[i])):
            if line_array[i][count] in consonants:
                consonant+=1            
            if line_array[i][count] == " ":
                words += 1
            count += 1 


avg = consonant/words

print(avg)

        
