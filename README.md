**Bacteria Simulation in 2D Grid**

**Overview**

This project simulates a population of bacteria living in a 2D grid environment. 
Each bacterium behaves independently — it can move, reproduce, age, and die based on defined conditions.
The simulation demonstrates object-oriented design and models interactions within a dynamic system.

**Key Concepts**

Object-Oriented Programming (OOP)
Simulation of autonomous agents
State management in dynamic systems
Randomized behavior

**Project Structure**

1. Grid Class
   
Purpose:

Represents the 2D environment where bacteria exist.

Attributes:

size – dimensions of the grid
grid – 2D structure storing bacteria instances

Methods:

update() – updates the state of the grid in each simulation step
add_bacterium(position) – adds a bacterium at a specific location
remove_bacterium(position) – removes a bacterium from a location


2. Bacterium Class
   
Purpose:

Models a single bacterium with its lifecycle and behavior.

Attributes:

position – current location in the grid
health – determines survival and reproduction ability
age – bacterium lifespan indicator

Methods:

move() – random movement within the grid
reproduce() – creates a new bacterium if conditions are met
age() – increments age and affects health
die() – determines if the bacterium should be removed


**Simulation Flow**

- Initialize the grid
- Create and place initial bacteria

Run the simulation loop:

- Move bacteria
- Update age and health
- Check reproduction conditions
- Remove dead bacteria

Repeat steps for each iteration

Implementation Steps

**Design Bacterium Class**

Define attributes (position, health, age)
Implement lifecycle methods (move, age, reproduce, die)

**Implement Grid**

Create 2D structure
Add management methods for bacteria

**Simulate Behavior**

- Random movement logic
- Interactions between bacteria


**Lifecycle Management**

- Aging system
- Reproduction conditions
- Death conditions

**Run Simulation**

Initialize environment
Execute update loop


**Tips & Best Practices**

- Start simple (movement + grid) and iteratively add complexity
- Test components independently
- Use Python random module for stochastic behavior
- Keep state updates consistent per simulation step


**Learning Outcomes**

This project strengthens:

- OOP design skills
- Simulation modeling
- Problem decomposition
- Thinking about complex system interactions

