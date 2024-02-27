def solution(jobs):
    jobs = sorted(jobs, key=lambda x : x[1])
    start = 0
    answer = 0
    length = len(jobs)
    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += (start - jobs[i][0])
                jobs.pop(i)
                break
            if i == len(jobs) - 1:
                start += 1
    return answer // length