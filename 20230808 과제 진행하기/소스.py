#https://school.programmers.co.kr/learn/courses/30/lessons/176962

def converted_time(time):
    hour, minute = map(int, time.split(':'))
    return hour*60+minute

def solution(plans):
    #시작시간별로 정렬하기
    plans.sort(key=lambda a: converted_time(a[1]))
    task_done = []
    current_plan = plans[0]
    next_plan = plans[1]
    saved_task = []
    current_task_name, current_task_start, current_task_playtime = current_plan[0], converted_time(current_plan[1]), int(current_plan[2])
    next_task_name, next_task_start, next_task_playtime = next_plan[0], converted_time(next_plan[1]), int(next_plan[2])
    if current_task_start + current_task_playtime <= next_task_start:
        task_done.append(current_task_name)
    else:
        saved_task.append([current_task_name, current_task_start+current_task_playtime-next_task_start])

    for previous_plan, current_plan, next_plan in list(zip(plans[:-2], plans[1:-1], plans[2:])):
        previous_task_name, previous_task_start, previous_task_playtime = previous_plan[0], converted_time(previous_plan[1]), int(previous_plan[2])
        current_task_name, current_task_start, current_task_playtime = current_plan[0], converted_time(current_plan[1]), int(current_plan[2])
        next_task_name, next_task_start, next_task_playtime = next_plan[0], converted_time(next_plan[1]), int(next_plan[2])
        #이전 것들 중에서 해결할 것 있는지 확인해 보기
        if saved_task and (previous_task_start+previous_task_playtime < current_task_start):
            t = previous_task_start+previous_task_playtime
            while saved_task and t != current_task_start:
                saved_task_name, saved_task_playtime = saved_task[-1][0], saved_task[-1][1]
                saved_task[-1][1] -= 1
                t += 1
                if saved_task[-1][1] == 0:
                    task_done.append(saved_task_name)
                    saved_task.pop()

        #할 일을 하기
        if current_task_start+current_task_playtime <= next_task_start:
            task_done.append(current_task_name)
        else:
            saved_task.append([current_task_name, current_task_start+current_task_playtime-next_task_start])

    #마지막 처리
    previous_plan, current_plan = plans[-2], plans[-1]
    previous_task_name, previous_task_start, previous_task_playtime = previous_plan[0], converted_time(previous_plan[1]), int(previous_plan[2])
    current_task_name, current_task_start, current_task_playtime = current_plan[0], converted_time(current_plan[1]), int(current_plan[2])

    if saved_task and (previous_task_start + previous_task_playtime < current_task_start):
        t = previous_task_start+previous_task_playtime
        while saved_task and t != current_task_start:
            saved_task_name, saved_task_playtime = saved_task[-1][0], saved_task[-1][1]
            saved_task[-1][1] -= 1
            t += 1
            if saved_task[-1][1] == 0:
                task_done.append(saved_task_name)
                saved_task.pop()

    task_done.append(current_task_name)

    while saved_task:
        saved_task_name, saved_task_playtime = saved_task[-1][0], saved_task[-1][1]
        task_done.append(saved_task_name)
        saved_task.pop()

    return task_done


print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))







