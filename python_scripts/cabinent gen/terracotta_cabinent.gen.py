# Function to create a directory if it doesn't exist
import json
import os


def create_directory_if_not_exists(directory):
    os.makedirs(directory, exist_ok=True)

# Function to save JSON data to a file with overwrite


def save_json_to_file(data, file_path, overwrite=True):
    mode = "w"  # Use "w" for write mode
    if not overwrite and os.path.exists(file_path):
        mode = "x"  # Use "x" for exclusive creation, will raise an error if the file already exists
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

# Function to create and save a JSON loot table


def create_loot_table(color, loot_table_output_directory):
    loot_table_template = {
        "pools": [
            {
                "rolls": 1,
                "entries": [
                    {
                        "type": "item",
                        "name": f"block:kitchen_cabinent_terracotta_{color}",
                        "weight": 1,
                        "functions": [
                            {"function": "set_count", "count": {"min": 1, "max": 1}}
                        ],
                    }
                ],
            }
        ]
    }

    loot_table_json_file_path = os.path.join(
        loot_table_output_directory, f"kitchen_cabinent_terracotta_{color}.loot.json"
    )
    save_json_to_file(loot_table_template, loot_table_json_file_path)

    print(
        f'JSON loot table file "kitchen_cabinent_terracotta_{color}.loot.json" has been created in the directory "{loot_table_output_directory}".'
    )


# List of colors to generate files for
colors = [
    "black", "green", "blue", "brown", "gray", "cyan", "light_blue",
    "light_gray", "lime", "magenta", "orange", "pink", "purple",
    "red", "white", "yellow"
]

# Specify the directory where the loot table JSON files will be generated
loot_table_output_directory = r"C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\BP\loot_tables\kitchen_furniture_loot\kitchen_cabinent_loot"

# Ensure the loot table output directory exists
create_directory_if_not_exists(loot_table_output_directory)

# Define the color-to-data mapping
color_data_map = {
    "white": 0,
    "light_gray": 8,
    "gray": 7,
    "black": 15,
    "brown": 12,
    "red": 14,
    "orange": 1,
    "yellow": 4,
    "lime": 5,
    "green": 13,
    "cyan": 9,
    "light_blue": 3,
    "blue": 11,
    "purple": 10,
    "magenta": 2,
    "pink": 6
}

for color in colors:
    # Define the JSON item template
    formatted_file_name = f"kitchen_cabinent_terracotta_{color}"
    block_template = {
        "format_version": "1.20.0",
        "minecraft:block": {
            "description": {
                "identifier": f"block:{formatted_file_name}",
                "menu_category": {
                    "category": "construction",
                    "group": "itemGroup.name.cabinent"
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
                        2
                    ],
                    "property:timer": [
                        0,
                        1
                    ],
                    "property:storage0": [
                        0,
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7,
                        8,
                        9
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
                    "condition": "query.block_property('property:storage0') == 0",
                    "components": {
                        "minecraft:material_instances": {
                            "storage0": {
                                "texture": "drawer_storage_empty",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            },
                            "*": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            }
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:storage0') == 1",
                    "components": {
                        "minecraft:material_instances": {
                            "storage0": {
                                "texture": "drawer_storage0",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            },
                            "*": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            }
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:storage0') == 2",
                    "components": {
                        "minecraft:material_instances": {
                            "storage0": {
                                "texture": "drawer_storage1",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            },
                            "*": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            }
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:storage0') == 3",
                    "components": {
                        "minecraft:material_instances": {
                            "storage0": {
                                "texture": "drawer_storage2",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            },
                            "*": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            }
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:storage0') == 4",
                    "components": {
                        "minecraft:material_instances": {
                            "storage0": {
                                "texture": "drawer_storage3",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            },
                            "*": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            }
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:storage0') == 5",
                    "components": {
                        "minecraft:material_instances": {
                            "storage0": {
                                "texture": "drawer_storage4",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            },
                            "*": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            }
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:storage0') == 6",
                    "components": {
                        "minecraft:material_instances": {
                            "storage0": {
                                "texture": "drawer_storage5",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            },
                            "*": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            }
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:storage0') == 7",
                    "components": {
                        "minecraft:material_instances": {
                            "storage0": {
                                "texture": "drawer_storage6",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            },
                            "*": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            }
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:storage0') == 8",
                    "components": {
                        "minecraft:material_instances": {
                            "storage0": {
                                "texture": "drawer_storage7",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            },
                            "*": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            }
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:storage0') == 9",
                    "components": {
                        "minecraft:material_instances": {
                            "storage0": {
                                "texture": "drawer_storage8",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            },
                            "*": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_terracotta_{color}",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            }
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:animated') == 0",
                    "components": {
                        "minecraft:geometry": "geometry.cabinent_closed",
                        "minecraft:queued_ticking": {
                            "looping": False,
                            "interval_range": [
                                0.25,
                                0.25
                            ],
                            "on_tick": {
                                "event": "event:place_inventory"
                            }
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:timer') == 1",
                    "components": {
                        "minecraft:queued_ticking": {
                            "looping": True,
                            "interval_range": [
                                0.01,
                                0.01
                            ],
                            "on_tick": {
                                "event": "event:are_doors_open"
                            }
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:animated') == 0",
                    "components": {
                        "minecraft:selection_box": {
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
                        "minecraft:geometry": "geometry.cabinent_closed"
                    }
                },
                {
                    "condition": "query.block_property('property:animated') == 1",
                    "components": {
                        "minecraft:selection_box": {
                            "origin": [
                                -8,
                                1,
                                -8
                            ],
                            "size": [
                                16,
                                15,
                                12
                            ]
                        },
                        "minecraft:geometry": "geometry.cabinent_closed"
                    }
                },
                {
                    "condition": "query.block_property('property:animated') == 2",
                    "components": {
                        "minecraft:selection_box": {
                            "origin": [
                                -8,
                                1,
                                -8
                            ],
                            "size": [
                                16,
                                15,
                                12
                            ]
                        },
                        "minecraft:geometry": "geometry.cabinent_opened"
                    }
                }
            ],
            "components": {
                "minecraft:selection_box": {
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
                "minecraft:loot": f"loot_tables/kitchen_furniture_loot/kitchen_cabinent_loot/kitchen_cabinent_terracotta_{color}.loot.json",
                "minecraft:destructible_by_explosion": {
                    "explosion_resistance": 15
                },
                "minecraft:material_instances": {
                    "*": {
                        "texture": f"kitchen_terracotta_{color}",
                        "ambient_occlusion": True,
                        "render_method": "alpha_test"
                    },
                    "drawer": {
                        "texture": f"kitchen_terracotta_{color}",
                        "ambient_occlusion": True,
                        "render_method": "alpha_test"
                    },
                    "storage0": {
                        "texture": "drawer_storage_empty",
                        "ambient_occlusion": True,
                        "render_method": "alpha_test"
                    }
                },
                "minecraft:map_color": "#7d7d7d"
            },
            "events": {
                "event:place_inventory": {
                    "run_command": {
                        "command": [
                            "/summon entity:kitchen_furniture_inventory drawer ~ ~-0.25 ~"
                        ]
                    },
                    "set_block_property": {
                        "property:animated": 1,
                        "property:timer": 1,
                        "property:storage0": 0
                    }
                },
                "event:are_doors_open": {
                    "sequence": [
                        {
                            "condition": "q.block_property('property:animated') <= 1",
                            "run_command": {
                                "command": [
                                    "/event entity @e[type=entity:kitchen_furniture_inventory,r=1] event:inventory_has_no_hit_box"
                                ]
                            }
                        },
                        {
                            "condition": "q.block_property('property:animated') > 1",
                            "run_command": {
                                "command": [
                                    "/event entity @e[type=entity:kitchen_furniture_inventory,r=1] event:inventory_has_hit_box"
                                ]
                            }
                        }
                    ]
                },
                "event:block_placed": {
                    "set_block_property": {
                        "property:direction_player_is_facing": "q.cardinal_facing_2d-2"
                    }
                },
                "event:cycle_properties": {
                    "sequence": [
                        {
                            "condition": "query.is_sneaking == True",
                            "set_block_property": {
                                "property:storage0": "q.block_property('property:storage0') == 9 ? 0 :q.block_property('property:storage0')+1"
                            },
                            "run_command": {
                                "command": [
                                    "/playsound interact.drawer_fill @p"
                                ]
                            }
                        },
                        {
                            "condition": "!q.is_sneaking && q.block_property('property:animated') == 2",
                            "run_command": {
                                "command": [
                                    "/playsound drawer.close @p"
                                ]
                            }
                        },
                        {
                            "condition": "!q.is_sneaking && q.block_property('property:animated') >= 1",
                            "set_block_property": {
                                "property:animated": "q.block_property('property:animated') == 2 ? 1 :q.block_property('property:animated')+1"
                            },
                            "run_command": {
                                "command": [
                                    "/playsound drawer.open @p"
                                ]
                            }
                        }
                    ]
                }
            }
        }

        # Add any desired attributes for the block
        # Set the "data" value based on the color

    }

    # Specify the output directory for items
    output_directory = os.path.join(
        r"C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\BP\blocks\kitchen_furniture_cabinent_blocks"
    )

    create_directory_if_not_exists(output_directory)

    # Save the JSON item file in the specified directory, overwriting if it already exists
    item_json_file_path = os.path.join(
        output_directory, f"kitchen_cabinent_terracotta_{color}.block.json"
    )
    save_json_to_file(block_template, item_json_file_path, overwrite=True)

    print(
        f'JSON file "kitchen_cabinent_terracotta_{color}.block.json" has been created in the directory "{output_directory}".'
    )

    # Define the JSON recipe template
    recipe_template = {
        "format_version": "1.20.0",
        "minecraft:recipe_shaped": {
            "description": {
                "identifier": f"block:kitchen_cabinent_terracotta_{color}"
            },
            "tags": ["crafting_table"],
            "priority": 1,
            "pattern": [
                "###",
                "#C#",
                "VVV"
            ],
            "key": {
                "#": {
                    "item": "minecraft:stained_hardened_clay",
                    "data": color_data_map[color]
                },
                "C": {
                    "item": "minecraft:chest"
                },
                "V": {
                    "item": "minecraft:concrete"
                }
            },
            "result": f"block:kitchen_cabinent_terracotta_{color}",
            "count": 3
        }
    }

    # Specify the directory where the recipe JSON file will be generated
    recipe_output_directory = os.path.join(
        r"C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\BP\recipes\kitchen_furniture_recipes\kitchen_cabinent_recipes"
    )

    create_directory_if_not_exists(recipe_output_directory)

    # Save the JSON recipe file in the specified directory, overwriting if it already exists
    recipe_json_file_path = os.path.join(
        recipe_output_directory, f"kitchen_cabinent_terracotta_{color}.recipe.json"
    )
    save_json_to_file(recipe_template, recipe_json_file_path, overwrite=True)

    print(
        f'JSON recipe file "kitchen_cabinent_terracotta_{color}.recipe.json" has been created in the directory "{recipe_output_directory}".'
    )

    # Modify the color to have spaces between words and capitalize the second word
    formatted_file_name_for_lang = " ".join(
        word.capitalize() for word in formatted_file_name.replace("_", " ").split()
    )

    # Specify the line number to insert the text (e.g., line 6)
    line_number = 6

    # Append data to another file (en_US.lang) with capitalized text or replace it if exists
    lang_file_path = os.path.join(
        r"C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\RP\texts\en_US.lang"
    )

    line_to_add_or_replace = f"tile.block:{formatted_file_name.lower()}.name={formatted_file_name_for_lang}"
    add_or_replace_line(lang_file_path, line_to_add_or_replace)

    print(f'Line added or replaced in "{lang_file_path}".')

    # Create and save the loot table for this color
    create_loot_table(color, loot_table_output_directory)
