# python-supermarket

This project is a full re-implementation of a supermarket simulator originally developed in C# for a Data Structures course. The Python version includes both a terminal-based simulation and a Tkinter-based graphical simulation with animated customer queues.

## Project Overview

The simulator models a simplified checkout system in a supermarket:

* Customers arrive with a random number of items.
* Each customer is assigned to the register with the shortest queue.
* Registers process customers in a first-in, first-out (FIFO) order.
* Final statistics are displayed after all customers are processed.

## Features

* Terminal simulation with live customer processing logs.
* Tkinter GUI simulation with animated customer queues.
* Modular object-oriented code structure.
* Complete rewrite from C# to Python, expanding on the original project specifications.

## How to Run

### Terminal Simulation

```bash
python terminal_sim.py
```

### GUI Simulation

```bash
python gui_sim.py
```

### Windows Executable (v1.0.0 Release)

A downloadable **v1.0.0 release executable** of the GUI simulator is available under the [Releases] section. This allows running the simulator on Windows without requiring Python installation.

## File Structure

```
python-supermarket/
├── supermarket_logic/
│   ├── customer.py
│   ├── item.py
│   ├── register.py
│   ├── supermarket.py
│   └── __init__.py
├── terminal_sim.py
├── gui_sim.py
├── README.md
└── .gitignore
```

## Technologies Used

* Python 3.12
* Tkinter for GUI
* OOP principles and data structure concepts (lists used as queues)
* PyInstaller for Windows executable packaging

## Background

This project is based on the CSCI 2210 Project 4: Supermarket Simulation. The Python version was developed to modernize the project and provide both terminal and graphical outputs while adhering to clean code principles.
