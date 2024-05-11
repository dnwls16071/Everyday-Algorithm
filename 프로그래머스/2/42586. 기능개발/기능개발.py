from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    """
    작업의 개수가 존재할 때까지
    """
    while progresses:
        """
        cnt : 배포 작업의 개수
        뒤의 기능이 개발이 다 되었다 하더라도 맨 앞의 기능부터 완료가 되어야 배포가 가능하다는 점을 인지
        """
        cnt = 0
        while progresses and progresses[0] >= 100:
            cnt += 1
            pro = progresses.popleft()
            sep = speeds.popleft()
        """
        작업 속도를 반영해서 현재 진행률을 갱신
        """
        progresses = deque([pro + sep for pro, sep in zip(progresses, speeds)])
        """
        배포할 작업물이 존재한다면 모두 배포
        """
        if cnt > 0:
            answer.append(cnt)
    return answer