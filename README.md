# Castle Escape
"The house breathes. The house laughs. Do you have the strength to escape?"
## 1.0 Description
Castle Escape is an immersive text-based interactive fiction game developed in Python. Players wake up in a gloomy, mysterious castle and must find the key to escape by exploring rooms, gathering clues, and solving puzzles. The game combines classic text adventure gameplay with Turtle Graphics for real-time map visualization, delivering a unique dual-window gaming experience.

## 2.0 Game Features

Dual-Window Interaction System：
Terminal: Handles core storytelling, player command input, and status feedback.

Turtle Map: Displays the castle floor plan and the player's real-time position (red dot) to enhance spatial awareness.

## 3.0 Survival System

HP (Health Points): Physical damage (e.g., cold, monster attacks) reduces HP. If HP reaches 0, the player dies.

SAN (Sanity): Horrific events (e.g., hallucinations, whispers) reduce Sanity. If SAN drops below 10, the player succumbs to madness.

## 4.0 Non-Linear Exploration

Freely explore four main areas: Bedroom, Hall, Kitchen, and Bathroom.
Item Collection & Puzzle Solving: Find critical items (such as the Rusty Tiny Key and Heavy Silver Key) to unlock the final exit.

## 5.0 Random Event System

Entering a room may trigger random horror events (e.g., exploding light bulbs, cracking mirrors, whispering voices), adding unpredictability and tension to the gameplay.

## 6.0 Multiple Endings

True Ending: Successful Escape (Alive & High Sanity).

Bad Ending 1: Death (HP Depleted).

Bad Ending 2: Madness (Sanity Lost).

## 7.0 Project Structure

The project follows a modular design. Key files are described below:

1/CastleEscape-play.py:
The main entry point of the game. It bridges the logic layer and the view layer, initializes the Turtle map, and runs the main game loop.

2/scenes.py:
The data core. It stores node information for all rooms, choice logic, global state (STATE), and the random event pool (RANDOM_EVENTS).

3/main.py:
Contains text processing logic, such as show_scene (reading scripts) and apply_stat_changes (parsing HP/SAN changes via regular expressions).

4/escape_turtle.py:
Handles the graphics logic. Uses Python's Turtle library to draw the castle floor plan, furniture details, and the dynamic title.

5/rooms/:
A folder containing all story text files (.txt), ensuring separation of content and code.

## 8.0 How to Run

Ensure Python 3.x is installed on your computer.
Make sure all project files (including the rooms folder) are in the same directory.
Run the following command in your terminal or command prompt to start the game:

## 9.0 Gameplay Guide:

Once the game starts, a Turtle Map Window will pop up. Please place it side-by-side with your terminal to track your location.
Read the story in the Terminal Window and enter numbers (e.g., 1, 2) to choose your actions.

## 10.0 Team Contributions

This project was developed by [Dispatch], with individual roles and contributions as follows:

|Name	       |Role	                     |Specific Contributions
| :--- | :--- | :--- |
|Annacy YAN	   |QA / Project Manager         |Graphics System & Main Program Integration
|Dongjiyi Er   |Systems Engineer             |Scene Logic & Random cases
|Yves Zhou     |Systems Engineer             |Core Functions & HP/SAN
|Leah          |Content Designer / Writer    |Content & story logic

## 11.0 Dependencies

Standard Libraries: turtle, time, random, os, re

No external pip packages are required.

Created for LIS875: Technical Foundations of Information Science.

Author：Annacy Yan