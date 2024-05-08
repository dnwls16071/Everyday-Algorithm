def solution(phone_book):
    phone_book.sort()
    flag = True
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            flag = False
            break
    return flag
