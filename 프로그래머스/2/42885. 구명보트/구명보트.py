def solution(people, limit):
    people.sort()
    start, end = 0, len(people) - 1
    boat = 0
    while start < end:
        if people[start] + people[end] <= limit:
            start += 1
            boat += 1
        end -= 1
    return len(people) - boat