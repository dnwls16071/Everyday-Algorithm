def solution(s):
    s = sorted(s[2:-2].split("},{"), key=lambda x:len(x))
    result = []
    for i in s:
        data = i.split(",")
        for j in data:
            if int(j) not in result:
                result.append(int(j))
    return result