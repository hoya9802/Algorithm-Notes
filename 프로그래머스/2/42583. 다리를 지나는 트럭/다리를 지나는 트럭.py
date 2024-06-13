# solve 2
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    time = 0; current_weight = 0
    while truck_weights:
        w = bridge.popleft()
        if w > 0 :
            current_weight -= w
        bridge.append(0)
        time += 1
        upcoming_weight = truck_weights[0]
        if upcoming_weight + current_weight > weight:
            continue
        bridge[-1] = upcoming_weight
        current_weight += upcoming_weight
        truck_weights.pop(0)
    return time + bridge_length