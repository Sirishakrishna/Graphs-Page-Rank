
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

n = 50 #5 nodes
m = 100 #10 edges
G= nx.gnm_random_graph(n,m)
pr = nx.pagerank(G, alpha=0.1)
print pr

#Plotting Values
plt.hist(pr.keys(), weights=pr.values(), bins=range(50), color='y')

plt.show()


