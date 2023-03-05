import requests
from bs4 import BeautifulSoup
import numpy as np
import json
from json import JSONEncoder


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def parser(categories):
    global titles, ratings, class_ratings, class_titles, category
    restaurants = {}
    for category in categories:
        if category == 'grill':
            class_ratings = 'ba hq bb by fi fh ht br hw ah bf bg'
            class_titles = 'ba b8 bb b9 dq cx cv hk bc'
        elif category == 'noodles':
            class_ratings = 'ba hv bb by fi fh hx hy hz i0 ah bf bg'
            class_titles = 'ba b8 bb b9 dq cx cv hp bc'
        elif category == 'pizza':
            class_ratings = 'ba hq bb by fi fh hr br hu ah bf bg'
            class_titles = 'ba b8 bb b9 dq cx cv hk bc'
        elif category == 'sandwich':
            class_ratings = 'ba hq bb by fi fh hr hs ht hu ah bf bg'
            class_titles = 'ba b8 bb b9 dq cx cv hk bc'
        elif category == 'pollo':
            class_ratings = 'ba hv bb by fi fh hw hy hz hx ah bf bg'
            class_titles = 'ba b8 bb b9 dq cx cv hp bc'
        elif category == 'candy':
            class_ratings = 'ba hq bb by fi fh hr br hu ah bf bg'
            class_titles = 'ba b8 bb b9 dq cx cv hk bc'
        num_of_rest = 0
        url = 'https://www.ubereats.com/pl/category/wroclaw-dolnoslaskie/' + category
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id='main-content')
        restaurants_list = results.find_all("div", class_='h1 h2 h3 h4 h5 h6 h7')
        for restaurant_div in restaurants_list:
            titles = restaurant_div.find_all("p", class_=class_titles)
            ratings = restaurant_div.find_all("div", class_=class_ratings)
        for (restaurant, rating) in zip(titles, ratings):
            if num_of_rest < 30:
                if restaurant.text not in restaurants:
                    restaurants[restaurant.text] = (category, rating.text)
                elif isinstance(restaurants[restaurant.text], list):
                    restaurants[restaurant.text].append((category, rating.text))
                else:
                    restaurants[restaurant.text] = [restaurants[restaurant.text],
                                                    (category, rating.text)]
                num_of_rest += 1
    return restaurants


def write_json_matrix(matrix):
    np_data = {"array": matrix}
    with open("json_matrix.json", "w") as write_file:
        json.dump(np_data, write_file, cls=NumpyArrayEncoder)


def write_json_dict(restaurants):
    with open("json_dict.json", "w", encoding="utf-8") as outfile:
        json.dump(restaurants, outfile, ensure_ascii=False)


def read_json_matrix(file="json_matrix.json"):
    with open(file, "r") as read_file:
        decoded_array = json.load(read_file)
        return np.asarray(decoded_array["array"])


def read_json_dict(file="json_dict.json", ):
    with open(file, encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data

