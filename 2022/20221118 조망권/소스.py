#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh

def compute(i, heights):
    previous_height, next_height, current_height = 0, 0, heights[i]
    if i != 0:
        previous_height = heights[0] if i == 1 else max(heights[i-1], heights[i-2])
    if i != len(heights)-1:
        next_height = heights[-1] if i == len(heights)-2 else max(heights[i+1], heights[i+2])
    competing_height = max(previous_height, next_height)
    return current_height-competing_height if current_height-competing_height >= 0 else 0

def calculate():
    N = int(input())
    heights = list(map(int, input().split()))
    count = 0
    for i, height in enumerate(heights):
        count += compute(i, heights)
    return count

if __name__ == '__main__':
    for T in range(10):
        count = calculate()
        print(f'#{T+1} {count}')

