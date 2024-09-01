from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for string in skill_trees:          
        string_list = deque(skill[:])  
        for char in string:            
            if char in skill and char != string_list.popleft(): 
                break
        else:
            answer += 1    
    return answer