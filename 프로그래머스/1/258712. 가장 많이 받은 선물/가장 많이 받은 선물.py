# 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.
# 두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면
    # 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.
    # 선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값
    # 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않습니다.
# A는 선물을 준 친구의 이름을 B는 선물을 받은 친구의 이름

from collections import defaultdict

def solution(friends, gifts):
    answer = 0
    giftLevel = defaultdict(int)
    table = [[0] * len(friends) for _ in range(len(friends))]

    # 친구 순서 리스트
    friend_idx = dict()
    for i in range(len(friends)):
        friend_idx[friends[i]] = i
    
    for gift in gifts:
        a, b = gift.split()
        idx1, idx2 = friend_idx[a], friend_idx[b]
        giftLevel[idx1] += 1
        giftLevel[idx2] -= 1
        table[idx1][idx2] += 1
    
    will_getList = [0] * len(friends)
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i == j:
                continue
            if table[i][j] > table[j][i]:
                will_getList[i] += 1
            elif table[i][j] == table[j][i]:
                if giftLevel[i] > giftLevel[j]:
                    will_getList[i] += 1
    answer = max(will_getList)
    return answer