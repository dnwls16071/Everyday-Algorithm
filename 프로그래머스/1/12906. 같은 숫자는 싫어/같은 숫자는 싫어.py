### 집합(Set)으로 처리하면 테스트케이스 1번 실패
### 마지막 숫자로 비교해서 같은 숫자가 연속적으로 나타나지 않도록 하는 것이 포인트

def solution(arr):
    stack = [arr[0]]
    for i in arr[1:]:
        if stack[-1] != i:
            stack.append(i)
    return stack