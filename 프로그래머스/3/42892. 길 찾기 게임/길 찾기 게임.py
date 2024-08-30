import sys
sys.setrecursionlimit(10**6)

# 주어진 데이터를 이진 트리로 만들 수 있는가?
# 이진 트리를 만든 후 트리 순회(전위/후위 순회) 코드까지 구현할 수 있는가?

# data : [x축 좌표, y축 좌표]
# 노드(본인, 왼쪽, 오른쪽)
class Node:
    def __init__(self, data):
        self.idx = data[1]      # 인덱스
        self.data = data[0]    # 좌표평면 좌표값
        self.left = None
        self.right = None

def addNode(root, info):
    # 루트 노드보다 값이 크면 오른쪽에 배치
    if root.data[0] < info[0][0]:
        if not root.right:
            root.right = Node(info)
        else:
            addNode(root.right, info)
    # 루트 노드보다 값이 작으면 왼쪽에 배치
    elif root.data[0] > info[0][0]:
        if not root.left:
            root.left = Node(info)
        else:
            addNode(root.left, info)
    # 루트 노드와 값이 같은 경우는 없음

def preorder(root, data):
    if root:
        data.append(root.idx)
        preorder(root.left, data)
        preorder(root.right, data)
    return data
        
        
def postorder(root, data):
    if root:
        postorder(root.left, data)
        postorder(root.right, data)
        data.append(root.idx)
    return data
        
def solution(nodeinfo):
    nodeinfo = [[info, idx+1] for idx, info in enumerate(nodeinfo)]   # 순서(인덱스) 값도 포함
    nodeinfo = sorted(nodeinfo, key=lambda x : -x[0][1])              # y축 좌표 기준 내림차순 정렬
    
    rootNode = Node(nodeinfo[0])    # 루트 노드 설정
    
    for info in nodeinfo[1:]:
        addNode(rootNode, info)

    pre_lst = preorder(rootNode, [])
    post_lst = postorder(rootNode, [])
    return [pre_lst, post_lst]
    
    
