import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency matrix
A = np.array([[0, 1, 1, 0],
              [1, 0, 1, 1],
              [1, 1, 0, 1],
              [0, 1, 1, 0]])

# Create a graph from the adjacency matrix
G = nx.Graph(A)

# Draw the graph
nx.draw(G, with_labels=True)

# Show the plot
plt.show()