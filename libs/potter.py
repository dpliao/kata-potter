BOOK_PRICE = 8
DISCOUNT = {1:1, 2:0.95, 3:0.9, 4:0.8, 5:0.75}
    
def get_price(books):
    set_len = divide_into_sets(books)
    return sum(get_discount(length) for length in set_len)

def divide_into_sets(books):
    set_len = []
    while books:
        unique_set = set(books)
        set_len.append(len(unique_set))
        for u in unique_set:
            books.remove(u)
    return set_len

def get_discount(length):
    return BOOK_PRICE * length * DISCOUNT[length]