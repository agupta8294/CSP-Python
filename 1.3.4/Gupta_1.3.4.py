# 8

from __future__ import print_function # must be first in file 
import random

def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = float(raw_input('Guess: '))
    if guess < secret:
        print('Too low - my number is ', secret, '.', sep='')
    elif guess > secret:
        print('Too high - my number is ', secret, '.', sep='')
    else:
        print('Right on! I was number ', secret, end='!\n')

# 8a. it works because it puts the number (n) infront of the exclamation mark


def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
            
# number 1a it got the reply from line 17
# number 1b i. orange ; ii. apple ; iii. potato ; iv. hot dog
# number 1c because bananas are listed as fruit and starchy, so line 20 will...
# ...not happen because bananas are starchy and fruit so it cancels out

# 2

def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    if food_id('apple') != 'NOT Citrus, Fruit':
        works = 'apple bug in food_id()'
    if food_id('potato') != 'Starchy, NOT Fruit':
        works = 'potato bug in food_id()'

    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

# 3

def f(n):
    if int(n) == n:
        if n % 3 == 0 and n % 2 == 0:
            return 'This number is a multiple of six'
        elif n % 3 == 0:
            return 'This number is even'
        elif n % 2==0:
            return 'This number is even'
        else:
            return 'The number is odd'
    else:
        return 'The number is not an integer'

# 4. works or test
# 5

def f_test():
    ''' Unit test for f returns True if good,
     returns False and prints error if not 
    good
    '''
    works = True
    if f(6) != 'This number is a multiple of six':
        works = '6 bug in f()'
    if f(12) != 'This number is a multiple of six':
        works = '12 bug in f()'
    if f(2) != 'This number is even':
        works = '2 bug in f()'
    if f(0) != 'This number is a multiple of six':
        works = '0 bug in f()'
    if f(1) != 'This number is odd':
        works = '1 bug in f()'
    if f(0.1) != 'The number is not an integer':
        works = '0.1 bug in f()'
    
# Question 6 is skipped on the worksheet

# 7. Conatenation is to add strings together and numeric addition is to add ints or floats

# 9

def quiz_decimal(low,high):
	number = input("Tell a number that is between 4 and 4.1 =")
	if(number<low):
		print("No,",number,"is less than 4")
	else:
		if(number>high):
			print("No,",number,"is greater than 4.1")
		else:
			print("Good! 4 < ",number,"< 4.1")


# conclusion
# 1. Both test for the effectiveness of a block of code
# 2.Maybe half of them.
# 3. A test suite tests code; programmers might code them before because they...
# ...need to make sure it all works before.
# 4. Yes

def a(n):
    if int(n) % 6 == 0:
        return '%s is a multiple of six' %(n)
    else:
        return '%s is not a multiple of six' %(n)

def b(n):    
    if n % 2==0:
        return '%s is even' %(n)
    else:
        return '%s is odd' %(n)
def c(n):
    if int(n) == n:
        return '%s is an integer' %(n)
    else:
        return '%s is not an integer' %(n)

# Challenge 
def f_challenge(n):
    print (a(n))
    print (b(n))
    print (c(n))

#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)
