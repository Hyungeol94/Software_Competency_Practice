
#https://leetcode.com/problems/design-a-food-rating-system/?envType=daily-question&envId=2025-09-17
#2353. Design a Food Rating System

import heapq

class TrieNode:
    def __init__(self, c):
        self.letter = c
        self.children = {}
        self.is_word = False
    
    def find(self, word):
        curr = self
        for c in word:
            if not curr.children.get(c):
                return None
            curr = curr.children[c]
        
        if curr.is_word:
            return curr
    
    def insert(self, word, rating):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.is_word = True
        curr.rating = rating

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        #각 cuisine마다 trie로 관리
        self.cuisine_dict = {}
        self.cuisine_heap = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            if cuisine not in self.cuisine_dict:
                self.cuisine_dict[cuisine] = TrieNode("")
                self.cuisine_heap[cuisine] = []
                heapq.heapify(self.cuisine_heap[cuisine])

            cuisine_trie = self.cuisine_dict[cuisine]
            cuisine_trie.insert(food, rating)
            cuisine_heap = self.cuisine_heap[cuisine]
            heapq.heappush(cuisine_heap, (-rating, food))


    def changeRating(self, food: str, newRating: int) -> None:
        for cuisine, cuisine_trie in self.cuisine_dict.items():
            res = cuisine_trie.find(food)
            if res:
                res.rating = newRating
                cuisine_heap = self.cuisine_heap[cuisine]
                heapq.heappush(cuisine_heap, (-newRating, food))
                break

    def highestRated(self, cuisine: str) -> str:
        trie = self.cuisine_dict[cuisine]
        heap = self.cuisine_heap[cuisine]
        while heap:
            rating, food = heap[0]
            if not trie.find(food).rating == -rating:
                heapq.heappop(heap)
                continue
            return food

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)