# 자물쇠 크기 : N x N
# 열쇠 크기 : M x M
#1. Lock(자물쇠)을 확장할 필요가 있음(2배)
#2. Key(열쇠)를 90도 회전시켜서 나오는 결과 총 4개를 Lock에 비교하여 일치하면 열리게 된다.

def rotate_right_90_degree(array):
    width = len(array[0])
    height = len(array)
    result = [[0] * width for _ in range(height)]
    
    for h in range(height):
        for w in range(width):
            result[w][height - h - 1] = array[h][w]
    return result

def check(array1):
    length = len(array1) // 3
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if array1[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    
    nn = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            nn[i+n][j+n] = lock[i][j]
    
    for _ in range(4):
        key = rotate_right_90_degree(key)
        
        for i in range(n * 2):
            for j in range(n * 2):
                for y in range(m):
                    for x in range(m):
                        nn[i + y][j + x] += key[y][x]
                if check(nn):
                    return True
                for y in range(m):
                    for x in range(m):
                        nn[i + y][j + x] -= key[y][x]
    return False