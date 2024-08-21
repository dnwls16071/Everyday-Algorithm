from collections import defaultdict

def solution(answers):
    score = defaultdict(int)
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if a[i % len(a)] == answers[i]:
            score[1] += 1
        if b[i % len(b)] == answers[i]:
            score[2] += 1
        if c[i % len(c)] == answers[i]:
            score[3] += 1
    
    answer = []
    max_hit = max(score.values())
    score = sorted(score.items(), key=lambda x : (x[1], x[0]))
    for key, value in score:
        if value == max_hit:
            answer.append(key)
    return answer
            