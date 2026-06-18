# University Timetable Scheduler

This project was developed as part of the Advanced Algorithms module.

The aim of the project is to create a simple university timetable scheduler using Python. The system assigns courses to available time slots and classrooms while considering room capacity, student group conflicts, and professor availability.

## Problem

Creating a university timetable manually can be difficult because many constraints must be considered at the same time.

The scheduler should:

- Assign courses to suitable classrooms.
- Avoid room conflicts.
- Consider professor availability.
- Reduce wasted classroom capacity.
- Generate a valid timetable for all courses whenever possible.

## Algorithms Used

1. Greedy Algorithm
2. Conflict Graph and Graph Coloring
3. Room Optimization
4. Backtracking

## How to Run

Run each file from the src folder:

python greedy_solver.py
python graph_engine.py
python optimizer.py
python backtracker.py

## Dataset

The project uses JSON files:

- courses.json
- rooms.json
- professors.json
- student_groups.json

## Results

The project successfully generated a timetable for 10 courses.

The following algorithms were implemented:

- Greedy Scheduling
- Graph Coloring
- Room Optimization
- Backtracking

The final timetable assigns courses to rooms and time slots while considering professor availability and room capacity.