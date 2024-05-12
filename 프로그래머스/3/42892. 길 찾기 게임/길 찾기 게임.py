import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, info):
        self.x = info[0][0]
        self.y = info[0][1]
        self.idx = (info[1] + 1)
        self.left = None
        self.right = None
    
def insert(node, info):
    if node is None:
        return Node(info)
    
    if info[0][0] < node.x:
        node.left = insert(node.left, info)
    else:
        node.right = insert(node.right, info)
    return node

def maketree(nodeinfo):
    nodes = []
    for idx, node in enumerate(nodeinfo):
        nodes.append((node, idx))
    nodes.sort(key=lambda x : x[0][0])
    nodes.sort(key=lambda x : x[0][1], reverse=True)
    
    root = None
    for node in nodes:
        root = insert(root, node)
    return root

def preorder(root):
    res = []
    def _preorder(node):
        if node:
            res.append(node.idx)
            _preorder(node.left)
            _preorder(node.right)
    _preorder(root)
    return res

def inorder(root):
    res = []
    def _inorder(node):
        if node:
            _inorder(node.left)
            res.append(node.idx)
            _inorder(node.right)
    _inorder(root)
    return res

def postorder(root):
    res = []
    def _postorder(node):
        if node:
            _postorder(node.left)
            _postorder(node.right)
            res.append(node.idx)
    _postorder(root)
    return res

def solution(nodeinfo):
    answer = []
    root = maketree(nodeinfo)
    answer.append(preorder(root))
    answer.append(postorder(root))
    return answer