def solution(word):
    answer = 0
    word_list = []
    alphabets = ['A', 'E', 'I', 'O', 'U']
    
    def DFS(cur, cnt):
        if cnt == 5:
            return
        for i in range(5):
            word_list.append(cur + alphabets[i])
            DFS(cur + alphabets[i], cnt + 1)
    DFS("", 0)
    return word_list.index(word) + 1