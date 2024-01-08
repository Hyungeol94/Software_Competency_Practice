import sys
import re


def search(char_list):
    pattern = r'F+'
    parfait_count_list = [len(string) for string in re.split(pattern, char_list)]
    print(sum(parfait_count_list)-max(parfait_count_list))


char_list = sys.stdin.readline().strip()
search(char_list)