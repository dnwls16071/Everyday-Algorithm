def solution(numbers):
    numbers = list(map(str, numbers))
    numbers  = sorted(numbers, key=lambda x : x*3, reverse=True)
    
    answer = "".join(map(str, numbers))
    if int(answer) == 0:
        return "0"
    else:
        return "".join(map(str, numbers))
    