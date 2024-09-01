def solution(numbers):
    answer = []
    def f(number):
        if number % 2 == 0:
            return number + 1
        else:
            binnum = '0' + bin(number)[2:]
            binnum = binnum[:binnum.rindex('0')] + "10" + binnum[binnum.rindex('0') + 2:]
            return int(binnum, 2)

    for number in numbers:
        answer.append(f(number))
    return answer