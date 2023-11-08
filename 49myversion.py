def f(dice):
    n1 = dice.count('1')
    n2 = dice.count('2')
    n3 = dice.count('3')
    n4 = dice.count('4')
    n5 = dice.count('5')
    n6 = dice.count('6')

    #if max(n1,n2,n3,n4,n5,n6) == dice.count('1'):
    #    return '1'
    #if max(n1,n2,n3,n4,n5,n6) == dice.count('2'):
    #    return '2'
    #if max(n1,n2,n3,n4,n5,n6) == dice.count('3'):
    #    return '3'
    #if max(n1,n2,n3,n4,n5,n6) == dice.count('4'):
    #    return '4'
    #if max(n1,n2,n3,n4,n5,n6) == dice.count('5'):
    #    return '5'
    #if max(n1,n2,n3,n4,n5,n6) == dice.count('6'):
    #    return '6'
    
    #pierwsza wersja tak dla wspomnien 

    for i in range (len(dice)):
        if max(n1,n2,n3,n4,n5,n6) == dice.count(str(i)):
            return str(i)

    
    
           
print(f("5233165554211"))
print(f('2133'))