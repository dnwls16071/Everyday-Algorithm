def solution(s):
    result = list()
    s = s[2:len(s)-2].split("},{")
    s = sorted(s, key=lambda x : len(x))
    for t in s:
        t = t.split(",")
        for i in t:
            if int(i) not in result:
                result.append(int(i))
    return result