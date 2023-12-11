def f(player1,player2):
    suma1 = 0
    suma2 = 0
    highs = ['A','K','Q','J','T']
    player1.split()
    for i in player1:
        if i in highs:
            suma1 += 10
        else:
            suma1 += int(i)
    for i in player2:
        if i in highs:
            suma2 += 10
        else:
            suma2 += int(i)
    if suma1 >= suma2:
        return True
    else:
        return False
    
print(f("AJ972","AQT72"))
print(f("9532","K8"))