def solution(numbers, target):
    answer = 0    
    def DFS(idx, total):
        nonlocal answer
        if idx == len(numbers):
            if total == target:
                answer += 1
            else:
                return
        else:
            DFS(idx+1, total+numbers[idx])
            DFS(idx+1, total-numbers[idx])
    DFS(0, 0)
    return answer