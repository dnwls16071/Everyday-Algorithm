import sys
sys.setrecursionlimit(10**6)

def solution(numbers):
    prime_set = set()
    numbers = list(map(int, numbers))
    visited = [False] * len(numbers)

    def checking_prime(number):
        if number == 1 or number == 0:
            return False
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                return False
        return True
    
    def backtracking(combination):
        if combination:
            num = int("".join(map(str, combination)))
            if checking_prime(num):
                prime_set.add(num)
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                combination.append(numbers[i])
                backtracking(combination)
                combination.pop()
                visited[i] = False
        
    backtracking([])
    return len(prime_set)