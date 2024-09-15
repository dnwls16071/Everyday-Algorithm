#1. 자물쇠 영역을 확장
#2. 열쇠를 90도 회전한 결과 4번을 자물쇠와 비교

def rotate_right_90_degree(array):
    width = len(array[0])   # 가로
    height = len(array)     # 세로
    
    result = [[0] * width for _ in range(height)]   # 90도 회전한 배열을 저장
    for i in range(height):
        for j in range(width):
            result[j][height - i - 1] = array[i][j]
    return result

def check_func(array):
    # 90도 회전한 배열(열쇠)과 자물쇠가 일치한다면 True, 아니면 False
    length = len(array) // 3
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if array[i][j] != 1:
                return False
    return True

def solution(key, lock):
    N = len(lock)   # 자물쇠
    M = len(key)    # 열쇠
    
    nN = [[0] * (N * 3) for _ in range(N * 3)]  # M이 N보다 항상 작고 기존 N배열을 확장(자물쇠 확장)
    # 확장된 배열에 맞추기
    for i in range(N):
        for j in range(N):
            nN[i + N][j + N] = lock[i][j]
    
    # 90도 회전 4번을 돌려 홈과 맞는 형태를 보이면 True, 하나라도 안 보이면 False
    for _ in range(4):
        key = rotate_right_90_degree(key)
        for i in range(N * 2):
            for j in range(N * 2):
                for y in range(M):
                    for x in range(M):
                        nN[y+i][x+j] += key[y][x]
                if check_func(nN):
                    return True
                for y in range(M):
                    for x in range(M):
                        nN[y+i][x+j] -= key[y][x]
    return False