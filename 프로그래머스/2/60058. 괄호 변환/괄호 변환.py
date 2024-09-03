def check(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append("(")
        elif stack:
            stack.pop()
        else:
            return False
    return True

def DFS(string):
    if not string:
        return string   #1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
    
    close = 0
    for idx in range(len(string)):
        if string[idx] == "(":
            close += 1
        else:
            close -= 1  
        
        #2. 문자열 w를 두 균형잡힌 괄호 문자열 u, v로 분리한다.
        if close == 0:  
            u = string[:idx+1]  
            v = string[idx+1:]
            #3. 문자열 u가 올바른 괄호 문자열이라면 문자열 v에 대해 1단계부터 다시 수행
            if check(u):
                return ''.join([u, DFS(v)])
            #4. 문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정을 수행
            #4-1. 빈 문자열에 첫 번째 문자로 "("를 붙인다.
            #4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과를 이어 붙인다.
            #4-3. ")"를 붙인다.
            else:
                empty = ["(", DFS(v), ")"]
                #4-4. u의 첫 번째 문자와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
                for t in range(1, idx):
                    if u[t] == "(":
                        empty.append(")")
                    else:
                        empty.append("(")
                return "".join(empty)
                    
def solution(p):
    return DFS(p)
    
    
            