# my solution
def solution(data, ext, val_ext, sort_by):
    column_index = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    data = sorted([x for x in data if x[column_index.get(ext)] <= val_ext], key=lambda x : x[column_index.get(sort_by)])
    
    return data