def solution(number, k):
    stack = []
    number = list(map(int, number))
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1 
        stack.append(num)
    
    if k > 0:
        return ''.join(map(str, number[:k+1]))
    return ''.join(map(str, stack))