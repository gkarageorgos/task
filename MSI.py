import networkx as nx
import matplotlib.pyplot as plt

# Creat a random tree with n nodes
n = 20
T = nx.random_tree(n)
# copy tree T
Tcopy = nx.Graph(T)
# Maximum Independent Set
M = []
while len(Tcopy):
    # the set of remaining leaves in Tcopy
    leaves = []
    # the neighbors of the leaves
    neighborhood = []
    # for every connected components
    for cc in nx.connected_components(Tcopy):
        G1 = Tcopy.subgraph(cc)
        if len(cc) == 1:
            leaves.append(list(G1.nodes())[0])
        elif len(cc) == 2:
            leaves.append(list(G1.nodes())[0])
            neighborhood.append(list(G1.nodes())[1])
        else:
            for v in G1.nodes():
                if G1.degree(v) == 1:
                    leaves.append(v)
                    if neighborhood.count(list(G1.neighbors(v))[0]) == 0:
                        neighborhood.append(list(G1.neighbors(v))[0])
    M += leaves
    Tcopy.remove_nodes_from(leaves+neighborhood)

print(M, "is the maximum independent set of the tree")
color_map = []
for v in T.nodes():
    if M.count(v):
        color_map.append('red')
    else:
        color_map.append('blue')
pos = nx.layout.kamada_kawai_layout(T)
nx.draw_networkx(T, pos, node_color=color_map, width=1.0)
plt.show()
