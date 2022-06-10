import math

from aco import ACO, Graph

def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)

def main_aco(file):
    cities = []
    points = []
    with open(file) as f:
        for line in f.readlines():
            city = line.split(' ')
            cities.append(dict(index=float(city[0]), x=float(city[1]), y=float(city[2])))
            points.append((float(city[1]), float(city[2])))
    cost_matrix = []
    rank = len(cities)

    for i in range(rank):
        row = []
        for j in range(rank):
            row.append(distance(cities[i], cities[j]))
        cost_matrix.append(row)
    aco = ACO(ant_count=len(cities), generations=100, alpha=1, beta=1, rho=0.5, q=10,strategy=2)
    graph = Graph(cost_matrix, rank)
    path, cost = aco.solve(graph)
    print('ACO')
    print(cost)
    return cost

if __name__ == '__main__':
    main_aco()