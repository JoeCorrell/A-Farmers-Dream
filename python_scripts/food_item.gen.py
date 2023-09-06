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
        "description": {"identifier": f"item:{file_name}"},
        "components": {
            "tag:stove_recipes": {},
            "minecraft:icon": {"texture": file_name},
            "minecraft:use_duration": 1.6,
            "minecraft:use_animation": "eat",
            "minecraft:food": {
                "nutrition": nutrition,
                "saturation_modifier": saturation_modifier,
            },
        },
        "events": {},
    },
}

# Add "using_converts_to" if provided
if converts_to_item:
    item_template["minecraft:item"]["components"]["minecraft:food"]["using_converts_to"] = converts_to_item

# Specify the directory where the JSON files will be generated
output_directory = r'C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\BP\items\food_items'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Save the JSON item file in the specified directory
item_json_file_path = os.path.join(output_directory, f"{file_name}.json")
with open(item_json_file_path, "w") as json_file:
    json.dump(item_template, json_file, indent=2)

print(
    f'JSON file "{file_name}.json" has been created in the directory "{output_directory}".')

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
recipe_output_directory = r'C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\BP\recipes'

# Ensure the recipe output directory exists
os.makedirs(recipe_output_directory, exist_ok=True)

# Save the JSON recipe file in the specified directory
recipe_json_file_path = os.path.join(
    recipe_output_directory, f"{file_name}_recipe.json")
with open(recipe_json_file_path, "w") as json_file:
    json.dump(recipe_template, json_file, indent=2)

print(
    f'JSON recipe file "{file_name}_recipe.json" has been created in the directory "{recipe_output_directory}".')

# Modify the file_name to have spaces between words and capitalize the second word
lang_entry = file_name.replace('_', ' ').replace(' ', '_').title()

# Specify the line number to insert the text (e.g., line 6)
line_number = 6

# Append data to another file at the specified line
additional_data_file_path = r'C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\RP\textures\item_texture.json'
with open(additional_data_file_path, "r") as data_file:
    lines = data_file.readlines()

# Insert the new data at the specified line, replacing "pumpkin_soup" with the file name
lines.insert(line_number - 1,
             f'\n"{file_name}": {{\n  "textures": "textures/items/food_item_textures/{file_name}"\n}},\n')

# Write the modified content back to the file
with open(additional_data_file_path, "w") as data_file:
    data_file.writelines(lines)

print(f'Data appended to line {line_number} in "{additional_data_file_path}".')

lang_entry = ' '.join(word.capitalize()
                      for word in file_name.replace('_', ' ').split())

# Append data to another file (en_US.lang) with capitalized text
lang_file_path = r'C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\RP\texts\en_US.lang'
with open(lang_file_path, "a") as lang_file:
    lang_file.write(
        f'\nitem.item:{file_name.lower()}={lang_entry}\n')

print(f'Data appended to "{lang_file_path}".')
