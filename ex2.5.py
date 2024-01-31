# Used ChatGPT to write modify_json_size()
import timeit
import json

def modify_json_size(data, new_size=35):
    for record in data:
        record['size'] = new_size


file_path = 'large-file.json'  

elapsed_time = timeit.timeit(lambda: modify_json_size(file_path), number=10)
print(f'Elapsed time: {elapsed_time} seconds')
