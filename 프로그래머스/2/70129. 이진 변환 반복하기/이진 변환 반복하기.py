def solution(s):
    change, zero = 0, 0
    while s != "1":
        num = s.count("1")
        zero += s.count("0")
        change += 1
        s = bin(num)[2:]
    return [change, zero]