def solution(n):
    
    def n_to_three(n):
        result = []
        while n != 0:
            result.append(n % 3)
            n //= 3
        result = "".join(map(str, result))
        return result
    
    answer = n_to_three(n)
    return int(answer, 3)