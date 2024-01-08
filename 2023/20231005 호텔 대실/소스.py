from collections import deque


def minutes(time):
    hours = int(time[:2])
    minutes = int(time[-2:])
    return hours * 60 + minutes


def is_in_range(criteria, target):
    if target[0] < criteria[1]:
        return True
    return False


def checkout_rooms(i, occupied_rooms):
    updated_rooms = []
    for j, [start_time, end_time] in enumerate(occupied_rooms):
        if i != end_time:
            updated_rooms.append(occupied_rooms[j])
    return updated_rooms

def checkin_rooms(i, occupied_rooms, book_time_converted):
    for j, [start_time, end_time] in enumerate(book_time_converted):
        if i == start_time:
            occupied_rooms.append(book_time_converted[j])
    return occupied_rooms


def solution(book_time):
    # 분으로 환산
    book_time_converted = list(map(lambda a:
                                   (minutes(a[0]), minutes(a[1]) + 10),
                                   book_time))

    # 시작시간을 중심으로 정렬하기
    book_time_converted.sort(key=lambda a: a[0])

    # 최소 방의 수 구하기
    book_time_converted = deque(book_time_converted)
    i = 0
    occupied_rooms = []
    room = 1
    while i != minutes("24:00"):
        occupied_rooms = checkout_rooms(i, occupied_rooms) if occupied_rooms else []
        occupied_rooms = checkin_rooms(i, occupied_rooms, book_time_converted)
        room = max(room, len(occupied_rooms)) if occupied_rooms else room
        i += 1

    return room
