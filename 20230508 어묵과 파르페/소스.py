import sys
import copy

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
        sub_char_list = sub_char_list[:j]
        while sub_char_list and sub_char_list[-1] == 'F':
            sub_char_list = sub_char_list[:-1]
        return abs(right_parfait_count) + search(sub_char_list)

    else:
        sub_char_list = sub_char_list[i:]
        while sub_char_list and sub_char_list[0] == 'F':
            sub_char_list = sub_char_list[1:]
        return left_parfait_count + search(sub_char_list)


char_list = sys.stdin.readline().strip()
print(search(char_list))