from scraper import *
from visualize import show_network


if __name__ == '__main__':
    categories = ['grill', 'noodles', 'pizza', 'sandwich', 'pollo', 'candy']
    restaurants = parser(categories)
    write_json_dict(restaurants)
    matrix = np.zeros((len(restaurants), len(categories)))
    for i, restaurant in enumerate(restaurants.keys()):
        if isinstance(restaurants[restaurant], list):
            for j in restaurants[restaurant]:
                matrix[i, categories.index(j[0])] = 1
        else:
            matrix[i, categories.index(restaurants[restaurant][0])] = 1
    write_json_matrix(matrix)
    restaurants_names = list(restaurants.keys())
    competitors = []
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][0] + matrix[j][0] == 2 or matrix[i][1] + matrix[j][1] == 2 \
                or matrix[i][2] + matrix[j][2] == 2 or matrix[i][3] + matrix[j][3] == 2 \
                    or matrix[i][4] + matrix[j][4] == 2 or matrix[i][5] + matrix[j][5] == 2 and \
                    (restaurants_names[j], restaurants_names[i]) not in competitors and \
                    (restaurants_names[i], restaurants_names[j]) not in competitors:
                competitors.append((restaurants_names[i], restaurants_names[j]))
    show_network(restaurants, competitors, categories)





