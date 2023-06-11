#https://blog.naver.com/boostcamp_official/223085597916
#코딩테스트 유형2-Q2 풀이

def solution(types):
    answer = []
    string = ''
    for i, t in enumerate(types):
        if t == "BOOL":
            #padding 없음
            if len(string)== 8:
                    answer.append(string)
                    string = ''
            string += '#'
            
        elif t == "SHORT":
            if len(string) %2 != 0:
                string += '.'
            if len(string)== 8:
                answer.append(string)
                string = ''
            string += '##'
            
        elif t == 'FLOAT':
            while (len(string)%4 != 0):
                string += '.'
            if len(string)== 8:
                answer.append(string)
                string = ''
            string += '####'
            
        elif t == 'INT':
            while (len(string)%8 !=0):
                string += '.'
            if len(string)== 8:
                answer.append(string)
                string = ''
            answer.append('########')
            
        elif t == 'LONG':
            while (len(string)%8 !=0):
                string += '.'
            if len(string)== 8:
                answer.append(string)
                string = ''
            answer.append('########')
            answer.append('########')
        if i == len(types)-1 and string != '':
            while (len(string)%8 !=0):
                string += '.'            
            answer.append(string)
            
    if 16<len(answer):
        return "HALT"    
    return ','.join(answer)
                
                
            
            
            
