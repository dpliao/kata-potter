from typing import Counter

BOOK_PRICE = 8
DISCOUNT = {1:1, 2:0.95, 3:0.9, 4:0.8, 5:0.75}
    
def get_price(books):
    set_len = divide_into_sets(books)
    best_sets = replace_sets(set_len)
    return get_discount(best_sets)

def divide_into_sets(books):
    set_len = []
    while books:
        unique_set = set(books)
        set_len.append(len(unique_set))
        for u in unique_set:
            books.remove(u)
    return set_len

def replace_sets(sets):
    lengths = Counter(sets)
    while lengths[3] > 0 and lengths[5] > 0:
        lengths[3] -= 1
        lengths[5] -= 1
        lengths[4] += 2
    return lengths.elements()

def get_discount(sets):
    return sum(BOOK_PRICE * length * DISCOUNT[length] for length in sets)