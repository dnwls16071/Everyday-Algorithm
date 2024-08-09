def solution(data, col, row_begin, row_end):
    # 테이블의 튜플을 col번째 컬럼의 값을 기준으로 오름차순 정렬
    # 만약 그 값이 동일하면 기본키인 첫 번째 컬럼의 값을 기준으로 내림차순 정렬
    data = sorted(data, key=lambda x : (x[col-1], -x[0]))

    answer = 0
    
    # i번째 행의 튜플에 대해 각 컬럼의 값을 i로 나눈 나머지들의 합으로 정의
    for i in range(row_begin, row_end+1):
        sub_array = data[i-1]
        result = sum(element % i for element in sub_array)
        answer ^= result
    return answer