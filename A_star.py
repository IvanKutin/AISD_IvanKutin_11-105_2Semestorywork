import matplotlib.pyplot as plt
import time


class Graph:

    def __init__(self, list):
        self.list = list
        self.open = []
        self.close = []

    def __getitem__(nodenames) -> float:
        nodeAname, nodeBname = nodenames
        return None

    def __setitem__(self, nodenames, weight):
        pass

    def shortestPath_A_star(self, *args):
        self.s = args[0]
        self.f = args[1]
        self.list[self.s][2] = 0
        self.list[self.s][3] = 0
        self.x2 = self.list[self.s][0][0]
        self.y2 = self.list[self.s][0][1]
        self.x3 = self.list[self.f][0][0]
        self.y3 = self.list[self.f][0][1]
        self.list[self.s][3] = (abs(self.x2 - self.x3) ** 2 + abs(self.y2 - self.y3) ** 2) ** 0.5

        def __A_star(s):
            self.x1 = self.list[self.s][0][0]
            self.y1 = self.list[self.s][0][1]
            for i in self.list[self.s][1]:
                if i not in self.close:
                    self.x2 = self.list[i][0][0]
                    self.y2 = self.list[i][0][1]
                    if self.list[i][2] > (abs(self.x1 - self.x2) ** 2 + abs(self.y1 - self.y2) ** 2) ** 0.5 + \
                            self.list[s][2]:
                        self.list[i][2] = (abs(self.x1 - self.x2) ** 2 + abs(self.y1 - self.y2) ** 2) ** 0.5 + \
                                          self.list[s][2]
                        self.list[i].append(self.s)
            for i in self.list[self.s][1]:
                if i not in self.close:
                    self.x2 = self.list[i][0][0]
                    self.y2 = self.list[i][0][1]
                    self.x3 = self.list[self.f][0][0]
                    self.y3 = self.list[self.f][0][1]
                    self.list[i][3] = (abs(self.x2 - self.x3) ** 2 + abs(self.y2 - self.y3) ** 2) ** 0.5
            self.min = float('inf')
            for i in self.list[self.s][1]:
                if i not in self.close:
                    if self.list[i][2] + self.list[i][3] < self.min:
                        self.min = self.list[i][2] + self.list[i][3]
            for i in self.list[s][1]:
                if i not in self.close:
                    if self.list[i][2] + self.list[i][3] == self.min:
                        self.list[i].append(self.s)
                        if i == self.f:
                            self.way = [i]
                            while i is not args[0]:
                                self.way.append(self.list[i][4])
                                i = self.list[i][4]
                            self.way.reverse()
                            self.string = str(self.way[0])

                            for i in range(1, len(self.way)):
                                self.string = self.string + '->' + str(self.way[i])
                            self.length = self.list[self.list[self.f][4]][2] + self.list[self.list[self.f][4]][3]
                            return self.string, self.length
                        else:
                            self.close.append(self.s)
                            self.list[i].append(self.s)
                            return __A_star(i)

        return __A_star(self.s)


times = []

# Так как алгоритм А* использует эвристическое расстояние, в списке каждой вершины хранятся её координаты, расстояние же между вершинами будет вычисляться по теореме пифагора


# 1 тест

list = {'A1': [(0, 0), ['A2'], float('inf'), 0], 'A2': [(1, 0), ['A1', 'A3'], float('inf'), 0],
        'A3': [(2, 0), ['A2'], float('inf'), 0]}
graph = Graph(list)
time1 = time.time()
print(graph.shortestPath_A_star('A2', 'A3'))
for i in range(1000):
    graph.shortestPath_A_star('A2', 'A3')
times.append(time.time() - time1)
print(times)

# 2 тест
list = {'A1': [(0, 0), ['B1', 'A2'], float('inf'), 0], 'A2': [(1, 0), ['A1', 'A3', 'B2'], float('inf'), 0],
        'A3': [(2, 0), ['B3', 'A2'], float('inf'), 0], 'B1': [(0, 1), ['A1', 'B2'], float('inf'), 0],
        'B2': [(1, 1), ['A2', 'B1', 'B3'], float('inf'), 0], 'B3': [(1, 2), ['B2', 'A3'], float('inf'), 0]
        }
graph = Graph(list)
time1 = time.time()
print(graph.shortestPath_A_star('A1', 'B3'))
for i in range(1000):
    graph.shortestPath_A_star('A1', 'B3')
times.append(time.time() - time1)
print(times)

# 3 тест
list = {'A1': [(0, 0), ['B1', 'A2'], float('inf'), 0], 'A2': [(1, 0), ['A1', 'A3', 'B2'], float('inf'), 0],
        'A3': [(2, 0), ['B3', 'A2'], float('inf'), 0], 'B1': [(0, 1), ['A1', 'B2', 'C1'], float('inf'), 0],
        'B2': [(1, 1), ['A2', 'B1', 'B3', 'C2'], float('inf'), 0], 'B3': [(1, 2), ['B2', 'A3', 'C3'], float('inf'), 0],
        'C1': [(0, 2), ['B1', 'C2'], float('inf'), 0], 'C2': [(1, 2), ['C1', 'C3', 'B2'], float('inf'), 0],
        'C3': [(2, 2), ['B3', 'C2'], float('inf'), 0]
        }
graph = Graph(list)
time1 = time.time()
print(graph.shortestPath_A_star('A1', 'C3'))
for i in range(1000):
    graph.shortestPath_A_star('A1', 'C3')
times.append(time.time() - time1)
print(times)

# 4 тест
list = {'A1': [(0, 0), ['B1', 'A2'], float('inf'), 0], 'A2': [(1, 0), ['A1', 'A3', 'B2'], float('inf'), 0],
        'A3': [(2, 0), ['B3', 'A2'], float('inf'), 0], 'B1': [(0, 1), ['A1', 'B2', 'C1'], float('inf'), 0],
        'B2': [(1, 1), ['A2', 'B1', 'B3', 'C2'], float('inf'), 0], 'B3': [(1, 2), ['B2', 'A3', 'C3'], float('inf'), 0],
        'C1': [(0, 2), ['B1', 'C2', 'D1'], float('inf'), 0], 'C2': [(1, 2), ['C1', 'C3', 'B2', 'D2'], float('inf'), 0],
        'C3': [(2, 2), ['B3', 'C2', 'D3'], float('inf'), 0], 'D1': [(0, 3), ['C1', 'D2'], float('inf'), 0],
        'D2': [(1, 3), ['D1', 'D3', 'C2'], float('inf'), 0],
        'D3': [(2, 3), ['C3', 'D2'], float('inf'), 0]}
graph = Graph(list)
time1 = time.time()
print(graph.shortestPath_A_star('A1', 'D3'))
for i in range(1000):
    graph.shortestPath_A_star('A1', 'D3')
times.append(time.time() - time1)
print(times)

# 5 тест
list = {'A1': [(0, 0), ['B1', 'A2'], float('inf'), 0], 'A2': [(1, 0), ['A1', 'A3', 'B2'], float('inf'), 0],
        'A3': [(2, 0), ['B3', 'A2'], float('inf'), 0], 'B1': [(0, 1), ['A1', 'B2', 'C1'], float('inf'), 0],
        'B2': [(1, 1), ['A2', 'B1', 'B3', 'C2'], float('inf'), 0], 'B3': [(1, 2), ['B2', 'A3', 'C3'], float('inf'), 0],
        'C1': [(0, 2), ['B1', 'C2', 'D1'], float('inf'), 0], 'C2': [(1, 2), ['C1', 'C3', 'B2', 'D2'], float('inf'), 0],
        'C3': [(2, 2), ['B3', 'C2', 'D3'], float('inf'), 0], 'D1': [(0, 3), ['C1', 'D2', 'E1'], float('inf'), 0],
        'D2': [(1, 3), ['D1', 'D3', 'C2', 'E2'], float('inf'), 0],
        'D3': [(2, 3), ['B3', 'D2', 'E3'], float('inf'), 0], 'E1': [(0, 4), ['D1', 'E2'], float('inf'), 0],
        'E2': [(1, 4), ['E1', 'E3', 'D2'], float('inf'), 0],
        'E3': [(2, 4), ['D3', 'E2'], float('inf'), 0]
        }
graph = Graph(list)
time1 = time.time()
print(graph.shortestPath_A_star('A1', 'E3'))
for i in range(1000):
    graph.shortestPath_A_star('A1', 'E3')
times.append(time.time() - time1)
print(times)

plt.xlabel('Количество вершин')
plt.ylabel('Время')
plt.plot([3, 6, 9, 12, 15], times)
plt.show()
