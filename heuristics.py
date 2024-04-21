def base_heuristic(_pancake_state):
    length = len(_pancake_state.get_state_list())
    heuristic = 0
    pancake_not_in_place = False
    if _pancake_state.get_state_list()[0] != length:
        return sum(_pancake_state.get_state_list())
    for pancake in _pancake_state.get_state_list():
        if pancake_not_in_place:
            heuristic += pancake
        elif pancake != length:
            pancake_not_in_place = True
            heuristic += pancake
        length -= 1
    return heuristic

def advanced_heuristic(_pancake_state):
    state_list = _pancake_state.get_state_list()
    length = len(state_list)
    heuristic = 0 if state_list[0] == length else sum(state_list)
    last_pancake_in_place = -1
    for i in range(1,length):
        curr_pancake = state_list[i-1]
        prev_pancake = state_list[i]
        if curr_pancake != length - i:
            last_pancake_in_place = prev_pancake
            break
    for i in range(1,length):
        curr_pancake = state_list[i-1]
        next_pancake = state_list[i]
        if (next_pancake == curr_pancake and last_pancake_in_place != curr_pancake + 1) or abs(
                curr_pancake - next_pancake) > 1:
            heuristic += sum(range(curr_pancake - 1, 0, -1))
    return heuristic
