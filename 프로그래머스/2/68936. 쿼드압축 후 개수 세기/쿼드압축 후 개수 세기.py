def solution(arr):
    answer = [0, 0]
    def quad(arr, a, b, l):
        for i in range(a, a+l):
            for j in range(b, b+l):
                if arr[a][b] != arr[i][j]:
                    l //= 2
                    quad(arr, a, b, l)
                    quad(arr, a+l, b, l)
                    quad(arr, a, b+l, l)
                    quad(arr, a+l, b+l, l)
                    return
        answer[arr[a][b]] += 1
    quad(arr, 0, 0, len(arr))
    return answer