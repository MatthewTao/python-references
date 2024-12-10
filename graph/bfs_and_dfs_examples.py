from collections import defaultdict


class Graph:

    def __init__(self):

        # Default dictionary to store graph
        self.graph = defaultdict(list)

        self.bfs_queue = []
        self.bfs_visited = defaultdict(lambda: False)

        self.dfs_visited = set()

    def add_edge(self, point, edge):
        self.graph[point].append(edge)

    def bfs(self, start):
        self.bfs_queue.append(start)
        self.bfs_visited[start] = True

        while self.bfs_queue:
            point = self.bfs_queue.pop(0)
            print(point, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s.
            # If an adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[point]:
                if not self.bfs_visited[i]:
                    self.bfs_queue.append(i)
                    self.bfs_visited[i] = True

    def dfs(self, node):
        if node not in self.dfs_visited:
            print(node, end=" ")
            self.dfs_visited.add(node)
            for neighbour in self.graph[node]:
                self.dfs(neighbour)


# Driver code
if __name__ == '__main__':
    # Create a graph
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 4)
    g.add_edge(1, 5)
    g.add_edge(1, 6)
    g.add_edge(2, 7)
    g.add_edge(2, 8)
    g.add_edge(2, 9)
    g.add_edge(3, 10)
    g.add_edge(3, 11)
    g.add_edge(3, 12)

    print("Breadth First Traversal (starting from vertex 2)")
    g.bfs(0)

    print("\nDepth First Search")
    g.dfs(0)
