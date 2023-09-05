import json
import os

# List of wood types
wood_types = [
    "oak", "dark_oak", "mangrove", "birch",
    "acacia", "cherry", "warped", "spruce", "crimson", "jungle",  "stripped_oak", "stripped_dark_oak", "stripped_mangrove", "stripped_birch",
    "stripped_acacia", "stripped_cherry", "stripped_warped", "stripped_spruce", "stripped_crimson", "stripped_jungle"
]

# Load data from the JSON file
json_file_path = os.path.join(os.path.dirname(__file__), "wood_data.json")

try:
    with open(json_file_path, 'r') as json_file:
        wood_data = json.load(json_file)
except FileNotFoundError:
    print(f"Could not find the 'wood_data.json' file in the script's folder.")
    exit()

# Create a directory to store the JSON files (if it doesn't exist)
if not os.path.exists('script_generated_files'):
    os.mkdir('script_generated_files')

# Generate and save JSON files with wood type names as filenames and data from the loaded JSON
for wood_type in wood_types:
    if wood_type in wood_data:
        file_name = f'script_generated_files/kitchen_cutting_board_{wood_type}.loot.json'
        data = wood_data[wood_type]

        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print(
            f'File {wood_type}.loot.json created with data from the JSON file.')
    else:
        print(f'Warning: No data found for {wood_type} in the JSON file.')
