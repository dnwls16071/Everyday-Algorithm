def solution(new_id):
    new_id = "".join(map(str, new_id.lower()))
    
    result = []
    for s in new_id:
        if s.isalpha() or s.isdigit() or s in "-_.":
            result.append(s)
    new_id = "".join(map(str, result))
    
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    
    new_id = new_id.strip(".")
    if not new_id:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.strip(".")
    if len(new_id) <= 2:
        new_id = new_id + (new_id[-1] * (3 - len(new_id)))
    
    return new_id
        