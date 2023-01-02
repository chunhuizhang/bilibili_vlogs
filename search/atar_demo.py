
import astar


class GraphAStar(astar.AStar):
    def __init__(self, nodes):
        self.nodes = nodes

    def neighbors(self, node):
        for n, d in self.nodes[node]:
            yield n

    # g function
    def distance_between(self, n1, n2):
        for n, d in self.nodes[n1]:
            if n == n2:
                return d

    # h function
    def heuristic_cost_estimate(self, current, goal):
        return 1


if __name__ == '__main__':
    nodes = {'A': [('B', 100), ('C', 20)],
             'C': [('D', 20)],
             'D': [('B', 20)]}
    # A -> B

    graph_solver = GraphAStar(nodes)
    print(list(graph_solver.astar('A', 'B')))
    print(list(graph_solver.astar('A', 'C')))
