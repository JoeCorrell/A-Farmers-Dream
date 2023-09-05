import json
import os

# List of wood types
foods = [
    " "
]

# Load data from the JSON file
json_file_path = os.path.join(os.path.dirname(__file__), "food_data.json")

try:
    with open(json_file_path, 'r') as json_file:
        food_data = json.load(json_file)
except FileNotFoundError:
    print(f"Could not find the 'food_data.json' file in the script's folder.")
    exit()

# Create a directory to store the JSON files (if it doesn't exist)
if not os.path.exists('script_generated_files'):
    os.mkdir('script_generated_files')

# Generate and save JSON files with wood type names as filenames and data from the loaded JSON
for food in foods:
    if food in food_data:
        file_name = f'script_generated_files/{food}.item.json'
        data = food_data[food]

        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print(
            f'File {food}.loot.json created with data from the JSON file.')
    else:
        print(f'Warning: No data found for {food} in the JSON file.')
