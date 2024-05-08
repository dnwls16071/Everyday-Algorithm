from collections import defaultdict

def solution(genres, plays):
    """
    노래 수록 기준(장르 별로 2개씩 모아...)
    1. 속한 노래가 많이 재생된 장르 먼저
    2. 장르 내에서 많이 재생된 노래 먼저
    3. 장르 내에서 재생 횟수가 같은 노래 중에서 고유 번호가 낮은 노래를 먼저
    """
    info = defaultdict(lambda: [[], [], 0])
    answer = []
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        info[genre][0].append(idx)      # 고유 번호
        info[genre][1].append(play)     # 해당 고유 번호 장르 재생 횟수
        info[genre][2] += play          # 장르 총 재생 횟수
    info = sorted(info.items(), key=lambda x : -x[1][2])
    
    for g, i in info:
        song = sorted(zip(i[0], i[1]), key=lambda x : (-x[1], x[0]))[:2]
        for s in song:
            answer.append(s[0])
    return answer