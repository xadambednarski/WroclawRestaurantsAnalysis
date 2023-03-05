from pyvis.network import Network
from collections import Counter


def show_network(restaurants, edges, categories):
    links = []
    for i in edges:
        links.append(i[0])
        links.append(i[1])
    restaurants_names = list(restaurants.keys())
    edges_per_node = dict(Counter(links))
    for i in restaurants_names:
        if i not in edges_per_node.keys():
            edges_per_node[i] = 0
    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
    net.barnes_hut()
    for i in restaurants:
        print(i)
        if restaurants[i][0] in categories:
            if isinstance(restaurants[i][1], str):
                rating = restaurants[i][1]
            else:
                rating = 4.5
            net.add_node(i, label=i, title=f'Rating:\n{rating}\nLinks:\n{edges_per_node[i]}\nCuisines:\n{restaurants[i][0]}')
        else:
            cuisines = []
            for k in range(len(restaurants[i])):
                cuisine_name = restaurants[i][k][0]
                if cuisine_name not in cuisines:
                    cuisines.append(cuisine_name)
            rating = restaurants[i][0][1]
            net.add_node(i, label=i, title=f'Rating:\n{rating}\nLinks:\n{edges_per_node[i]}\nCuisines:\n{cuisines}')
    for i in edges:
        if i[0] == i[1]:
            edges.remove(i)
        else:
            net.add_edge(i[0], i[1], weight=0.85)
    net.show("restaurants.html")
