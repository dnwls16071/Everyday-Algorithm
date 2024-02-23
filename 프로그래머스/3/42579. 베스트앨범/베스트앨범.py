def solution(genres, plays):
    answer = []
    dic = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in dic.keys():
            dic[genre][0].append(i)      # 고유 번호
            dic[genre][1].append(play)   # 재생 횟수
            dic[genre][2] += play        # 장르별 누적 재생 횟수
        else:
            dic[genre] = [[i], [play], play]
    
    # [1]. 속한 노래가 많이 재생된 장르 먼저 수록 -> 장르별 누적 재생 횟수 기준 내림차순
    new_dic = sorted(dic.items(), key=lambda x : -x[1][2])
    
    # [2]. 장르 내에서 많이 재생된 노래 먼저 수록 -> 재생 횟수 기준 내림차순
    # [3]. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래 먼저 수록
    for genre, info in new_dic:
        # x[0] : 고유 번호
        # x[1] : 재생 횟수
        songs = sorted(zip(info[0], info[1]), key=lambda x : (-x[1], x[0]))
        for index, value in songs[:2]:
            answer.append(index)
    return answer 