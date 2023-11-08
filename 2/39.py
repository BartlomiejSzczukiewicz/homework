price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))
discount = discount/100
priceTEMP = price * discount
price = price - priceTEMP
print("Price with discount: ",price)
print("Reduction: ",priceTEMP)