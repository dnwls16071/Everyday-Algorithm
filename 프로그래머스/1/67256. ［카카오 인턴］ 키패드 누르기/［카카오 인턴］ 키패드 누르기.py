def solution(numbers, hand):
    # 키패드 위치 딕셔너리 저장
    keypad = {1 : (0, 0), 2 : (0, 1), 3 : (0, 2),
             4 : (1, 0), 5 : (1, 1), 6 : (1, 2),
             7 : (2, 0), 8 : (2, 1), 9 : (2, 2),
             "*" : (3, 0), 0 : (3, 1), "#" : (3, 2)}

    # 왼손 원래 위치 + 오른손 원래 위치
    left_pos = keypad["*"]
    right_pos = keypad["#"]
    
    # 번호 누른 손가락이 어느 손인지 저장하는 배열
    answer = []

    for number in numbers:
        if number in (1, 4, 7):
            left_pos = keypad[number]
            answer.append("L")
        elif number in (3, 6, 9):
            right_pos = keypad[number]
            answer.append("R")
        else:
            ld = abs(keypad[number][0] - left_pos[0]) + abs(keypad[number][1] - left_pos[1])
            rd = abs(keypad[number][0] - right_pos[0]) + abs(keypad[number][1] - right_pos[1])
            if ld > rd:
                right_pos = keypad[number]
                answer.append("R")
            elif ld < rd:
                left_pos = keypad[number]
                answer.append("L")
            else:
                if hand == "left":
                    left_pos = keypad[number]
                    answer.append("L")
                else:
                    right_pos = keypad[number]
                    answer.append("R")
    return "".join(answer)