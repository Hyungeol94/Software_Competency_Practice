#https://school.programmers.co.kr/learn/courses/30/lessons/155651
from collections import deque

def minutes(time):
    hours = int(time[:2])
    minutes = int(time[-2:])
    return hours*60+minutes


def is_in_range(criteria, target):
    if target[0]<criteria[1]:
        return True
    return False


def solution(book_time):
    #분으로 환산
    book_time_converted = list(map(lambda a:
        (minutes(a[0]), minutes(a[1])+10),
        book_time))
    
    #마침시간을 중심으로 정렬하기
    book_time_converted.sort(key = lambda a: a[1])

    
    #최소 방의 수 구하기
    book_time_converted = deque(book_time_converted)
    room = 1
    while book_time_converted:
        criteria = book_time_converted.popleft()
        i = 1
        while book_time_converted:
            target = book_time_converted[0]
            if is_in_range(criteria, target):
                i += 1
                book_time_converted.popleft()
            else:
                break
        room = max(room, i)
    return room