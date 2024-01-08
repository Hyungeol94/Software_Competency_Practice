#https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

def compute():
    building_count = int(input());
    building_list = list(map(int, input().split()));
    #조망권이 확보된 세대 수를 구하기;
    #각 빌딩의 최대 높이는 255

    ##조망권 구하기
    sum = 0;
    for i in range(2, building_count-2):
        building_height = building_list[i];
        previous_height = max(building_list[i-2], building_list[i-1]);
        next_height = max(building_list[i+1], building_list[i+2]);

        compare_height = max(previous_height, next_height);
        if (building_height>compare_height):
            sum += building_height-compare_height;

    return sum;

if __name__ == '__main__':
    for i in range(10):
        answer = compute();
        print("#"+str(i+1)+" "+str(answer));




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
