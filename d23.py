import sys
import networkx as nx
from collections import defaultdict
from itertools import product


G = nx.Graph()
neighbors = defaultdict(set)
t_nodes = set()
with open(sys.argv[1]) as in_f:
    for line in in_f:
        nodes = line.strip().split('-')
        neighbors[nodes[0]].add(nodes[1])
        neighbors[nodes[1]].add(nodes[0])
        G.add_node(nodes[0])
        G.add_node(nodes[1])
        G.add_edge(nodes[0], nodes[1])
        if nodes[0][0] == 't':
            t_nodes.add(nodes[0])
        if nodes[1][0] == 't':
            t_nodes.add(nodes[1])

silver = set()
for a, b, c in product(neighbors, neighbors, t_nodes):
    if a in neighbors[b] and a in neighbors[c] and b in neighbors[c]:
        silver.add(str(sorted([a, b, c])))
print(len(silver))

gold = max(nx.find_cliques(G), key=len)
print(','.join(sorted(gold)))
