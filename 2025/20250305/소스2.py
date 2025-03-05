#https://school.programmers.co.kr/learn/courses/30/lessons/258707
#n + 1 카드게임

from itertools import combinations

def solution(coin, cards):
    stack_mask = 0 
    n = len(cards)
    i = n // 3 
    
    reserved_cards = []
    available_cards = cards[:i]
    
    round = 0
    while i <= n:
        round += 1
        reserved_cards += cards[i:min(i+2, n)]
        is_found = False
        for combi in combinations(available_cards, 2):
            if sum(combi) == n+1:
                available_cards.pop(available_cards.index(combi[0]))
                available_cards.pop(available_cards.index(combi[1]))
                is_found = True
                break
        if is_found:
            i += 2
            continue
        
        if not 1 <= coin:
            break
            
        for card in available_cards:
            if n+1-card in reserved_cards:
                available_cards.pop(available_cards.index(card))
                reserved_cards.pop(reserved_cards.index(n+1-card))
                coin -= 1
                is_found = True
                break
        
        if is_found:
            i += 2
            continue
        
        if not 2 <= coin:
            break
        
        for combi in combinations(reserved_cards, 2):
            if sum(combi) == n+1:
                reserved_cards.pop(reserved_cards.index(combi[0]))
                reserved_cards.pop(reserved_cards.index(combi[1]))
                coin -= 2
                is_found = True
                break
        
        if is_found:
            i+=2
            continue
            
        else:
            break
    
    return round