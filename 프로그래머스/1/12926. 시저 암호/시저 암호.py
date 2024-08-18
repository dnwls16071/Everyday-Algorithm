# a : 97, z : 122, A : 65, Z : 90
def solution(s, n):
    result = []
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in range(len(s)):
        if s[i].isupper():
            idx = (upper_list.find(s[i]) + n) % 26
            result.append(upper_list[idx])
        elif s[i].islower():
            idx = (lower_list.find(s[i]) + n) % 26
            result.append(lower_list[idx])
        else:
            result.append(" ")
    return "".join(result)