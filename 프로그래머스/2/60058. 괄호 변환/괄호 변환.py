from collections import defaultdict

def proper(p):
    d = defaultdict(int)
    for i in range(len(p)):
        d[p[i]] += 1
        if d["("] == d[")"]:
            return p[:i+1], p[i+1:]

def check(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True
    
def solution(p):
    if len(p) == 0:
        return ""

    u, v = proper(p)
    string = []
    if check(u):
        return u + solution(v)
    else:
        string.append("(")
        string.append(solution(v))
        string.append(")")
        for i in u[1:len(u)-1]:
            if i == "(":
                string.append(")")
            else:
                string.append("(")
        return "".join(map(str, string))