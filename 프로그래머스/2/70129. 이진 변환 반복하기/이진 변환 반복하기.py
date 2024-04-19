def solution(s):
    val1, val2 = convert(s)
    return [val1, val2]


def convert(n):
    zero_cnt = 0
    conv_cnt = 0
    while len(n) != 1:
        result = ""
        for i in n:
            if int(i) == 0:
                zero_cnt += 1
            else:
                result += "1"
        len_res = len(result)
        answer = []
        while len_res != 0:
            answer.append(len_res % 2)
            len_res //= 2
        answer = answer[::-1]
        n = answer
        conv_cnt += 1
    return [conv_cnt, zero_cnt]