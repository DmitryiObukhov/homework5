def bfs_shortest_route(subway, start_station, end_station):
    if start_station not in subway or end_station not in subway:
        return None
    queue = []
    visited = set()
    queue.append((start_station, [start_station]))
    while queue:
        current_station, route = queue.pop(0)
        if current_station == end_station:
            return route
        visited.add(current_station)
        for neighbor in subway[current_station]:
            if neighbor not in visited:
                queue.append((neighbor, route + [neighbor]))
    return None


subway_system = {
    'Station A': {'Station B'},
    'Station B': {'Station A', 'Station C', 'Station D'},
    'Station C': {'Station B', 'Station D', 'Station E'},
    'Station D': {'Station B', 'Station C', 'Station E', 'Station F'},
    'Station E': {'Station C', 'Station D', 'Station F'},
    'Station F': {'Station D', 'Station E'}
}

start = 'Station D'
end = 'Station A'
route = bfs_shortest_route(subway_system, start, end)
if route:
    print(f"Shortest way from {start} to {end}: {route}")
else:
    print(f"Route from {start} to {end} not founded.")
