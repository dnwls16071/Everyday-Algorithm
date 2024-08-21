def DFS(data, string, cnt):
    if cnt == 6:
        return
    if string != "":
        data.append(string)
    for c in ["A", "E", "I", "O", "U"]:
        DFS(data, "".join(map(str, [string, c])), cnt+1)
    
def solution(word):
    answer = 0
    data = []
    DFS(data, "", 0)
    for i in range(len(data)):
        if data[i] == word:
            return answer + 1
        answer += 1