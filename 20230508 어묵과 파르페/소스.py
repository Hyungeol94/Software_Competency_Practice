import sys
import copy
from collections import deque

def search(char_list):
    if 'F' not in char_list:
        return 0
    # 왼쪽에서부터 세기
    left_parfait_count = 0
    i = 0
    while char_list[i] != 'F':
        i += 1
        left_parfait_count += 1

    # 오른쪽에서부터 세기
    right_parfait_count = 0
    j = -1
    while char_list[j] != 'F':
        j -= 1
        right_parfait_count += 1

    sub_char_list = copy.copy(char_list)
    if left_parfait_count > abs(right_parfait_count):
        while sub_char_list and sub_char_list[-1] == 'P':
            sub_char_list.pop()
        while sub_char_list and sub_char_list[-1] == 'F':
            sub_char_list.pop()
        return abs(right_parfait_count) + search(sub_char_list)

    elif left_parfait_count < abs(right_parfait_count):
        while sub_char_list and sub_char_list[0] == 'P':
            sub_char_list.popleft()
        while sub_char_list and sub_char_list[0] == 'F':
            sub_char_list.popleft()
        return left_parfait_count + search(sub_char_list)

    else:
        second_substring = copy.copy(char_list)
        while sub_char_list and sub_char_list[-1] == 'P':
            sub_char_list.pop()
        while sub_char_list and sub_char_list[-1] == 'F':
            sub_char_list.pop()
        while sub_char_list and second_substring[0] == 'P':
            second_substring.popleft()
        while sub_char_list and second_substring[0] == 'F':
            second_substring.popleft()
        return min(left_parfait_count + search(second_substring), abs(right_parfait_count) + search(sub_char_list))

char_list = deque(sys.stdin.readline().strip())
print(search(char_list))