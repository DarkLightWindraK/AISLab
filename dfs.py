# dfs.py
def dfs(edges, start, end):
    # Создаём множество всех вершин из рёбер
    vertices = set()
    for u, v in edges:
        vertices.add(u)
        vertices.add(v)

    # Проверка корректности входных вершин
    if start not in vertices:
        raise ValueError(f"Начальная вершина {start} отсутствует в графе")
    if end not in vertices:
        raise ValueError(f"Конечная вершина {end} отсутствует в графе")

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
    stack = [(start, 0)]  # (вершина, длина пути до неё)
    distances = {start: 0}  # Словарь для хранения длин путей

    while stack:
        vertex, dist = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            # Если достигли конечной вершины, возвращаем длину пути
            if vertex == end:
                return visited, dist
            # Добавляем непосещённые соседние вершины в стек
            for neighbor in sorted(graph.get(vertex, []), reverse=True):
                if neighbor not in visited:
                    stack.append((neighbor, dist + 1))
                    distances[neighbor] = dist + 1

    # Если вершина end недостижима, возвращаем путь и -1
    return visited, -1

# Пример использования
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
