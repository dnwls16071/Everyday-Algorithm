def solution(arrayA, arrayB):
    answerA = 1; answerB = 1
    sA = arrayA[0]; sB = arrayB[0];
    for i in arrayA[1:]:
        sA = gcd(sA, i)
    
    for i in arrayB[1:]:
        sB = gcd(sB, i)
    
    if div(arrayA, sB):
        answerA = max(answerA, sB)
    
    if div(arrayB, sA):
        answerB = max(answerB, sA)

    if answerA == 1 and answerB == 1:
        return 0
    else:
        return max(answerA, answerB)
    
# 최대공약수 구하기(유클리드 호제법)
def gcd(a, b):
    # a : 작은 수, b : 큰 수
    while b != 0:
        if a > b:
            a, b = b, a
        b = b % a
    return a

# 배열의 모든 원소 중 하나라도 최대공약수에 의해 나뉘면 False
def div(array, gcd):
    for i in array:
        if i % gcd == 0:
            return False
    return True