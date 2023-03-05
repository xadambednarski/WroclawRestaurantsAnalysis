import networkx as nx
from matplotlib import pyplot as plt
import random
'''
1. 
3 typy sieci: liniowa, pierscieniowa i kraty
wyznaczyc srednia dlugosc trasy (waga krawedzi 1)

2. wygenerowac losowa siec:
a) podejscie 1: generujemy graf pelny i usuwamy krawedzie tak dlugo poki chcemy ale tak zeby pozostal spojny
b) skorzystac z wbudowanego w networkx generatora
'''

#1
pc_list = ['pc1', 'pc2', 'pc3', 'pc4', 'pc5', 'pc6', 'pc7', 'pc8', 'pc9']
glin = nx.Graph()
glin.add_nodes_from(pc_list)
for i in range(len(pc_list)-1):
    glin.add_edge(pc_list[i], pc_list[i+1])
avgpath_lin = nx.average_shortest_path_length(glin)
delay_lin = nx.betweenness_centrality(glin)
print('Average shortest path for linear network:', avgpath_lin)
print('Average betweenenness centrality in linear network:', delay_lin)
# nx.draw(glin, with_labels=True, node_size=1000)
# plt.show()
gring = nx.Graph()
gring.add_nodes_from(pc_list)
for i in range(len(pc_list)-1):
    gring.add_edge(pc_list[i], pc_list[i+1])
gring.add_edge(pc_list[0], pc_list[8])
pos = nx.spring_layout(gring)
avgpath_gring = nx.average_shortest_path_length(gring)
delay_gring = nx.betweenness_centrality(gring)
print('Average shortest path for annular network:', avgpath_gring)
print('Average betweenenness centrality in annular network:', delay_gring)
# nx.draw(gring, with_labels=True, node_size=1000, pos=pos)
# plt.show()

#2
s = list()
curr = random.choice(pc_list)
s.append(curr)
while len(s) != len(pc_list):
    neighb = random
