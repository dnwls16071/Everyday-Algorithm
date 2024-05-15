def solution(numbers, target):
    ct = 0
    def DFS(idx, result):
        nonlocal ct
        if idx == len(numbers):
            if result == target:
                ct += 1
            else:
                return
        else:
            DFS(idx+1, result+numbers[idx])
            DFS(idx+1, result-numbers[idx])
    DFS(0, 0)
    return ct