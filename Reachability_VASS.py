import matplotlib.pyplot as plt
import heapq
from datetime import datetime

class Node:
    nodes_created = 0
    def __init__(self, value, p, parent=None):
        self.value = value
        self.parent = parent
        self.vectors = p
        self.cout = 0
        self.is_goal = 0
        Node.nodes_created += 1

    def generate_successors(self, goal_state):
        successors = []
        for vector in self.vectors:
            new_value = tuple(v + nv for v, nv in zip(self.value, vector))
            new_node = self.vect_valid(vector, new_value)
            new_node.parent = self
            new_node.cout = self.cout + 1

            if new_node.value == goal_state:
                new_node.is_goal = 1

            successors.append(new_node)

        return successors

    def vect_valid(self, vector, new_value):
        if vector == (2, 2):
            successor = Node(new_value, p)
        elif vector == (0, 1):
            successor = Node(new_value, q)
        elif vector == (-5, -5):
            successor = Node(new_value, q)
        elif vector == (-2, 0):
            successor = Node(new_value, p)
        return successor
        
    #-------------------------------------------------------------------------------------------------------#
    def heuristic(self, goal_state):
         #-Euclidean distance 
        return ((goal_state[0] - self.value[0]) ** 2 + (goal_state[1] - self.value[1]) ** 2) ** 0.5
    #-------------------------------------------------------------------------------------------------------#    
    #def heuristic(self, goal_state):
        #-Euclidean distance h(e) = p(e)*alpha + d(e)*(1-alpha)
        #alpha = 0.5
        #distance = ((goal_state[0] - self.value[0]) ** 2 + (goal_state[1] - self.value[1]) ** 2) ** 0.5
        #return distance * alpha + self.cout * (1 - alpha)
    #-------------------------------------------------------------------------------------------------------#       
    #def heuristic(self, goal_state):
        #-Manhattan distance 
        #return abs(goal_state[0] - self.value[0]) + abs(goal_state[1] - self.value[1])
    #-------------------------------------------------------------------------------------------------------#   
    #def heuristic(self, goal_state):
        #-Chebyshev distance 
        #return max( abs(goal_state[0] - self.value[0]) , abs(goal_state[1] - self.value[1]) )
    #-------------------------------------------------------------------------------------------------------#       
    #def heuristic(self, goal_state):
        #-Random distance 
        #return 1
    #-------------------------------------------------------------------------------------------------------#
    
    def __lt__(self, other):
        # Define the less-than comparison for heap ordering
        return (self.cout + self.heuristic(goal_state)) < (other.cout + other.heuristic(goal_state))


def a_star_search(etat_initial, goal_state):
    heap = [etat_initial]
    visited = set()

    while heap:
        current_node = heapq.heappop(heap)
        #print(current_node.value)
        if current_node.value == goal_state:
            return construct_path(current_node)

        if current_node.value in visited:
            continue

        visited.add(current_node.value)

        successors = current_node.generate_successors(goal_state)
        for successor in successors:
            heapq.heappush(heap, successor)

    return []


def construct_path(node):
    path = []
    while node:
        path.insert(0, node.value)
        node = node.parent
    return path


def display_path_steps(path):
    for i, node in enumerate(path):
        print(f"Step {i}: {node}")


def display_path(path, start, goal):
    x_values = [node[0] for node in path]
    y_values = [node[1] for node in path]

    plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label='Path', zorder=1)
    plt.scatter(start[0], start[1], marker='s', color='g', label='Start', zorder=3, s=50)
    plt.scatter(goal[0], goal[1], marker='*', color='r', label='Goal', zorder=3, s=150)

    for i in range(len(path) - 1):
        plt.annotate(
            "",
            xy=path[i + 1], xycoords='data',
            xytext=path[i], textcoords='data',
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='black')
        )

    plt.title('A* Path')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()


#define Automata
p = [(2, 2), (-5, -5)]
q = [(0, 1), (-2, 0)]
        
#Initial state
etat_initial = Node((0, 0), p)

#Goal state 
goal_state = (-33, 5)

#Search path
start_time = datetime.now()
path_to_goal = a_star_search(etat_initial, goal_state)
end_time = datetime.now()

#Display path Graph
print("\n-> " + "Path Graph :")
display_path(path_to_goal, etat_initial.value, goal_state)

#Nodes Created
print("\n-> " + f'Number of nodes created: {Node.nodes_created}')

#Duration
print("\n-> " +'Duration: {:.6f} seconds'.format((end_time - start_time).total_seconds()))

#Display all path steps
print("\n-> " + "Path Steps :\n")
display_path_steps(path_to_goal)