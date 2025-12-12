
STATE = {
    "hp": 100,
    "sanity": 100,
    "location": "bedroom_intro",  
    "alive": True,
    "inventory": [],
}

# Optional: Friendly scene/option display names for menu substitution of scene ids
DISPLAY_NAMES = {
    "door_a": "Door A (Left Door)",
    "door_b": "Door B (Right Door)",
    "bedroom_underbed": "Under the Bed",
    "bedroom_wardrobe": "Wardrobe",
    "kitchen_intro": "Kitchen",
    "kitchen_freezer": "Freezer",
    "kitchen_counter": "Counter",
    "kitchen_sink": "Sink",
    "bathroom_intro": "Bathroom",
    "bathroom_mirror": "Mirror",
    "bathroom_toilet": "Toilet",
    "hall_intro": "Hall",
    "hall_sheet": "Pull Back the Sheet",
}

SCENES = {
    # ========== Bedroom ==========
    "bedroom_intro": {
        "file": "bedroom/bedroom_intro.txt",
        "choices": {
            "1": "bedroom_underbed",    
            "2": "bedroom_wardrobe",    
            "3": "door_a",              
            "4": "door_b",              
        },
    },

    "bedroom_underbed": {
        "file": "bedroom/bedroom_underbed.txt",
        "choices": {
            "1": "bedroom_intro",       
            "2": "hall_intro",          
        },
    },

    "bedroom_wardrobe": {
        "file": "bedroom/bedroom_wardrobe.txt",
        "choices": {
            "1": "bedroom_intro",       
            "2": "hall_intro",          
        },
    },

    # —— Door Aliases (Door A / Door B) —— Abstract door choices as independent scene entries
    "door_a": {
        "file": "bathroom/bathroom_intro.txt",
        "choices": {
            "1": "bathroom_mirror",
            "2": "bathroom_toilet",
            "3": "bedroom_intro",
        },
    },

    "door_b": {
        "file": "hall/hall_intro.txt",
        "choices": {
            "1": "hall_sheet",
            "2": "kitchen_intro",
            "3": "bathroom_intro",
        },
    },

    # ========== Hall ==========
    "hall_intro": {
        "file": "hall/hall_intro.txt",
        "choices": {
            "1": "hall_sheet",          # Pull Back the Sheet
            "2": "kitchen_intro",       # Go to Kitchen
            "3": "bathroom_intro",      # Go to Bathroom
        },
    },

    "hall_sheet": {
        "file": "hall/hall_sheet.txt",
        "choices": {
            "1": "hall_intro",          # Return to Hall
        },
    },

    "hall_finalcheck": {
        "file": "hall/hall_finalcheck.txt",
        "choices": {
            "1": "ending_check",        # Perform Final Check
        },
    },

    # ========== Kitchen ==========
    "kitchen_intro": {
        "file": "kitchen/kitchen_intro.txt",
        "choices": {
            "1": "kitchen_freezer",     # Check Freezer
            "2": "kitchen_counter",     # Check Counter
            "3": "kitchen_sink",        # Check Sink
            "4": "hall_intro",          # Return to Hall
        },
    },

    "kitchen_freezer": {
        "file": "kitchen/kitchen_freezer.txt",
        "choices": {
            "1": "kitchen_intro",      
        },
    },

    "kitchen_counter": {
        "file": "kitchen/kitchen_counter.txt",
        "choices": {
            "1": "kitchen_intro",       
        },
    },

    "kitchen_sink": {
        "file": "kitchen/kitchen_sink.txt",
        "choices": {
            "1": "kitchen_intro",       
            "2": "hall_finalcheck",     # Go to Hall for Final Check
        },
    },

    # ========== Bathroom ==========
    "bathroom_intro": {
        "file": "bathroom/bathroom_intro.txt",
        "choices": {
            "1": "bathroom_mirror",     # Check Mirror
            "2": "bathroom_toilet",     # Check Toilet
            "3": "hall_intro",          # Return to Hall
        },
    },

    "bathroom_mirror": {
        "file": "bathroom/bathroom_mirror.txt",
        "choices": {
            "1": "bathroom_intro",      
        },
    },

    "bathroom_toilet": {
        "file": "bathroom/bathroom_toilet.txt",
        "choices": {
            "1": "bathroom_intro",      
        },
    },

    # ========== Ending Check Logic ==========
    "ending_check": {
        "file": "endings/ending_check.txt",
        "choices": {
            "1": "ending_success",      # HP > 0 and SAN >= 10
            "2": "ending_death",        # HP <= 0
            "3": "ending_madness",      # SAN < 10
        },
    },

    # ========== Endings ==========
    "ending_death": {
        "file": "endings/ending_death.txt",
        "choices": {},
    },

    "ending_madness": {
        "file": "endings/ending_madness.txt",
        "choices": {},
    },

    "ending_success": {
        "file": "endings/ending_success.txt",
        "choices": {},
    },
}

RANDOM_EVENTS = {
    # when go into the kitchen
    "kitchen_intro": {
        "pool": [
            None,                           # 0. nothing happen
            "events/lamp_explode.txt",      # 1. lamp_explode (lost HP)
            "events/rotten_smell.txt"       # 2. rotten_smell (lost SAN)
        ],
        "weights": [40, 40, 20]             # persent: 40%, 40%, 20%
    },

    # when go into bathroom
    "bathroom_intro": {
        "pool": [
            None,
            "events/mirror_crack.txt",      # mirror_crack
            "events/slip_floor.txt"         # slip_floor
        ],
        "weights": [40, 30, 30]
    },

    # when go into hall
    "hall_intro": {
        "pool": [
            None,
            "events/whisper.txt"            # whisper
        ],
        "weights": [60, 40]
    }
}