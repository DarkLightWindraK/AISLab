# dfs.py
def dfs(edges, start, end):
    vertices = set()
    for u, v in edges:
        vertices.add(u)
        vertices.add(v)

    if start not in vertices:
        raise ValueError(f"Начальная вершина {start} отсутствует в графе")
    if end not in vertices:
        raise ValueError(f"Конечная вершина {end} отсутствует в графе")

    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    visited = []
    stack = [(start, 0)]
    distances = {start: 0}

    while stack:
        vertex, dist = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            if vertex == end:
                return visited, dist
            for neighbor in sorted(graph.get(vertex, []), reverse=True):
                if neighbor not in visited:
                    stack.append((neighbor, dist + 1))
                    distances[neighbor] = dist + 1

    return visited, -1

if __name__ == "__main__":
    try:
        edges = [(4, 2), (1, 3), (2, 4)]
        start_vertex = 2
        end_vertex = 4
        path, length = dfs(edges, start_vertex, end_vertex)
        print("Путь обхода:", path)
        print("Длина пути от", start_vertex, "до", end_vertex, ":", length)
    except ValueError as e:
        print("Ошибка:", e)
