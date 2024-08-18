def solution(s):
    result = dict()
    s = s[2:len(s)-2].split("},{")
    s = sorted(s, key=lambda x : len(x))
    for t in s:
        t = t.split(",")
        for i in t:
            if int(i) not in result:
                result[int(i)] = 1
    return list(result)