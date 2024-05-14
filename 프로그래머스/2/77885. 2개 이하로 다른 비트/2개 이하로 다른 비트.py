def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            bin_number = bin(number)[2:]
            result = "0" + str(bin_number)
            bin_result = result[:result.rindex("0")] + "10" + result[result.rindex("0")+2:]
            answer.append(int(bin_result, 2))
    return answer