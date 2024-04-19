def solution(s):
    s = list(s)
    idx = 0
    for i in range(len(s)):
        if s[i] == " ":
            idx = 0
        else:
            if idx % 2 == 0:
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
            idx += 1
    return "".join(map(str, s))