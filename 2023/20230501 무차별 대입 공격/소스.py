import sys
import itertools

num_char, max_depth = list(map(int, sys.stdin.readline().split()))
char_string = sys.stdin.readline().strip()
char_list = [char for char in char_string]
char_list.sort()
char_string = ''.join(char_list)
#print(char_list)
for x in itertools.product(char_list, repeat=max_depth):
    print(''.join(list(x)))
