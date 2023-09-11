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
base_output_directory = r"C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\BP\blocks\kitchen\furniture\counter"

for color in colors:
    # Define the JSON item template
    formatted_file_name = f"counter_{color}"
    block_template = {
        "format_version": "1.20.0",
        "minecraft:block": {
            "description": {
                "identifier": f"block:kitchen_counter_{color}",
                "menu_category": {
                    "category": "construction"
                },
                "properties": {
                    "property:direction_player_is_facing": [
                        0,
                        1,
                        2,
                        3
                    ],
                    "property:animated": [
                        0,
                        1,
                        2,
                        3,
                        4
                    ]
                }
            },
            "permutations": [
                {
                    "condition": "query.block_property('property:direction_player_is_facing')== 0",
                    "components": {
                        "minecraft:transformation": {
                            "rotation": [
                                0,
                                0,
                                0
                            ]
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:direction_player_is_facing')== 1",
                    "components": {
                        "minecraft:transformation": {
                            "rotation": [
                                0,
                                180,
                                0
                            ]
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:direction_player_is_facing')== 2",
                    "components": {
                        "minecraft:transformation": {
                            "rotation": [
                                0,
                                90,
                                0
                            ]
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:direction_player_is_facing')== 3",
                    "components": {
                        "minecraft:transformation": {
                            "rotation": [
                                0,
                                270,
                                0
                            ]
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:animated') == 0",
                    "components": {
                        "minecraft:geometry": "geometry.counter"
                    }
                },
                {
                    "condition": "query.block_property('property:animated') == 1",
                    "components": {
                        "minecraft:geometry": "geometry.counter_corner0"
                    }
                },
                {
                    "condition": "query.block_property('property:animated') == 2",
                    "components": {
                        "minecraft:geometry": "geometry.counter_corner1"
                    }
                },
                {
                    "condition": "query.block_property('property:animated') == 3",
                    "components": {
                        "minecraft:geometry": "geometry.counter_corner2"
                    }
                },
                {
                    "condition": "query.block_property('property:animated') == 4",
                    "components": {
                        "minecraft:geometry": "geometry.counter_corner3"
                    }
                }
            ],
            "components": {
                "minecraft:selection_box": True,
                "minecraft:collision_box": {
                    "origin": [
                        -8,
                        0,
                        -8
                    ],
                    "size": [
                        16,
                        16,
                        16
                    ]
                },
                "minecraft:destructible_by_mining": {
                    "seconds_to_destroy": 0.3
                },
                "minecraft:on_player_placing": {
                    "event": "event:block_placed"
                },
                "minecraft:on_interact": {
                    "event": "event:cycle_properties",
                    "target": "self"
                },
                "minecraft:geometry": "geometry.counter",
                "minecraft:loot": f"loot_tables/kitchen/furniture/counter/counter_{color}.loot.json",
                "minecraft:destructible_by_explosion": {
                    "explosion_resistance": 15
                },
                "minecraft:material_instances": {
                    "*": {
                        "texture": f"kitchen_{color}",
                        "ambient_occlusion": True,
                        "render_method": "alpha_test"
                    }
                },
                "minecraft:map_color": "#7d7d7d"
            },
            "events": {
                "event:block_placed": {
                    "set_block_property": {
                        "property:direction_player_is_facing": "q.cardinal_facing_2d-2"
                    }
                },
                "event:cycle_properties": {
                    "sequence": [
                        {
                            "condition": "!q.is_sneaking&&q.block_property('property:animated')==4"
                        },
                        {
                            "condition": "!q.is_item_name_any('slot.weapon.mainhand','minecraft:wooden_axe')&&!q.is_item_name_any('slot.weapon.mainhand','minecraft:stone_axe')&&!q.is_item_name_any('slot.weapon.mainhand','minecraft:iron_axe')&&!q.is_item_name_any('slot.weapon.mainhand','minecraft:golden_axe')&&!q.is_item_name_any('slot.weapon.mainhand','minecraft:diamond_axe')&&!q.is_item_name_any('slot.weapon.mainhand','minecraft:netherite_axe')&&!q.is_sneaking",
                            "set_block_property": {
                                "property:animated": "q.block_property('property:animated') == 4 ? 0 :q.block_property('property:animated')+1"
                            }
                        }
                    ]
                }
            }
        }
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
