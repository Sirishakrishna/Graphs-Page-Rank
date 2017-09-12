import networkx as nx
import matplotlib.pyplot as plt
import numpy as np



n = 500 #50 nodes
m = 1000 #100 edges
G1= nx.gnm_random_graph(n,m)
pr1 = nx.pagerank(G1, alpha=0.1)

G2= nx.gnm_random_graph(n,m)
pr2 = nx.pagerank(G2, alpha=0.2)

G3= nx.gnm_random_graph(n,m)
pr3 = nx.pagerank(G3, alpha=0.3)

G4= nx.gnm_random_graph(n,m)
pr4 = nx.pagerank(G3, alpha=0.4)

plt.hist(pr1.keys(), weights=pr1.values(), bins = range(200), label='alpha=0.1')
plt.hist(pr2.keys(), weights=pr2.values(), bins = range(200), label='alpha=0.2')
plt.hist(pr3.keys(), weights=pr3.values(), bins = range(200), label='alpha=0.3')
plt.hist(pr4.keys(), weights=pr4.values(), bins = range(200), label='alpha=0.4')

#bins = np.linspace(-10, 10, 100)
#plt.hist(pr1, bins, alpha=0.5, label='Complete Graph')
#plt.hist(pr2, bins, alpha=0.5, label='Cyclic Graph')
plt.legend(loc='upper right')

plt.xlabel('Pagerank for Varying alpha Values')

plt.show()