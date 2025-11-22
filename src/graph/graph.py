class Graph:
    def __init__(self, vertices: list[int], edges: list[tuple[int, int]]):
        self.vertices = vertices
        self.edges = edges

    def __iter__(self):
        return DFSIterator(self)

class DFSIterator:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited = set()
        self.stack = []
        
        self.adj = {v: [] for v in graph.vertices}
        for u, v in graph.edges:
            if u in self.adj:
                self.adj[u].append(v)
        
        if graph.vertices:
            self.stack.append(graph.vertices[0])

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            vertex = self.stack.pop()
            
            if vertex in self.visited:
                continue
                
            self.visited.add(vertex)
            
            for neighbor in reversed(self.adj.get(vertex, [])):
                if neighbor not in self.visited:
                    self.stack.append(neighbor)
            
            return vertex
        
        raise StopIteration
