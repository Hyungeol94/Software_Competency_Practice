def solution(d, budget):
    count = 0 
    d.sort()
    for i, item in enumerate(d):
        budget -= item
        count += 1
        if budget < 0:
            count -=1
            budget += item
            break
    return count     