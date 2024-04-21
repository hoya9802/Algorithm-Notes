def solution(bridge_length, weight, truck_weights):
    time = 0; current_weight = 0
    bridge = [0] * bridge_length
    while truck_weights:
        time += 1
        if bridge[0] != 0:
            current_weight -= bridge[0]
        bridge.pop(0); bridge.append(0)
        incoming = truck_weights[0]
        if current_weight + incoming <= weight:
            bridge[-1] = truck_weights.pop(0)
            current_weight += incoming
            
    return time + bridge_length