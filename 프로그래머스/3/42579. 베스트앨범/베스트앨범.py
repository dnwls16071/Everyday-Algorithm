from collections import defaultdict

def solution(genres, plays):
    answer = []
    info = defaultdict(list)
    gens = defaultdict(int)
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        info[genre].append([idx, play])
        gens[genre] += play
    
    gens = sorted(gens.items(), key=lambda x : -x[1])
    
    for (gen, _) in gens:
        for (idx, _) in sorted(info[gen], key=lambda x : -x[1])[:2]: 
            answer.append(idx)
    return answer