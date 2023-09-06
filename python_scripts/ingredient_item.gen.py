import json
import os


def get_user_input(prompt):
    return input(prompt).strip()


def create_directory_if_not_exists(directory):
    os.makedirs(directory, exist_ok=True)


def save_json_to_file(data, file_path):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=2)


# Get user input
file_name = get_user_input("Enter file name: ")
ingredient = get_user_input("Enter the ingredient for the recipe: ")

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

# Specify the output directory for items
output_directory = os.path.join(
    r'C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\BP\items\ingredient_items')

create_directory_if_not_exists(output_directory)

# Save the JSON item file in the specified directory
item_json_file_path = os.path.join(output_directory, f"{file_name}.json")
save_json_to_file(item_template, item_json_file_path)

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

# Specify the output directory for recipes
recipe_output_directory = os.path.join(
    r'C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\BP\recipes')

create_directory_if_not_exists(recipe_output_directory)

# Save the JSON recipe file in the specified directory
recipe_json_file_path = os.path.join(
    recipe_output_directory, f"{file_name}_recipe.json")
save_json_to_file(recipe_template, recipe_json_file_path)

print(
    f'JSON recipe file "{file_name}_recipe.json" has been created in the directory "{recipe_output_directory}".')

# Modify the file_name to have spaces between words and capitalize the second word
formatted_file_name = ' '.join(word.capitalize()
                               for word in file_name.replace('_', ' ').split())

# Specify the line number to insert the text (e.g., line 6)
line_number = 6

# Append data to another file at the specified line
additional_data_file_path = os.path.join(
    r'C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\RP\textures\item_texture.json')

with open(additional_data_file_path, "r") as data_file:
    lines = data_file.readlines()

# Insert the new data at the specified line, replacing "pumpkin_soup" with the file name
lines.insert(line_number - 1,
             f'\n"{file_name}": {{\n  "textures": "textures/items/ingredient_item_textures/{file_name}"\n}},\n')

# Write the modified content back to the file
with open(additional_data_file_path, "w") as data_file:
    data_file.writelines(lines)

print(f'Data appended to line {line_number} in "{additional_data_file_path}".')

# Append data to another file (en_US.lang) with capitalized text
lang_file_path = os.path.join(
    r'C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\RP\texts\en_US.lang')

with open(lang_file_path, "a") as lang_file:
    lang_file.write(f'\nitem.item:{file_name.lower()}={formatted_file_name}\n')

print(f'Data appended to "{lang_file_path}".')
