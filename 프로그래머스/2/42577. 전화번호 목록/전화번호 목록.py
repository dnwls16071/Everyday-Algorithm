# phone_book의 길이는 최대 1,000,000이하로 시간 제한이 1초라는 가정 하에 2중 for문을 돌리게 된다면 시간초과 발생
# 정렬 후 맨 앞의 번호가 다른 번호의 접두어가 되는 것만을 고려하는 것이 아닌...
# 다른 번호 역시 또 다른 번호의 접두어가 될 수 있기에 for문으로 순회

def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
    return answer