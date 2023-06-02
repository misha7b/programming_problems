
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import numpy as np

def csv_to_matrix(filename):
    
    with open(filename, 'r') as file:
        lines = file.readlines()

   
    lines = [line.strip() for line in lines]

    
    lines = lines[1:]

    
    matrix_data = [[ord(char) for char in line] for line in lines]

   
    matrix = np.array(matrix_data)

    return matrix


filename = '/Users/michaelbelyaev/Desktop/Programming/Python/programming_problems/blockade/input.txt'
matrix = csv_to_matrix(filename)

#print(matrix)

unique_values = np.unique(matrix)
regions = (len(unique_values)+1)

#print(regions)


mapping_dict = {65: 0}
emumerated_value = 1
for i, element in enumerate(unique_values):
    if element != 65:
        mapping_dict[element] = emumerated_value
        emumerated_value += 1

mapped_matrix = np.vectorize(mapping_dict.get)(matrix)

#print(mapped_matrix)

graph_matrix = np.zeros((regions, regions), dtype=int)

for i in range(len(mapped_matrix)):
    for j in range(len(mapped_matrix[i])):
        
        if j > 0:
            if mapped_matrix[i][j] != mapped_matrix[i][j - 1]:

                graph_matrix[mapped_matrix[i][j]][mapped_matrix[i][j - 1]] = 1
                graph_matrix[mapped_matrix[i][j - 1]][mapped_matrix[i][j]] = 1

        if i > 0:

            if mapped_matrix[i][j] != mapped_matrix[i - 1][j]:

                graph_matrix[mapped_matrix[i][j]][mapped_matrix[i - 1][j]] = 1
                graph_matrix[mapped_matrix[i - 1][j]][mapped_matrix[i][j]] = 1
        

        if i < len(mapped_matrix) - 1:

                if mapped_matrix[i][j] != mapped_matrix[i + 1][j]:

                    graph_matrix[mapped_matrix[i][j]][mapped_matrix[i + 1][j]] = 1
                    graph_matrix[mapped_matrix[i + 1][j]][mapped_matrix[i][j]] = 1
        
        if j < len(mapped_matrix[i]) - 1:

                if mapped_matrix[i][j] != mapped_matrix[i][j + 1]:

                    graph_matrix[mapped_matrix[i][j]][mapped_matrix[i][j + 1]] = 1
                    graph_matrix[mapped_matrix[i][j + 1]][mapped_matrix[i][j]] = 1

        if i == 0 or j == 0 or i == len(mapped_matrix) - 1 or j == len(mapped_matrix[i]) - 1:
             
            graph_matrix[mapped_matrix[i][j]][regions - 1] = 1
            graph_matrix[regions - 1][mapped_matrix[i][j]] = 1

#print(graph_matrix)

G = nx.Graph(graph_matrix)


def djikstras_algorithm(graph, start, finish):
     
    distances = {}
    previous_nodes = {}
    queue = []

    for node in graph.nodes:
        distances[node] = float('inf')
        previous_nodes[node] = None
        queue.append(node)
       
    
    distances[start] = 0

    while len(queue) > 0:
        u = min(queue, key=lambda node: distances[node])
        if u == finish:
            break
        queue.remove(u)

        for neighbour in graph.neighbors(u):
            if neighbour in queue:
                
                temp = distances[u] + 1
                
                if temp < distances[neighbour]:
                    distances[neighbour] = temp
                    previous_nodes[neighbour] = u
    
    shortest_path = []
    current_node = finish

    while current_node != start:
        shortest_path.append(current_node)
        current_node = previous_nodes[current_node]
    
    shortest_path.append(start)
    shortest_path.reverse()

    return shortest_path, distances


                
shortest_path, distance = (djikstras_algorithm(G, 7, 0) )


radius = 1.0
num_nodes = G.number_of_nodes()
angle = 2 * np.pi / num_nodes
positions = {node: (np.cos(i * angle), np.sin(i * angle)) for i, node in enumerate(G.nodes)}

nx.draw(G, pos=positions, with_labels=True)

path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]


nx.draw_networkx_nodes(G, pos=positions, nodelist=shortest_path, node_color='r')
nx.draw_networkx_edges(G, pos=positions, edgelist=path_edges, edge_color='r', width=2)

must_visit = set()

for i in range(len(shortest_path)):
    must_visit.add(shortest_path[i])

#print(must_visit)

capital_neighbors = (G.neighbors(0))



H = G.copy()

for i in (capital_neighbors):
    H.remove_edge(0, i)
    path, d = djikstras_algorithm(G, 0, i)
    if path == []:
        print(-1)
    else:
        for j in path:
            must_visit.add(j)


#print(must_visit)

print(len(must_visit) - 2)



plt.show()

  
















        

  

 

   

    
     


     
     
    


     










