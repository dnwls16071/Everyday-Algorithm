def solution(triangle):
    # 모서리 부분
    for i in range(len(triangle) - 1):
        triangle[i+1][0] += triangle[i][0]
        triangle[i+1][-1] += triangle[i][-1]
    
    # 모서리 제외한 가운데 부분
    for i in range(2, len(triangle)):
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] = max(triangle[i][j] + triangle[i-1][j-1], triangle[i][j] + triangle[i-1][j])
    return max(triangle[-1])