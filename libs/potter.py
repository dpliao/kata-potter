class Potter:
    
    def __init__(self):
        self.books = []
        
    def get_price(self, book_list):
        self.books = book_list
        total = 0
        for book in self.books:
            total += 8
        return total