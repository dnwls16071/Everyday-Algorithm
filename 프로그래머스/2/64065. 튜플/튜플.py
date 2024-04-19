def solution(s):
    s = sorted(s[2:-2].split("},{"), key=lambda x:len(x))
    dic = dict()
    for i in s:
        data = i.split(",")
        for j in data:
            if int(j) not in dic:
                dic[int(j)] = 1
    return list(dic)