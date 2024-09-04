def solution(people, limit):
    left = 0; right = len(people) - 1
    people.sort()
    answer = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    return answer