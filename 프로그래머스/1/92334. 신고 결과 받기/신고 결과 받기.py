def solution(id_list, report, k):
    answer = [0] * len(id_list) 
    report = list(set(report))
    reported_dict = {}
    for hist in report:
        a, b = hist.split()
        if b not in reported_dict:
            reported_dict[b] = 1
        else:
            reported_dict[b] += 1
    
    for hist in report:
        a, b = hist.split()
        if reported_dict[b] >= k:
            answer[id_list.index(a)] += 1
    return answer