def solution(record):
    info = dict()
    actions = []
    commands = []
    for r in record:
        r = r.split(" ")
        if r[0] == "Enter" or r[0] == "Change":
            info[r[1]] = r[2]
        actions.append([r[0], r[1]])
    
    for action in actions:
        if action[0] == "Enter":
            commands.append(f"{info[action[1]]}님이 들어왔습니다.")
        elif action[0] == "Leave":
            commands.append(f"{info[action[1]]}님이 나갔습니다.")
    return [command for command in commands]