file_path = 'large-file.json'  
with open(file_path, 'r') as file:
            data = json.load(file)

def modify_json_size(data, new_size=35):
    for record in data:
        record['size'] = new_size


modify_json_size(data)