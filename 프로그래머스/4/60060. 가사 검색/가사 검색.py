class Node:
    def __init__(self, key):
        self.key = key
        self.match = 0  # 여기서 중요한 것은 ?가 글자 하나에 매칭이 되므로 문자열의 길이가 일치 여부보다도 중요
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        curr = self.head
        
        for char in string:
            curr.match += 1
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
        
    def startswith(self, string):
        curr = self.head
        
        for char in string:
            if char == "?":
                break
            if char in curr.children:
                curr = curr.children[char]
            else:
                return 0
        return curr.match    
    
def solution(words, queries):
    answer = []
    tries = {}
    reverse_tries = {}
    
    for word in words:
        size = len(word)
        if size not in tries:
            tries[size] = Trie() # 단어 길이별로 트라이 자료구조를 구축
            reverse_tries[size] = Trie()
        tries[size].insert(word)
        reverse_tries[size].insert(word[::-1])
    
    for query in queries:
        size = len(query)
        if size in tries:
            if query[0] != "?":
                trie = tries[size]
                answer.append(trie.startswith(query))
            else:
                trie = reverse_tries[size]
                answer.append(trie.startswith(query[::-1]))
        else:
            answer.append(0)
    return answer