def solution(phone_book):
    flag = True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            flag = False
            break
    return flag