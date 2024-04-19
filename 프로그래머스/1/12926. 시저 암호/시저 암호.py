def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].islower():
            s[i] = chr((ord(s[i]) + n - ord('a')) % 26 + ord('a'))
        elif s[i].isupper():
            s[i] = chr((ord(s[i]) + n - ord('A')) % 26 + ord('A'))
        else:
            s[i] = " "
    return "".join(map(str, s))        