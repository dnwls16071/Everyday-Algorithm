def solution(name):
    answer = 0
    size = len(name)
    min_move = size - 1
    
    for idx, value in enumerate(name):
        # 알파벳을 맞추기 위해 최소로 조작해야하는 횟수
        answer += min(ord(value) - ord('A'), ord('Z') - ord(value) + 1)
        
        # 조이스틱을 왼쪽으로 조작할지 오른쪽으로 조작할지
        next_idx = idx + 1
        while next_idx < size and name[next_idx] == 'A':
            next_idx += 1
        
        # 최소로 움직이는 횟수를 반환
        # 연속된 A를 따라서 오른쪽으로 갈 때
        # 연속된 A를 따라가지 않고 왼쪽으로 갈 때
        min_move = min(min_move, idx + size - next_idx + min(idx, size - next_idx))
    answer += min_move
    return answer