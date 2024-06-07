def solution(files):
    answer = []
    for file in files:
        head = []
        number = []
        tail = []
        flag = False
        for i in range(len(file)):
            if file[i].isdigit() and len(number) <= 5:
                number.append(file[i])
                flag = True
            elif not flag:
                head.append(file[i])
            else:
                tail.append(file[i:])
                break
        str_head = "".join(map(str, head))
        str_number = "".join(map(str, number))
        str_tail = "".join(map(str, tail))
        answer.append([str_head, str_number, str_tail])
    # 파일명은 우선 HEAD 부분을 기준으로 사전 순으로 정렬, 이때, 문자열 비교 시 대소문자 구분을 하지 않는다. 
    answer = sorted(answer, key=lambda x : (x[0].lower(), int(x[1])))
    return ["".join(i) for i in answer]