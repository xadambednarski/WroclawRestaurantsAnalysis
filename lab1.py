import networkx as nx
from matplotlib import pyplot as plt


g = nx.Graph()
coach = 'Julian Nagelsmann'
team = ['Manuel Neuer', 'Alphonso Davies', 'Matthijs de Ligt', 'Lucas Hernández', 'Dayot Upamecano',
        'Leon Goretzka', 'Joshua Kimmich', 'Jamal Musiala', 'Sadio Mané',
        'Thomas Müller', 'Leroy Sané']
attackers = ['Sadio Mane', 'Thomas Müller', 'Leroy Sane']
midfielders = ['Leon Goretzka', 'Joshua Kimmich', 'Jamal Musiala']
defenders = ['Manuel Neuer', 'Alphonso Davies', 'Matthijs de Ligt', 'Lucas Hernández', 'Dayot Upamecano']
g.add_nodes_from(team)
g.add_node(coach)
for i in team:
        for j in team:
                if i and j in attackers or i and j in midfielders or i and j in defenders:
                        g.add_edge(i, j, weight=3)
                else:
                        g.add_edge(i, j, weight=1)
        g.remove_edge(i, i)
        g.add_edge(i, coach, weight=5)
node_sizes = [20000 if node == coach else 12000 for node in g.nodes()]
options = {
        "node_color": "#A0CBE2",
        "edge_cmap": plt.cm.Blues,
        "with_labels": True,
        "node_size": node_sizes
}
pos = nx.spring_layout(g, seed=1)
fig = plt.figure()
nx.draw(g, pos, **options)
fig.set_facecolor("tab:blue")
for edge in g.edges(data='weight'):
    nx.draw_networkx_edges(g, pos, edgelist=[edge], width=edge[2])
plt.show()
def shortest_longest_path(g):
        lsp = nx.all_pairs_dijkstra_path_length(g)
        paths = []
        for i in lsp:
                node = max(i[1], key=i[1].get)
                paths.append((i[0], node, len(nx.shortest_path(g, i[0], node))))
        paths.sort(key=lambda x: x[2], reverse=True)
        print(paths[0])
shortest_longest_path(g)