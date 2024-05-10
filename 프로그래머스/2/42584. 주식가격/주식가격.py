def solution(prices):
    stack = [0] # 시점을 저장하는 수단
    answer = [i for i in range(len(prices)-1, -1, -1)]
    for i in range(1, len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            seq = stack.pop()
            answer[seq] = i - seq
        stack.append(i)
    return answer