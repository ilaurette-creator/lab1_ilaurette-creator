# Kigali FSD Tesla Road Simulation - Lab 1

## Overview
This repository contains the completed solution for Individual Coding Lab 1 on the Kigali FSD Tesla Road Simulation starting from ALU Rwanda to Rwanda Convention Center.

## Features
- Dynamic speed limit adjustments (20–100 km/h).
- Automatic zebra crossing detection and 15-second stops.
- Bus avoidance and left lane switching logic.
- Input validation and index boundary protection.

## How to Run
Run tests and start simulation:

1. Open a terminal in the lab1_ilaurette-creator folder.
2. Run python road_simulation.py.
3. Enter your driver name, then use the road editor menu.
4. You will be given various option but choose 5. Start driving, then open the link (E.g: http://127.0.0.1:8008).
5. Go back to the terminal and press Enter. The car starts to drive.

## The structure of the program(road_simulation.py)
lab1_ilaurette-creator/
|___road_simulation.py
|___transit_program.py
|___engine.py
|___index.html


## Repository Files
- road_simulation.py: Student implementation file containing TODO 1 through TODO 10.
- transit_program.py: Read-only simulation execution engine and interactive CLI.
- engine.py: Read-only HTTP server and state broadcaster.
- index.html: Read-only visual dashboard frontend.
- transit_session.log: Log file generated during simulation sessions.
- README.md: Documentation, guidance for how the project runs.

