card_number = '1234567890123456'

def f(card_number):

    card_number = card_number[:2] + '*' * 10 + card_number[12:]
    return card_number

print(f(card_number))