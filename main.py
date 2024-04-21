import random
import time

from search import search
from pancake_state import pancake_state
from heuristics import *

if __name__ == '__main__':
    # goal_state = "4,3,2,1"
    # pancake_input = "3,4,1,2"
    # pancake_state = pancake_state(pancake_input)
    # # # print(base_heuristic(pancake_state))
    # start_time = time.time()
    # search_result1 = search(pancake_state, base_heuristic, goal_state)
    # for state in search_result1:
    #     print("g = ",state.g, " h = ",state.h)
    # end_time = time.time()
    #
    goal_state = "9,8,7,6,5,4,3,2,1"
    pancake_input = "3,9,4,7,1,8,5,6,2"
    print("base")
    pancake_state = pancake_state(pancake_input)
    start_time_base = time.time()
    search_result = search(pancake_state, base_heuristic, goal_state)
    end_time_base = time.time()
    print(end_time_base - start_time_base)
    print(search_result)

    print("advanced")
    start_time_advanced = time.time()
    search_result = search(pancake_state, advanced_heuristic, goal_state)
    end_time_advanced = time.time()
    print(end_time_advanced - start_time_advanced)
    print(search_result)



    #
    # numbers = list(range(9, 0, -1))
    # goal_state = ','.join(map(str, numbers))
    # print("goal state = ", goal_state)
    # random.shuffle(numbers)
    # start_string = ','.join(map(str, numbers))
    # print("start state = ", start_string)
    # print("============== base ==============")
    # pancake_state = pancake_state(start_string)
    # start_time_base = time.time()
    # search_result_base = search(pancake_state, base_heuristic, goal_state)
    # end_time_base = time.time()
    # print("Run Time = ",end_time_base - start_time_base)
    # print(search_result_base)
    # print("============== advanced ==============")
    # start_time_advanced = time.time()
    # search_result_advanced = search(pancake_state, advanced_heuristic, goal_state)
    # end_time_advanced = time.time()
    # print("Run Time = ",end_time_advanced - start_time_advanced)
    # print(search_result_advanced)
    # print("============== advanced_heuristic_dan ==============")
    # start_time_advanced_heuristic_dan = time.time()
    # search_result_advanced_heuristic_dan = search(pancake_state, advanced_heuristic_dan, goal_state)
    # end_time_advanced_heuristic_dan = time.time()
    # print("Run Time = ",end_time_advanced_heuristic_dan - start_time_advanced_heuristic_dan)
    # print(search_result_advanced_heuristic_dan)

    #
    # goal_state = "4,3,2,1"
    # pancake_input = "3,4,1,2"
    # print("============== base ==============")
    # pancake_state = pancake_state(pancake_input)
    # start_time_base = time.time()
    # search_result_base = search(pancake_state, base_heuristic, goal_state)
    # end_time_base = time.time()
    # print("Run Time = ",end_time_base - start_time_base)
    # print(search_result_base)
    # print("============== advanced ==============")
    # start_time_advanced = time.time()
    # search_result_advanced = search(pancake_state, advanced_heuristic, goal_state)
    # end_time_advanced = time.time()
    # print("Run Time = ",end_time_advanced - start_time_advanced)
    # print(search_result_advanced)
    # print("============== advanced_heuristic_dan ==============")
    # start_time_advanced_heuristic_dan = time.time()
    # search_result_advanced_heuristic_dan = search(pancake_state, advanced_heuristic_dan, goal_state)
    # end_time_advanced_heuristic_dan = time.time()
    # print("Run Time = ",end_time_advanced_heuristic_dan - start_time_advanced_heuristic_dan)
    # print(search_result_advanced_heuristic_dan)


