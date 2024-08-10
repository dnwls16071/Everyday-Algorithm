from collections import Counter

def solution(picks, minerals):
    # Test Case #8
    if len(minerals) > sum(picks) * 5:
        minerals = minerals[:sum(picks) * 5]
    
    summary = []
    for i in range(0, len(minerals), 5):
        counter = Counter(minerals[i:i+5]) 
        summary.append([counter["diamond"], counter["iron"], counter["stone"]])
    summary = sorted(summary, key=lambda x : (-x[0], -x[1], -x[2]))
    
    pirodo = 0
    for s in summary:
        # 다이아 곡괭이로 광물을 캐는 경우 피로도 : 1 1 1
        if picks[0] > 0:
            pirodo += s[0] + s[1] + s[2]
            picks[0] -= 1
        # 철 곡괭이로 광물을 캐는 경우 피로도 : 5 1 1
        elif picks[1] > 0:
            pirodo += s[0] * 5 + s[1] + s[2]
            picks[1] -= 1
        # 돌 곡괭이로 광물을 캐는 경우 피로도 : 25 5 1
        elif picks[2] > 0:
            pirodo += s[0] * 25 + s[1] * 5 + s[2]
            picks[2] -= 1
    return pirodo