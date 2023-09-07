import json
import os

# Get user input
file_name = input("Enter file name: ")
nutrition = int(input("Enter the nutrition value: "))
saturation_modifier = int(input("Enter the saturation value: "))

# Ask the player if they want to add "using_converts_to" and get their input
add_converts_to = input(
    "Do you want to add 'using_converts_to'? (yes/no): ").lower() == "yes"
converts_to_item = None

# If the player wants to add "using_converts_to," ask for the item to convert to
if add_converts_to:
    converts_to_item = input("Enter the item to convert to: ")

# Ask for the ingredient
ingredient = input("Enter the ingredient for the recipe: ")

# Define the JSON item template
item_template = {
    "format_version": "1.20.0",
    "minecraft:item": {
        "description": {
            "identifier": f"item:{file_name}"
        },
        "components": {
            "minecraft:icon": {
                "texture": f"{file_name}"
            }
        }
    }
}

# Add "using_converts_to" if provided
if converts_to_item:
    item_template["minecraft:item"]["components"]["minecraft:food"]["using_converts_to"] = converts_to_item

# Specify the directory where the JSON files will be generated
output_directory = r'C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\BP\items\food_items'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Save the JSON item file in the specified directory, overwriting if it exists
item_json_file_path = os.path.join(output_directory, f"{file_name}.item.json")
with open(item_json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(item_template, json_file, indent=2)

print(
    f'JSON file "{file_name}.json" has been created or overwritten in the directory "{output_directory}".')

# Define the JSON recipe template
recipe_template = {
    "format_version": "1.20.0",
    "minecraft:recipe_shaped": {
        "description": {
            "identifier": f"item:{file_name}"
        },
        "priority": 0,
        "tags": ["crafting_table"],
        "pattern": ["LLL", "LCL", "LCL"],
        "key": {
            "L": {"item": ingredient}
        },
        "result": f"item:{file_name}"
    }
}

# Specify the directory where the recipe JSON file will be generated
recipe_output_directory = r'C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\BP\recipes\food_item_recipes'

# Ensure the recipe output directory exists
os.makedirs(recipe_output_directory, exist_ok=True)

# Save the JSON recipe file in the specified directory, overwriting if it exists
recipe_json_file_path = os.path.join(
    recipe_output_directory, f"{file_name}.recipe.json")
with open(recipe_json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(recipe_template, json_file, indent=2)

print(
    f'JSON recipe file "{file_name}_recipe.json" has been created or overwritten in the directory "{recipe_output_directory}".')

# Modify the file_name to have spaces between words and capitalize the second word
lang_entry = file_name.replace('_', ' ').replace(' ', '_').title()

# Specify the line number to insert the text (e.g., line 6)
line_number = 6

# Append or replace data in the texture file
additional_data_file_path = r'C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\RP\textures\item_texture.json'
with open(additional_data_file_path, "r", encoding="utf-8") as data_file:
    lines = data_file.readlines()

# Check if the data already exists
data_exists = False
for index, line in enumerate(lines):
    if line.strip() == '"texture_data": {':
        lines.insert(index + 1, f'    "{file_name}": {{\n')
        lines.insert(
            index + 2, f'      "textures": "textures/items/food_item_textures/{file_name}"\n')
        lines.insert(index + 3, f'    }},\n')
        data_exists = True
        break

# If the data doesn't exist, insert it
if not data_exists:
    # Handle the case where "texture_data" does not exist at all
    lines.append('\n  "texture_data": {\n')
    lines.append(f'    "{file_name}": {{\n')
    lines.append(
        f'      "textures": "textures/items/food_item_textures/{file_name}"\n')
    lines.append('    },\n')
    lines.append('  },\n')

# Write the modified content back to the file
with open(additional_data_file_path, "w", encoding="utf-8") as data_file:
    data_file.writelines(lines)

print(f'Data appended or replaced in "{additional_data_file_path}".')

lang_entry = ' '.join(word.capitalize()
                      for word in file_name.replace('_', ' ').split())

# Append or replace data in the lang file
lang_file_path = r'C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\RP\texts\en_US.lang'

# Read existing data from the lang file
with open(lang_file_path, "r", encoding="utf-8") as lang_file:
    lang_lines = lang_file.readlines()

# Flag to check if the line already exists
line_exists = False

# Iterate through existing lines and check if the line exists
for index, line in enumerate(lang_lines):
    if line.startswith(f'item.item:{file_name.lower()}='):
        lang_lines[index] = f'item.item:{file_name.lower()}={lang_entry}\n'
        line_exists = True
        break

# If the line doesn't exist, append it
if not line_exists:
    lang_lines.append(f'item.item:{file_name.lower()}={lang_entry}\n')

# Write the modified content back to the file
with open(lang_file_path, "w", encoding="utf-8") as lang_file:
    lang_file.writelines(lang_lines)

print(f'Data appended or replaced in "{lang_file_path}".')
