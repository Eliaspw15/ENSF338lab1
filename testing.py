import timeit
import json
data = 
def load_json(file_path, new_size=35, num_records=1):
    try:
        # Load JSON data from file
        with open(file_path, 'r') as file:
            data = json.load(file)[:num_records]
        
        for record in data:
            record['size'] = new_size

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON in file - {file_path}")
    except Exception as e:
        print(f"Error: {e}")
    return data

def iterate_records(data):
    for record in data:
        record['size'] = new_size

file_path = 'large-file.json'
num_records_list = [1000, 2000, 5000, 10000]

for num_records in num_records_list:
  # Reset data to avoid interference between iterations
    setup_code = f"from __main__ import load_json, iterate_records; data = load_json('{file_path}', num_records={num_records})"
    elapsed_time = timeit.timeit(lambda: iterate_records(data), setup=setup_code, number=10)
    avg_time = elapsed_time / 10  # Calculate average time per iteration
    print(f'Average time for {num_records} records: {avg_time} seconds')
