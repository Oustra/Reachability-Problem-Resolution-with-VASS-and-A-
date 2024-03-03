# Project Title: Reachability Problem Resolution with VASS and A*

# Description:
In this project, we tackle the reachability problem, which is crucial in the field of motion planning and solving complex problems. This problem finds varied applications, particularly in robotics and artificial intelligence, where the ability to determine the feasibility of reaching a target state from an initial state is of strategic importance.
Our approach relies on using a two-state automaton, also known as VASS (Vector Addition System with States). We represent authorized movements in vector form, where each vector defines a possible transition from a given state. The use of VASS allows us to elegantly and accurately model the dynamics of movements.
We also employ the A* algorithm to provide an efficient search methodology in discovering the optimal path between the initial state and the target state. This combination of VASS automaton and A* algorithm constitutes a powerful approach for solving reachability problems.


# Technologies Used:
Programming Language: Python
Development Tools: matplotlib.pyplot , Jupyter Notebook

# Usage
Make sure to use a tool that supports the matplotlib.pyplot library, such as Jupyter Notebook, to execute this code.
To select a heuristic function, follow the instructions below:
- Remove the comments before the declaration and return of the heuristic function you wish to use.
- Comment out the other heuristic functions by adding a # before their declaration.
