from scenes import STATE, SCENES, DISPLAY_NAMES
import os
import re

ROOM_DIR = "rooms"

def apply_stat_changes(text):
    """Extract and apply HP / SAN changes from text."""
    hp_match = re.search(r'\[HP\s*([+-]?\d+)\]', text)
    san_match = re.search(r'\[SAN\s*([+-]?\d+)\]', text)
    
    if hp_match:
        hp_change = int(hp_match.group(1))
        STATE['hp'] += hp_change
        print(f"\n>>> HP {hp_change:+d} | Current HP: {STATE['hp']}")
    
    if san_match:
        san_change = int(san_match.group(1))
        STATE['sanity'] += san_change
        print(f">>> SAN {san_change:+d} | Current SAN: {STATE['sanity']}")
    
    # game_endingtime
    if STATE['hp'] <= 0:
        STATE['alive'] = False
        print("\n⚠️  Your body collapses. HP reached 0!")
    elif STATE['sanity'] <= 0:
        STATE['alive'] = False
        print("\n⚠️  Your mind shatters. SAN reached 0!")

def show_scene(scene_id):

    scene = SCENES.get(scene_id)
    if not scene:
        print(f"error: scene '{scene_id}' not defined in SCENES.")
        STATE["alive"] = False
        return
    
    filename = scene["file"]

    try:
        with open(f"{ROOM_DIR}/{filename}", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"file not found: {ROOM_DIR}/{filename}")
        STATE["alive"] = False
        return
    
    print("\n" + text)
    apply_stat_changes(text)
    print(f"\n[HP: {STATE['hp']} | SAN: {STATE['sanity']}]")

def game_loop():
    current = STATE["location"]

    while STATE["alive"]:
        show_scene(current)
        
        scene = SCENES.get(current)
        if not scene:
            print(f"Invalid scene. Game over.")
            break
        
        choices = scene.get("choices", {})

        # If there are no choices, it's usually an ending, so exit directly
        if not choices:
            break

        # Print available choices (using friendly names if available)
        print("\nYou can choose:")
        for key in sorted(choices.keys(), key=lambda x: int(x) if x.isdigit() else 0):
            next_scene_name = choices[key]
            display_entry = DISPLAY_NAMES.get(next_scene_name)
            if isinstance(display_entry, dict):
                label = display_entry.get('label')
                coords = display_entry.get('coords')
                if coords:
                    label = f"{label} @{coords}"
            elif isinstance(display_entry, str):
                label = display_entry
            else:
                # Fallback to a more readable scene id
                label = next_scene_name.replace('_', ' ').title()
            print(f"{key}. {label}")

        answer = input("\n> Please enter the option number: ").strip()

        if answer not in choices:
            print("Invalid option, please try again.")
            continue

        # Move to the next scene
        next_scene = choices[answer]
        STATE["location"] = next_scene
        current = next_scene

    print("\nGame over.")

if __name__ == "__main__":
    game_loop()


