import math
from anneal import SimAnneal
from util import City
from aco import ACO, Graph
from plot import plot


def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


def main_anneal(file):
    cities = []
    points = []
    cities_ann = []
    with open(file) as f:
        for line in f.readlines():
            city = line.split(' ')
            cities_ann.append(dict(index=float(city[0]), x=float(city[1]), y=float(city[2])))
            points.append((float(city[1]), float(city[2])))
            cities.append(City(float(city[1]), float(city[2])))
    cost_matrix = []
    rank = len(cities)

    sa = SimAnneal(cities, alpha=1, temperature=0.01, stopping_iter=100)
    sa.run()
    cost = sa.best_fitness
    #graph = Graph(cost_matrix, rank)
    #path, cost = aco.solve(graph)
    #print('cost: {}, path: {}'.format(sa.best_fitness, sa.route))
    #plot(points, path)
    print('Anneal')
    print(cost)
    return cost

if __name__ == '__main__':
    main_anneal()