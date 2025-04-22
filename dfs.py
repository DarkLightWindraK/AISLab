# dfs.py
def dfs(edges, start):
    # Создаём словарь смежности
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  # Для неориентированного графа

    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            # Добавляем непосещённые соседние вершины в стек
            for neighbor in sorted(graph.get(vertex, []), reverse=True):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited

# Пример использования
if __name__ == "__main__":
    edges = [(4, 2), (1, 3), (2, 4)]
    start_vertex = 1
    result = dfs(edges, start_vertex)
    print("Путь обхода:", result)
