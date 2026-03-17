#https://school.programmers.co.kr/learn/courses/30/lessons/42579
#베스트앨범

from collections import defaultdict

def solution(genres, plays):
    genre_counts = defaultdict(int)
    play_counts = {i:play for i, play in enumerate(plays)}
    n = len(genres)
    for i, genre in enumerate(genres):
        genre_counts[genre] += plays[i]
    
    arr = sorted(list(range(n)), key=lambda a: (-genre_counts[genres[a]], -play_counts[a], a))

    #두개씩 거르기
    genre_filter_counts = {genre: 0 for genre in genre_counts.keys()}
    
    res = []
    for i in arr:
        genre = genres[i]
        if genre_filter_counts[genre] == 2:
            continue
        genre_filter_counts[genre] += 1
        res.append(i)
    
    return res 