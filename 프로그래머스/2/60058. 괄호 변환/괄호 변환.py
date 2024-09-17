def check(u):
    stack = []
    for idx in range(len(u)):
        if u[idx] == '(':
            stack.append('(')
        elif stack and u[idx] == ')':
            stack.pop()
        else:
            return False
    
    if stack:
        return False
    else:
        return True

def solution(p):
    if len(p) == 0:
        return ''

    close = 0
    for idx in range(len(p)):
        if p[idx] == '(':
            close += 1
        else:
            close -= 1
        
        if close == 0:
            u = p[:idx+1]
            v = p[idx+1:]
            if check(u):
                return ''.join([u, solution(v)])
            else:
                result = ['(', solution(v), ')']
                for i in u[1:-1]:
                    if i == '(':
                        result.append(')')
                    else:
                        result.append('(')
                return ''.join(map(str, result))