def f():
    cardnumber = input("cardnumber: ")  # Read the card number as a string
    cardnumber = cardnumber[:4] + '*' * (len(cardnumber) - 8) + cardnumber[-4:]  # Replace characters from index 4 to len(cardnumber)-5 with asterisks
    print(cardnumber)

f()
