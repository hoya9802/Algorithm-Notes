# def solution(keymap, targets):
#     answer = []
#     key_index = {}
#     for key in keymap:
#         for idx, word in enumerate(key):
#             if word not in key_index:
#                 key_index[word] = idx+1
#             else:
#                 key_index[word] = min(key_index[word], idx+1)
#     for target in targets:
#         temp = 0
#         for word in target:
#             if word in key_index:
#                 temp += key_index[word]
#             else:
#                 temp = -1
#                 break
#         answer.append(temp)
#     return answer

def solution(keymap, targets):
    answer = []
    hs = {}
    for k in keymap:
        for i, ch in enumerate(k):
            hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1

    for i, t in enumerate(targets):
        ret = 0
        for ch in t:
            if ch not in hs:
                ret = - 1
                break
            ret += hs[ch]
        answer.append(ret)

    return answer