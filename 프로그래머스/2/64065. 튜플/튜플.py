def solution(s):
    s = s[2:-2].split("},{")
    s = sorted(s, key=lambda x : len(x))
    result = []
    for i in s:
        data = i.split(",")
        for j in data:
            if int(j) not in result:
                result.append(int(j))
    return result