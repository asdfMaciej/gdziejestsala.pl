import models


def BFS(adjacency_lists, start, goal):
    # You can easily optimize this function by 
    #   using a deque instead of list for queue
    assert start != goal 
    explored, queue = [], [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        if node not in explored:
            neighbours = adjacency_lists[node]
             
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return new_path

            explored.append(node)
 
    return None


def get_path(edges: list[models.Edge], start: int, end: int) -> list[int] | None:    
    if start == end:
        raise ValueError("Start and end IDs must not be identical!")

    """
    We should generate empty adjacency lists for classrooms
    So BFS doesn't route a path through the middle of a classroom,
      but still can find a path leading to one
    Right now there is no support in models, so just dropping this comment there
    """
    adjacency_lists = {}
    for edge in edges:
        if edge.from_point_id not in adjacency_lists:
            adjacency_lists[edge.from_point_id] = []
        
        adjacency_lists[edge.from_point_id].append(edge.to_point_id)

    return BFS(adjacency_lists, start, end)