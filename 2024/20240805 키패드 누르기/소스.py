#https://school.programmers.co.kr/learn/courses/30/lessons/67256

def get_distance(departure, destination):
    return abs(departure[0]-destination[0]) + abs(departure[1]-destination[1])

def solution(numbers, hand):
    curr_left = [3, 0]
    curr_right = [3, 2]
    answer = []

    for number in numbers:
        if number in {1,4,7}:
            answer.append('L')
            curr_left = [(number-1)//3, (number-1)%3]    
        elif number in {3,6,9}:
            answer.append('R')
            curr_right = [(number-1)//3, (number-1)%3]
        else:
            curr_position = [(number-1)//3, (number-1)%3] if number != 0 else [3, 1]
            distance_to_left = get_distance(curr_position, curr_left)
            distance_to_right = get_distance(curr_position, curr_right)
            if distance_to_left < distance_to_right:
                answer.append('L')
                curr_left = curr_position
            elif distance_to_left > distance_to_right:
                answer.append('R')
                curr_right = curr_position
            else:
                if hand == "left":
                    answer.append('L')
                    curr_left = curr_position
                else:
                    answer.append('R')
                    curr_right = curr_position
                
    return ''.join(answer)
            
            