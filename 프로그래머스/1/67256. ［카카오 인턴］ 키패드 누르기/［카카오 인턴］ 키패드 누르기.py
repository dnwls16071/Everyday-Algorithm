def solution(numbers, hand):
    phone = {"1" : [0, 0], "2" : [0, 1], "3" : [0, 2],
             "4" : [1, 0], "5" : [1, 1], "6" : [1, 2],
             "7" : [2, 0], "8" : [2, 1], "9" : [2, 2],
             "*" : [3, 0], "0" : [3, 1], "#" : [3, 2]}
    result = []
    cur_left = "*"
    cur_right = "#"
    
    for number in numbers:
        d1 = abs(phone[cur_left][0] - phone[str(number)][0]) + abs(phone[cur_left][1] - phone[str(number)][1])
        d2 = abs(phone[cur_right][0] - phone[str(number)][0]) + abs(phone[cur_right][1] - phone[str(number)][1])
        
        if str(number) in ["1", "4", "7"]:
            result.append("L")
            cur_left = str(number)
        elif str(number) in ["3", "6", "9"]:
            result.append("R")
            cur_right = str(number)
        else:
            if d1 == d2:
                if hand == "left":
                    result.append("L")
                    cur_left = str(number)
                else:
                    result.append("R")
                    cur_right = str(number)
            elif d1 > d2:
                result.append("R")
                cur_right = str(number)
            else:
                result.append("L")
                cur_left = str(number)
    return "".join(result)