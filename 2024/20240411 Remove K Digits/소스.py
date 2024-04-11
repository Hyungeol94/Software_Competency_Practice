sys.setrecursionlimit(10000)
sys.set_int_max_str_digits(10000)


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #제일 작은 값의 인덱스를 찾아서 그 앞뒤를 다 쳐내기
        #앞을 먼저 쳐내기
        #그다음에 뒤를 쳐내기
        #반복하기
        def remove(num, k):
            minNum = min(num)
            left = num.index(minNum)
            if len(num) == k:
                return ''

            if len(num[:left]) == k:
                return num[left:]

            if len(num[:left]) < k: #최소값의 위치보다 적게 있을 때
                return num[left]+remove(num[left+1:], k-len(num[:left]))

            if len(num[:left]) > k:
                return remove(num[:left], k)+num[left:]

        ans = remove(num, k)
        return str(int(ans)) if ans!='' else "0"


     

                    
            
            
            

            

            

            



                    
                        
            
            
        