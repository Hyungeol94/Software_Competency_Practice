#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYgEiwbKy48DFARP&categoryId=AYgEiwbKy48DFARP&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

def calculate(t):
    # Use a breakpoint in the code line below to debug your script.
    len = int(input())
    letters = input().strip()
    if len%2 != 0:
        print(f'#{t} No')
        return
    if letters[:len//2] != letters[len//2:]:
        print(f'#{t} No')
        return
    print(f'#{t} Yes')
    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    calculate(t)
    # ///////////////////////////////////////////////////////////////////////////////////
