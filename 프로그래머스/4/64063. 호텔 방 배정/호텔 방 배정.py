import sys
sys.setrecursionlimit(10000)

def solution(k, room_number):
    # 현재 방 배정 상태 딕셔너리
    rooms = dict()
    for num in room_number:
        empty = find_emptyrooms(num, rooms)
    return list(rooms.keys())

def find_emptyrooms(chk, rooms):
    if chk not in rooms.keys():
        rooms[chk] = chk + 1    # chk배정, chk+1을 다음 방에 배정
        return chk
    empty = find_emptyrooms(rooms[chk], rooms)
    rooms[chk] = empty + 1
    return empty