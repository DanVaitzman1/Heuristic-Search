import heapq
from search_node import search_node
def create_open_set():
    priorityQueue = []
    dictionary = {}
    return priorityQueue, dictionary

def create_closed_set():
    return {}
def add_to_open(vn, open_set):
    heapq.heappush(open_set[0], vn)
    open_set[1][hash(vn.state)] = vn
def open_not_empty(open_set):
    return len(open_set[1])
def get_best(open_set):
    node = heapq.heappop(open_set[0])
    return node
def add_to_closed(vn, closed_set):
    closed_set[hash(vn.state)] = vn
def duplicate_in_open(vn, open_set):
    hashCode = hash(vn.state)
    if hashCode in open_set[1]:
        if vn.g >= open_set[1][hashCode].g:
            return True
        else:
            open_set[1].pop(hashCode, None)
            return False
    else:
        return False

def duplicate_in_closed(vn, closed_set):
    hashCode = hash(vn.state)
    if hashCode in closed_set:
        if closed_set[hashCode].g <= vn.g:
            return True
        else:
            closed_set[hashCode] = vn
            return False
    return False

def print_path(path):
    for i in range(len(path) - 1):
        print(f"[{path[i].state.get_state_str()}] h:{path[i].h} g:{path[i].g}", end=", ")
    print(f"{path[-1].state.state_str}, h:{path[-1].h} g:{path[-1].g}")

def search(start_state, heuristic, goal_state):
    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)
    while open_not_empty(open_set):
        current = get_best(open_set)
        if current.state.get_state_str() == goal_state:
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path
        add_to_closed(current, closed_set)
        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)
    return None
