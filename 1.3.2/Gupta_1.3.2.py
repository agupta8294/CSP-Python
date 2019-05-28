def add_tip(total, tip_percent): 
    '''Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip
#hypotenuse test
def answer(a, b):
    return a ** 2.0 + b ** 2.0
def hyp(a, b):
    return answer(a, b) ** 0.5
#average of three numbers test
def mean(x, y, z):
    return (x + y + z)/3.0
#periemeter test
def perimeter(base, height):
    return base * 2.0 + height *2.0



#1.3.2 Function Test
print add_tip(20,0.15)
print add_tip(30,0.15)
print hyp(3,4)
print mean(3,4,7)
print perimeter(3,4)


