
from enum import unique


class Potter:
    BOOK_PRICE = 8
    DISCOUNT = {1:1, 2:0.95, 3:0.9, 4:0.8, 5:0.75}
    
    def __init__(self):
        self.books_list = []
        
    def get_price(self, books):
        self.books_list = books
        
        self.set_len = []
        while books:
            unique_set = set(books)
            self.set_len.append(len(unique_set))
            for u in unique_set:
                books.remove(u)
            
        return sum(self.BOOK_PRICE * length * self.DISCOUNT[length] for length in self.set_len)