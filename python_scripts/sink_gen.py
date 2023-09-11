import json
import os

# Function to create a directory if it doesn't exist


def create_directory_if_not_exists(directory):
    os.makedirs(directory, exist_ok=True)

# Function to save JSON data to a file with overwrite


def save_json_to_file(data, file_path, overwrite=True):
    mode = "w" if overwrite else "x" if not os.path.exists(file_path) else "a"
    with open(file_path, mode) as json_file:
        json.dump(data, json_file, indent=2)

# Function to add or replace a line in a text file


def add_or_replace_line(file_path, line_to_add_or_replace):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        lines = file.readlines()

    line_found = False
    for i, line in enumerate(lines):
        if line.strip().startswith(line_to_add_or_replace.split('=')[0]):
            lines[i] = line_to_add_or_replace + '\n'
            line_found = True
            break

    if not line_found:
        lines.append(line_to_add_or_replace + '\n')

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)


# Define the list of colors
colors = [
    "terracotta_black", "terracotta_green", "terracotta_blue", "terracotta_brown", "terracotta_gray", "terracotta_cyan", "terracotta_light_blue",
    "terracotta_light_gray", "terracotta_lime", "terracotta_magenta", "terracotta_orange", "terracotta_pink", "terracotta_purple",
    "terracotta_red", "terracotta_white", "terracotta_yellow",  "wood_oak", "wood_dark_oak", "wood_spruce", "wood_acacia", "wood_mangrove", "wood_cherry",
    "wood_bamboo", "wood_warped", "wood_crimson", "wood_birch", "wood_jungle",
    "wood_oak_stripped", "wood_dark_oak_stripped", "wood_spruce_stripped", "wood_acacia_stripped", "wood_mangrove_stripped", "wood_cherry_stripped",
    "wood_warped_stripped", "wood_crimson_stripped", "wood_birch_stripped", "wood_jungle_stripped"
]

# Specify the directory where files will be generated
base_output_directory = r"C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\BP\blocks\kitchen\furniture\sink"

for color in colors:
    # Define the JSON item template
    formatted_file_name = f"sink_{color}"
    block_template = {

    }

    # Specify the output directory for items
    output_directory = os.path.join(base_output_directory)

    create_directory_if_not_exists(output_directory)

    # Save the JSON item file in the specified directory, overwriting if it already exists
    item_json_file_path = os.path.join(
        output_directory, f"{formatted_file_name}.block.json")
    save_json_to_file(block_template, item_json_file_path, overwrite=True)

    print(f'JSON file "{item_json_file_path}" has been created.')

    # Modify the file_name to have spaces between words and capitalize the second word
    formatted_file_name_for_lang = " ".join(
        word.capitalize() for word in formatted_file_name.replace("_", " ").split())

    # Specify the line number to insert the text (e.g., line 6)
    line_number = 6

    # Append data to another file (en_US.lang) with capitalized text or replace it if exists
    lang_file_path = os.path.join(
        base_output_directory, f"RP/texts/en_US.lang")

    line_to_add_or_replace = f"tile.block:{formatted_file_name.lower()}.name={formatted_file_name_for_lang}"
    add_or_replace_line(lang_file_path, line_to_add_or_replace)

    print(f'Line added or replaced in "{lang_file_path}".')
