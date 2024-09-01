def solution(skill, skill_trees):
    answer = 0
    for string in skill_trees:          
        stack = list(skill)[::-1]
        for char in string:
            if char in skill and char != stack.pop(): 
                break
        else:
            answer += 1    
    return answer