buy = float(input("Bank buys EUR: "))
#buy = round(buy, 4)
sell = float(input("Bank sells EUR: "))
#sell = round(sell, 4)
spread = sell - buy
print("Spread: ", round(spread, 4))