import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    # r_key : 현재 들어찬 방, r_value : 들어갈 수 있는 가장 가까운 방
    rooms = dict()
    for room in room_number:
        findRoom(room, rooms)
    return list(rooms.keys())
        
        
def findRoom(room, rooms):
    # 신청한 방을 그대로 들어갈 수 있다면?
    if room not in rooms.keys():
        rooms[room] = room + 1
        return room
    # 신청한 방에 들어갈 수 없다면?
    else:
        value = findRoom(rooms[room], rooms)
        rooms[room] = value + 1
        return value