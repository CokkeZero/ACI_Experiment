import math
from genetic import GeneticAlgorithm
from util import City
from aco import ACO, Graph
from plot import plot


def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


def main_genetic(file):
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

    ga = GeneticAlgorithm(cities=cities, iterations=100, population_size=20,
                                          elites_num=20, mutation_rate=0.01, greedy_seed=1,
                                          roulette_selection=True, plot_progress=False)
    ga.run()
    cost = ga.best_distance()
    #graph = Graph(cost_matrix, rank)
    #path, cost = aco.solve(graph)
    #print('cost: {}, path: {}'.format(sa.best_fitness, sa.route))
    #plot(points, path)
    print('Genetic')
    print(cost)
    return cost

if __name__ == '__main__':
    main_genetic()