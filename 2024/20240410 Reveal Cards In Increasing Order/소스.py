import math
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        '''
        orderedDeck이 있음
        while orderedDeck:
            answer.append(orderedDeck.pop(0))
            if orderedDeck:
                orderedDeck.append(orderedDeck.pop(0))
        
        이걸 반복하면 answer에 순서대로 들어감
        orderedDeck은 어떻게 되어 있을까?
        '''
        
        orderedDeck = deque([])
        answer = sorted(deck)
        while answer:
            if orderedDeck:
                orderedDeck.appendleft(orderedDeck.pop())
            orderedDeck.appendleft(answer.pop())

        return orderedDeck

        

        