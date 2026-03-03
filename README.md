Added project documentation and instructions
# Baseball Team Manager (Sections 1–3)

## Course
CPRO 2201 – Python Programming II

## Student
Nikita Lnu

---

## Project Description

This is a console-based Baseball Team Manager program developed using Python.

The program allows a manager to:

- Display the lineup
- Add a player
- Remove a player
- Move a player in the lineup
- Edit player position
- Edit player statistics
- Store data in a CSV file for persistence

The program follows Object-Oriented Programming principles and proper layer separation.

---

## Architecture

The project is divided into separate modules:

- **main.py** → Controls program flow
- **objects.py** → Contains Player and Lineup classes (Business Logic)
- **db.py** → Handles file reading and writing (Data Layer)
- **ui.py** → Handles user input and output (Presentation Layer)
- **players.csv** → Stores player data

---

## OOP Design

### Player Class
Stores:
- first_name
- last_name
- position
- at_bats
- hits

Provides:
- full_name property
- batting_average property
- update methods

### Lineup Class
- Stores list of Player objects
- Supports add, remove, move, and edit
- Implements encapsulation
- Implements __len__ and __iter__

---

## Features Implemented

1 Input validation  
2 Error handling  
3 CSV persistence  
4 Batting average calculation  
5 Modular architecture  
6 Object-oriented design  

---

## How to Run

Make sure Python is installed.

Run:

