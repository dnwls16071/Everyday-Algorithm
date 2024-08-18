def solution(s):
    answer = []
    idx = 0
    for i in s:
        if i == " ":
            answer.append(" ")
            idx = 0
        else:
            if idx % 2 == 0:
                answer.append(i.upper())
            else:
                answer.append(i.lower())
            idx += 1
    return "".join(map(str, answer))