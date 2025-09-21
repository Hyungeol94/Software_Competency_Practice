#https://leetcode.com/problems/design-movie-rental-system/?envType=daily-question&envId=2025-09-21
#1912. Design Movie Rental System

from collections import defaultdict, deque
import heapq

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.rented = set()
        self.heap = []
        heapq.heapify(self.heap)
        self.my_queue = deque([])
        self.movie_heap = {}
        self.movie_deque = defaultdict(deque)
        
        for entry in entries:
            shop, movie, price = entry
            if not self.movie_heap.get(movie):
                self.movie_heap[movie] = []
                heapq.heapify(self.movie_heap[movie])
            heapq.heappush(self.heap, (price, shop, movie))
            heapq.heappush(self.movie_heap[movie], (price, shop))
        
        for key, value in self.movie_heap.items():
            heap = value
            while heap:
                curr = heapq.heappop(heap)
                self.movie_deque[key].append(curr)

        while self.heap:
            curr = heapq.heappop(self.heap)
            self.my_queue.append(curr)
        

    def search(self, movie: int) -> List[int]:
        arr = []
        for item in self.movie_deque[movie]:
            price, shop = item
            if (movie, shop) in self.rented:
                continue
            arr.append(shop)
            if len(arr) == 5:
                break
        return arr

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add((movie, shop))

    def drop(self, shop: int, movie: int) -> None:
        self.rented.remove((movie, shop))

    def report(self) -> List[List[int]]:
        arr = []
        for item in self.my_queue:
            price, shop, movie = item
            if (movie, shop) not in self.rented:
                continue
            arr.append([shop, movie])
            if len(arr) == 5:
                break
        return arr
            


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()