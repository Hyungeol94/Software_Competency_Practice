import sys

def dfs(depth, my_stack, max_depth, char_string):
    if depth == max_depth:
        print(''.join(my_stack))

    else:
        for i in char_string:
            my_stack.append(i)
            dfs(depth+1, my_stack, max_depth, char_string)
            my_stack.pop()

num_char, max_depth = list(map(int, sys.stdin.readline().split()))
char_string = sys.stdin.readline().strip()
char_list = [char for char in char_string]
char_list.sort()
char_string = ''.join(char_list)
my_stack =[]
dfs(0, my_stack, max_depth, char_string)