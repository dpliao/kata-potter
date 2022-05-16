BOOK_PRICE = 8
class Potter:
    
    def __init__(self):
        self.books = []
        
    def get_price(self, book_list):
        self.books = book_list
        return BOOK_PRICE * len(self.books)