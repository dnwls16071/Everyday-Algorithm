from itertools import permutations

def check(arr, banned_id):
    for i in range(len(banned_id)):
        if len(arr[i]) != len(banned_id[i]):
            return False
        for a, b in zip(arr[i], banned_id[i]):
            if b == "*":
                continue
            if a != b:
                return False
    return True
        
def solution(user_id, banned_id):
    answer = set()
    for arr in permutations(user_id, len(banned_id)):   # "frodo", "fradi"
        if check(arr, banned_id):
            arr = list(arr)
            arr.sort()
            arr = tuple(arr)
            answer.add(arr)
    return len(answer)