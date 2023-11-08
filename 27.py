def f(card_number):
    masked = card_number[:2] + '*'*10 + card_number[12:]
    return masked
print(f("5290312400019022"))