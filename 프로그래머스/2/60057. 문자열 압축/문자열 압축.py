def solution(s):
    answer = len(s)
    for z in range(1, (len(s) // 2) + 1):
        zip_array = []
        std = s[:z]
        cnt = 1
        for idx in range(z, len(s)+z, z):
            comp = s[idx:idx+z]
            
            if std == comp:
                cnt += 1
            elif std != comp:
                if cnt > 1:
                    zip_array.append(str(cnt) + std)
                else:
                    zip_array.append(std)
                std = comp
                cnt = 1
        joinProc = "".join(map(str, zip_array))
        answer = min(answer, len(joinProc))
    return answer