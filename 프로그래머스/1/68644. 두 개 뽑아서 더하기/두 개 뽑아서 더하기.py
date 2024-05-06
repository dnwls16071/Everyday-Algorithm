def solution(numbers):
    visited = [False] * len(numbers)
    result = set()
    def DFS(numbers, lst):
        if len(lst) == 2:
            result.add(sum(lst))
            return
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                lst.append(numbers[i])
                DFS(numbers, lst)
                visited[i] = False
                lst.pop()
        return result
    result = DFS(numbers, [])
    result = list(result)
    result.sort()
    return result