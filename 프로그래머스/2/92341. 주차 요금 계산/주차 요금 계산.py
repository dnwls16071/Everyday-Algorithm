from collections import defaultdict

def solution(fees, records):
    answer = []
    car_dict = {}
    fee_dict = defaultdict(int)
    for record in records:
        time, car_number, io = record.split(" ")
        time = time.split(":")
        h = int(time[0])
        m = int(time[1])

        
        if io == "IN":
            car_dict[car_number] = [h, m]
        else:
            oh = car_dict[car_number][0]
            om = car_dict[car_number][1]
            pt = (h - oh) * 60 + (m - om)
            fee_dict[car_number] += pt
            del car_dict[car_number]

    for key, value in car_dict.items():
        fee_dict[key] += (23 - value[0]) * 60 + (59 - value[1])
    
    for key, value in fee_dict.items():
        dt, df, ut, uf = fees
        if value <= dt:
            result = df
        else:
            result = df + ((value - dt) // ut + int((value - dt) % ut != 0)) * uf
        answer.append([key, result])
    answer = sorted(answer, key = lambda x : int(x[0]))
    return [i[1] for i in answer]