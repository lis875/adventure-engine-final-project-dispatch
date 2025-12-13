import turtle
import time
import random

from scenes import STATE, SCENES, DISPLAY_NAMES, RANDOM_EVENTS
from main import show_scene, apply_stat_changes
import escape_turtle
import ending_turtle
# ==========================================
# 1. Coordinate Mapping
# ==========================================
ROOM_COORDS = {
    "bedroom": (-135, -25),  
    "bathroom": (-270, -20), 
    "hall": (20, -60),        
    "kitchen": (135, 80) 
}

def get_coordinates(scene_id):
    if scene_id == "door_a":
        return ROOM_COORDS["bathroom"]
    elif scene_id == "door_b":
        return ROOM_COORDS["hall"]
    if "bedroom" in scene_id:
        return ROOM_COORDS["bedroom"]
    elif "bathroom" in scene_id:
        return ROOM_COORDS["bathroom"]
    elif "hall" in scene_id:
        return ROOM_COORDS["hall"]
    elif "kitchen" in scene_id:
        return ROOM_COORDS["kitchen"]
    else:
        return (0, 0)

# ==========================================
# 2. Player Setup
# ==========================================
def create_player_marker():
    player = turtle.Turtle()
    player.shape("circle") 
    player.color("red")    
    player.shapesize(0.8)  
    player.penup()        
    player.speed(3)         
    return player

# ==========================================
# 3. Modified Game Loop
# ==========================================
# random cases function
def trigger_random_event(scene_id):
    if scene_id not in RANDOM_EVENTS:
        return

    event_data = RANDOM_EVENTS[scene_id]
    pool = event_data["pool"]
    weights = event_data["weights"]

    chosen_event = random.choices(pool, weights=weights, k=1)[0]

    if chosen_event is not None:
        print("\n" + "!" * 40)
        print(">>> SUDDEN EVENT! <<<")
        
        try:
        
            with open(f"rooms/{chosen_event}", encoding="utf-8") as f:
                text = f.read()
                print(text)
                apply_stat_changes(text)
        except FileNotFoundError:
            print(f"[System Error] Event file missing: {chosen_event}")
        
        print("!" * 40 + "\n")
        time.sleep(1.5) 

def run_game_with_map():
    # --- A. ori_map ---
    escape_turtle.draw_gradient_title("Castle Escape", font_size=70)
    escape_turtle.draw_house_plan()
    escape_turtle.draw_bed(-120, -40)
    escape_turtle.draw_toilet(-315, -40)
    escape_turtle.draw_cutlery(150, 70)
    escape_turtle.draw_dining_set(20, -25)
    
    # --- B. ori_player ---
    player = create_player_marker()
    
    # current_location
    current_location = STATE["location"]
    start_x, start_y = get_coordinates(current_location)
    player.goto(start_x, start_y)

    print("=== Escapping start!! ===")
    print("Tip：Please check the turtle map and enter your chioces in terminal.")

    # --- C. loop ---
    while STATE["alive"]:
        
        # 1. update_location
        target_x, target_y = get_coordinates(STATE["location"])
        player.goto(target_x, target_y)
        trigger_random_event(STATE["location"])

        if not STATE["alive"]:
            break

        # 2. text
        current_scene_id = STATE["location"]
        show_scene(current_scene_id)
        
        #### ending check
        if current_scene_id == "ending_check":
            print("\n>>> Checking the ending based on your statement...\n")
            time.sleep(2) # Create a sense of tension
            if STATE["sanity"] >= 10 and STATE["hp"] > 0:
                STATE["location"] = "ending_success"
            elif STATE["sanity"] < 10:
                STATE["location"] = "ending_madness"
            else:
                STATE["location"] = "ending_death"
            continue

        # 3. scene_data
        scene_data = SCENES.get(current_scene_id)
        if not scene_data:
            print("Game over (scene not define)")
            break
            
        choices = scene_data.get("choices", {})

        if not choices:
            break

        # 4. print
        print("\nWhich choice you wanna choose:")

        for key in sorted(choices.keys(), key=lambda x: int(x) if x.isdigit() else 0):
            next_scene_name = choices[key]
            display_entry = DISPLAY_NAMES.get(next_scene_name)
            
            label = ""
            if isinstance(display_entry, dict):
                label = display_entry.get('label', next_scene_name)
            elif isinstance(display_entry, str):
                label = display_entry
            else:
                label = next_scene_name
            print(f"{key}. {label}")

        # 5. input
        user_input = input("\n> Please enter the number you choose: ").strip()

        # 6. update status
        if user_input in choices:
            next_scene = choices[user_input]
            STATE["location"] = next_scene  
        else:
            print("meaningless,try again")

    print("\n=== Ending ===")
    print("Please check the Popup Window for your Ending Card.")
    escape_turtle.screen.clearscreen()
    escape_turtle.screen.bgcolor("black") 

    if STATE["location"] == "ending_death" or STATE["hp"] <= 0:
        ending_turtle.ending1()
        
    elif STATE["location"] == "ending_success":
        ending_turtle.ending2()
        
    elif STATE["location"] == "ending_madness" or STATE["sanity"] <= 0:
        ending_turtle.ending3()
    

if __name__ == "__main__":
    run_game_with_map()