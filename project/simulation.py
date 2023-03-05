from matplotlib import pyplot as plt, animation
import networkx as nx
import random
from scraper import read_json_matrix, read_json_dict

k = 0
categories = ['grill', 'noodles', 'pizza', 'sandwich', 'pollo', 'candy']
matrix = read_json_matrix()
restaurants = read_json_dict()

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()
G = nx.Graph()
restaurants_names = list(restaurants.keys())
G.add_nodes_from(restaurants_names)
competitors = []
deleted = []
n = len(matrix)
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][0] + matrix[j][0] == 2 or matrix[i][1] + matrix[j][1] == 2 \
            or matrix[i][2] + matrix[j][2] == 2 or matrix[i][3] + matrix[j][3] == 2 \
                or matrix[i][4] + matrix[j][4] == 2 or matrix[i][5] + matrix[j][5] == 2 and \
                (restaurants_names[j], restaurants_names[i]) not in competitors and \
                (restaurants_names[i], restaurants_names[j]) not in competitors:
            competitors.append((restaurants_names[i], restaurants_names[j]))
G.add_edges_from(competitors)
pos = nx.spring_layout(G)
nx.draw_networkx(G, with_labels=True, pos=pos)


def update_restaurants():
    global categories, restaurants, competitors
    for i in list(restaurants):
        for j in list(restaurants):
            try:
                if restaurants[i][0] in categories and restaurants[j][0] in categories:
                    restaurants[i][1] = float(restaurants[i][1])
                    restaurants[j][1] = float(restaurants[j][1])
                    if (i, j) in competitors or (j, i) in competitors:
                        if restaurants[i][1] < restaurants[j][1]:
                            restaurants[j][1] += 0.05
                            restaurants[i][1] -= 0.05
                            if restaurants[i][1] < 3.5:
                                deleted.append(restaurants.pop(i))
                                if G.has_node(i):
                                    G.remove_node(i)
                                try:
                                    competitors.remove((i, j))
                                except ValueError:
                                    try:
                                        competitors.remove((j, i))
                                    except ValueError:
                                        continue
                            break
                        elif restaurants[i][1] > restaurants[j][1]:
                            restaurants[i][1] += 0.05
                            restaurants[j][1] -= 0.05
                            if restaurants[i][1] < 3.5:
                                deleted.append(restaurants.pop(i))
                                if G.has_node(i):
                                    G.remove_node(i)
                                try:
                                    competitors.remove((i, j))
                                except ValueError:
                                    try:
                                        competitors.remove((j, i))
                                    except ValueError:
                                        continue
                            break
                elif restaurants[i][0] not in categories and restaurants[j][0] not in categories:
                    restaurants[i][0][1] = float(restaurants[i][0][1])
                    restaurants[j][0][1] = float(restaurants[j][0][1])
                    if (i, j) in competitors or (j, i) in competitors:
                        if restaurants[i][0][1] < restaurants[j][0][1]:
                            restaurants[i][0][1] -= 0.05
                            restaurants[j][0][1] += 0.05
                            if restaurants[i][0][1] < 3.5:
                                deleted.append(restaurants.pop(i))
                                if G.has_node(i):
                                    G.remove_node(i)
                                try:
                                    competitors.remove((i, j))
                                except ValueError:
                                    competitors.remove((j, i))
                            break
                        elif restaurants[i][0][1] > restaurants[j][0][1]:
                            restaurants[i][0][1] += 0.05
                            restaurants[j][0][1] -= 0.05
                            if restaurants[i][0][1] < 3.5:
                                deleted.append(restaurants.pop(i))
                                if G.has_node(i):
                                    G.remove_node(i)
                                try:
                                    competitors.remove((i, j))
                                except ValueError:
                                    competitors.remove((j, i))
                            break
                elif restaurants[i][0] in categories and restaurants[j][0] not in categories:
                    restaurants[i][1] = float(restaurants[i][1])
                    restaurants[j][0][1] = float(restaurants[j][0][1])
                    if (i, j) in competitors or (j, i) in competitors:
                        if restaurants[i][1] < restaurants[j][0][1]:
                            restaurants[i][1] -= 0.05
                            restaurants[j][0][1] += 0.05
                            if restaurants[i][1] < 3.5:
                                if G.has_node(i):
                                    G.remove_node(i)
                                deleted.append(restaurants.pop(i))
                                try:
                                    competitors.remove((i, j))
                                except ValueError:
                                    competitors.remove((j, i))
                            break
                        elif restaurants[i][1] > restaurants[j][0][1]:
                            restaurants[i][1] += 0.05
                            restaurants[j][0][1] -= 0.05
                            if restaurants[i][1] < 3.5:
                                if G.has_node(i):
                                    G.remove_node(i)
                                deleted.append(restaurants.pop(i))
                                try:
                                    competitors.remove((i, j))
                                except ValueError:
                                    competitors.remove((j, i))
                            break
                        else:
                            break
            except KeyError:
                continue


def node_sizes(restaurants):
    sizes = []
    for i in restaurants:
        if restaurants[i][0] in categories:
            rating = restaurants[i][1]
        else:
            rating = restaurants[i][0][1]
        sizes.append(rating * 1000)
    return sizes


def animate(frame):
    global pos, restaurants, k
    fig.clear()
    update_restaurants()
    sizes = node_sizes(restaurants)
    nx.draw_networkx(G, with_labels=True, node_size=sizes, pos=pos)
    plt.title(f'Epoka: {k}')
    print(f'Centralnosc:\n {nx.betweenness_centrality(G)}')
    print(f'Srednia grafu: {nx.diameter(G)}')
    print(f'Closeness centrality:\n {nx.closeness_centrality(G)}')
    k += 1


ani = animation.FuncAnimation(fig, animate, frames=30, interval=500, repeat=False)
plt.show()