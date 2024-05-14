def solution(skill, skill_trees):
    skill = list(skill)
    answer = 0
    for s in skill_trees:
        stack = []
        l = list(s)
        for ele in l:
            if ele in skill:
                stack.append(ele)
        if "".join(skill).startswith("".join(stack)):
            answer += 1
    return answer