from itertools import permutations
import re

def solution(user_id, banned_id):
    answer = set()
    banned = ' '.join(map(str, banned_id)).replace("*", ".")
    """
    fr.d. abc1..
    """
    
    for perm in permutations(user_id, len(banned_id)):
        """동일한 경우
        frodo fradi
        fradi frodo
        """
        string = ' '.join(perm)
        if re.fullmatch(banned, string):
            temp = ' '.join(sorted(perm))
            answer.add(temp)
    return len(answer)