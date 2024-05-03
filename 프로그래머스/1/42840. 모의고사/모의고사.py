def solution(answers):
    MAX = -1
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]        
    answer = []
    result = [0] * 3
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            result[0] += 1
        
        if answers[i] == second[i % len(second)]:
            result[1] += 1
        
        if answers[i] == third[i % len(third)]:
            result[2] += 1
            
    for i in result:
        if i > MAX:
            MAX = i
            
    for idx, val in enumerate(result):
        answer.append([idx, val]) 
    answer = sorted(answer, key=lambda x : (-x[1], x[0]))
    
    ans = []
    for idx, val in answer:
        if val == MAX:
            ans.append(idx+1)
    return ans