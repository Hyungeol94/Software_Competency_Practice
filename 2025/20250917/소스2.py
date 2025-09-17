#https://school.programmers.co.kr/learn/courses/30/lessons/150367?language=python3#
#표현 가능한 이진트리

def is_convertable(bin_str, is_fillable):
    # 1 이상이기 때문에 0일 일이 없음
    # 반드시 1로 시작, fillable함
    if "1" not in bin_str:
        return True
    
    n = len(bin_str)
    ### 공통로직
    if n == 1:
        return True

    elif n == 2:
        if is_fillable and bin_str.startswith("1"):
            return True 
        return False
    
    elif n == 3:
        if bin_str[1] == "1":
            return True 
        return False
    
    else: #분기처리
        if not is_fillable:
            mid = n // 2
            if n < 7:
                return False

            if bin_str[mid] == "0":
                return False
            
            if is_convertable(bin_str[:mid], False) and is_convertable(bin_str[mid+1:], False):
                return True
            return False
        
        else:
            for i, bit in enumerate(bin_str):
                if bit == "0":
                    continue
                
                left_length = i
                right_length = n-i-1
                
                if not (right_length % 2 == 1):
                    continue
                    
                if left_length > right_length:
                    continue

                if not (is_convertable(bin_str[:i].zfill(right_length), False) and is_convertable(bin_str[i+1:], False)):
                    continue
                    
                return True
            return False
                    

def solution(numbers):
    answer = []

    for num in numbers:
        bin_str = bin(num)[2:]
        answer.append(1 if is_convertable(bin_str, True) else 0)

    return answer