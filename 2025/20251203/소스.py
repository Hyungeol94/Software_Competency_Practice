from itertools import combinations
from collections import defaultdict
from math import gcd

class Solution:
    def getCount(self, values):
        sum_val = sum(values)               # 전체 합 (a + b + c ...)
        sum_sq_val = sum(v*v for v in values) # 제곱의 합 (a^2 + b^2 + c^2 ...)

        # 공식 적용
        return (sum_val * sum_val - sum_sq_val) // 2

    def getFormula(self, points):
        x1, y1 = points[0]
        x2, y2 = points[1]

        if x1 < x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        #기울기
        dy = (y1 - y2)
        dx = (x1 - x2)

        g = gcd(dy, dx)
        a = (dy // g, dx // g)
        
        #y절편
        #y = ax + b
        b = (y1 * dx - x1 * dy) / dx

        return (a, b) #기울기, y절편


    def countTrapezoids(self, points: List[List[int]]) -> int:
        #기울기 그룹
        x_groups = defaultdict(int)
        groups = defaultdict(lambda: defaultdict(int))

        #벡터 그룹도 관리 => 절편 + 거리 조합
        x_vector_groups = defaultdict(lambda : defaultdict(int))
        vector_groups = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        
        for combi in combinations(points, 2):
            x1, y1 = combi[0]
            x2, y2 = combi[1]
            distance = ((x1-x2)**2 + (y1-y2)**2)

            if x1 == x2:
                x_groups[x1] += 1 #동일한 x절편을 가지는 쌍의 수
                x_vector_groups[distance][x1] += 1
            
            else:
                a, b = self.getFormula(combi) 
                groups[a][b] += 1 #기울기 내부에서 절편으로 나누기
                vector_groups[distance][a][b] += 1

        num_trapezoids = 0
        num_trapezoids += self.getCount(x_groups.values())
        
        for group in groups.values(): #동일한 기울기
            num_trapezoids += self.getCount(group.values())
        
        #평행사변형이라면 중복 계산 => 중복 제거 필요 => 어떻게?
        #임의로 뽑은 두 쌍이 평행사변형인 경우를 어떻게 제거 ??
        #평행사변형의 속성 => 마주보는 두 변의 길이가 같음
        
        num_parallelograms = 0

        for distance, x_groups in x_vector_groups.items():
            num_parallelograms += self.getCount(x_groups.values())

        for distance, groups in vector_groups.items(): #동일한 거리
            for group in groups.values(): #동일한 기울기
                num_parallelograms += self.getCount(group.values())

        return num_trapezoids - (num_parallelograms // 2)