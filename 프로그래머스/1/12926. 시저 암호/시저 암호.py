def solution(s, n):
    s = list(s)
    result = []
    for i in s:
        if i == " ":
            result.append(" ")
        if 65 <= ord(i) <= 90:
            if ord(i) + n > 90:
                result.append(chr(ord(i) + n - 26))
            else:
                result.append(chr(ord(i) + n))
        elif 97 <= ord(i) <= 122:
            if ord(i) + n > 122:
                result.append(chr(ord(i) + n - 26))
            else:
                result.append(chr(ord(i) + n))
    return "".join(map(str, result))        