from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses and progresses[0] >= 100:
            speeds.popleft()
            progresses.popleft()
            cnt += 1     
        if cnt > 0:
            answer.append(cnt)       
    return answer