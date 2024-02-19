def solution(nums):
    setNums = list(set(nums))
    if len(setNums) >= len(nums) // 2:
        return len(nums) // 2
    else:
        return len(setNums)