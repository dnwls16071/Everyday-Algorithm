def solution(record):
    answer = []
    actions = []
    users = {}  # key : 유저아이디, value : 닉네임
    for r in record:
        r = r.split()
        if r[0] == "Enter" or r[0] == "Change":
            users[r[1]] = r[2]
        actions.append([r[0], r[1]])
    
    for action in actions:
        type, id = action
        if type == "Enter":
            answer.append("{}님이 들어왔습니다.".format(users[id]))
        elif type == "Leave":
            answer.append("{}님이 나갔습니다.".format(users[id]))
    return answer