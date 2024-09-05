def solution(fees, records):
    
    def to_min(time):
        time = time.split(':')
        return int(time[0]) * 60 + int(time[1])

    parked = dict()         # 차량 번호 : 입/출차
    parked_time = dict()    # 차량 번호 : 주차 시간 
    for record in records:
        time, number, type = record.split(' ')
        
        if type == "IN":
            parked[number] = to_min(time)
        else:
            parked_duration = to_min(time) - parked[number]
            if number in parked_time:
                parked_time[number] += parked_duration
            else:
                parked_time[number] = parked_duration
            del parked[number]
    
    for number, type in parked.items():
        parked_duration = (23 * 60 + 59) - parked[number]
        if number in parked_time:
            parked_time[number] += parked_duration
        else:
            parked_time[number] = parked_duration
    
    parked_time = sorted(parked_time.items())
    
    result = []
    for number, total_time in parked_time:
        if total_time <= fees[0]:
            result.append(fees[1])
        else:
            extra_time = total_time - fees[0]
            extra_fee = (extra_time + fees[2] - 1) // fees[2] * fees[3]
            total_fee = fees[1] + extra_fee
            result.append(total_fee)
    return result
        