def solution(keymap, targets):
    answer = []
    key_index = {}
    for key in keymap:
        for idx, word in enumerate(key):
            if word not in key_index:
                key_index[word] = idx+1
            else:
                key_index[word] = min(key_index[word], idx+1)
    for target in targets:
        temp = 0
        for word in target:
            if word in key_index:
                temp += key_index[word]
            else:
                temp = 0
                break
        if temp == 0:
            answer.append(-1)
        else:
            answer.append(temp)
    return answer

# def solution(keymap, targets):
#     keytable = {}
#     for keys in keymap:
#         for i, key in enumerate(keys):
#             if key not in keytable:
#                 keytable[key] = i + 1
#             else:
#                 keytable[key] = min(keytable[key], i + 1)

#     result = []
#     for target in targets:
#         clicked = 0
#         for key in target:
#             if key not in keytable:
#                 clicked = -1
#                 break
#             clicked += keytable[key]
#         result.append(clicked)

#     return result