import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


tree = []
# 트리 전위 순회 → (루트 왼쪽 오른쪽)
while True:
    try:
        tree.append(int(input()))
    except:
        break

def search(start, end):
    if start > end:
        return
    ridx = end + 1
    for idx in range(start+1, end+1):
        # 각 트리의 루트 노드를 갱신
        if tree[start] < tree[idx]:
            ridx = idx
            break
    search(start+1, ridx-1)    # 왼쪽 서브트리
    search(ridx, end)          # 오른쪽 서브트리
    print(tree[start])          # 루트 노드

search(0, len(tree) - 1)