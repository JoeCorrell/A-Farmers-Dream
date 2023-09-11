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
base_output_directory = r"C:\Users\Joe\AppData\Local\com.bridge.dev\bridge\projects\HarvestCraft\BP\blocks\kitchen\furniture\half_cupboard"

for color in colors:
    # Define the JSON item template
    formatted_file_name = f"half_cupboard_{color}"
    block_template = {
        "format_version": "1.20.0",
        "minecraft:block": {
            "description": {
                "identifier": f"block:kitchen_half_cupboard_{color}",
                "menu_category": {
                    "category": "construction",
                    "group": "itemGroup.name.half_cupboard"
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
                                "texture": f"kitchen_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_{color}",
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
                                "texture": f"kitchen_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_{color}",
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
                                "texture": f"kitchen_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_{color}",
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
                                "texture": f"kitchen_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_{color}",
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
                                "texture": f"kitchen_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_{color}",
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
                                "texture": f"kitchen_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_{color}",
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
                                "texture": f"kitchen_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_{color}",
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
                                "texture": f"kitchen_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_{color}",
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
                                "texture": f"kitchen_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_{color}",
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
                                "texture": f"kitchen_{color}",
                                "ambient_occlusion": True,
                                "render_method": "alpha_test"
                            },
                            "drawer": {
                                "texture": f"kitchen_{color}",
                                "ambient_occlusion": False,
                                "render_method": "alpha_test"
                            }
                        }
                    }
                },
                {
                    "condition": "query.block_property('property:animated') == 0",
                    "components": {
                        "minecraft:geometry": "geometry.half_cupboard_closed",
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
                                13
                            ]
                        },
                        "minecraft:geometry": "geometry.half_cupboard_closed"
                    }
                },
                {
                    "condition": "query.block_property('property:animated') == 1",
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
                                13
                            ]
                        },
                        "minecraft:geometry": "geometry.half_cupboard_closed"
                    }
                },
                {
                    "condition": "query.block_property('property:animated') == 2",
                    "components": {
                        "minecraft:selection_box": {
                            "origin": [
                                -8,
                                3,
                                -7.5
                            ],
                            "size": [
                                16,
                                13,
                                13
                            ]
                        },
                        "minecraft:geometry": "geometry.half_cupboard_right_opened"
                    }
                },
                {
                    "condition": "query.block_property('property:animated') == 3",
                    "components": {
                        "minecraft:selection_box": {
                            "origin": [
                                -8,
                                3,
                                -7.5
                            ],
                            "size": [
                                16,
                                13,
                                13
                            ]
                        },
                        "minecraft:geometry": "geometry.half_cupboard_left_opened"
                    }
                },
                {
                    "condition": "query.block_property('property:animated') == 4",
                    "components": {
                        "minecraft:selection_box": {
                            "origin": [
                                -8,
                                3,
                                -7.5
                            ],
                            "size": [
                                16,
                                13,
                                13
                            ]
                        },
                        "minecraft:geometry": "geometry.half_cupboard_both_opened"
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
                        13
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
                        13
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
                "minecraft:loot": f"loot_tables/kitchen/furniture/half_cupboard/half_cupboard_{color}.loot.json",
                "minecraft:destructible_by_explosion": {
                    "explosion_resistance": 15
                },
                "minecraft:material_instances": {
                    "*": {
                        "texture": f"kitchen_{color}",
                        "ambient_occlusion": True,
                        "render_method": "alpha_test"
                    },
                    "drawer": {
                        "texture": f"kitchen_{color}",
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
                            f"/summon entity:kitchen_furniture_inventory cupboard_{color} ~ ~-0.25 ~"
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
                            "condition": "!q.is_sneaking && q.block_property('property:animated') == 4",
                            "run_command": {
                                "command": [
                                    "/playsound drawer.close @p"
                                ]
                            }
                        },
                        {
                            "condition": "!q.is_sneaking && q.block_property('property:animated') >= 1",
                            "set_block_property": {
                                "property:animated": "q.block_property('property:animated') == 4 ? 1 :q.block_property('property:animated')+1"
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
