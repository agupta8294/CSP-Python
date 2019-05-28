# 1-5 N/A
# 6a prediction: true
# 6b prediction: true
# 7. 100<x and 666==y is false
#8 N/A

from __future__ import print_function # use Python 3.0 printing 

def age_limit_output(age):
    '''Step 9a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT) 
    
# 9a. Prediction: for (10), it will be below the age limit ; for (16),  it will be old enough
age_limit_output(10)
age_limit_output(16)
# Discuss and explain the output: age limit is 13, so 10 is less than 13 so it is not allowed, but 16 is greater than 13 so it is allowed
# 10-12 N/A

def report_grade(percent):
    """Step 9b"""
    REPORT_GRADE = 80
    if percent < REPORT_GRADE:
        print( 'A grade of', percent, 'does not indicate mastery. Seek extra practice or help.')
    else:
        print('A grade of', percent, 'indicates mastery. Keep up the good work!')
    print('Minimum needed percent is ', REPORT_GRADE)
    
def letter_in_word(guess, word):
    """Step 11"""
    if guess in word:
        return True
    else:
        return False
        
def hint(color, secret):
    """Step 12"""
    if str(color) in secret:
        print('The color', color, 'IS in the secret sequence of colors.')
    else:
        print('The color', color, 'IS NOT in the secret sequence of colors.')

# conclusion
# 1: The indentation of the if, else, and elif code tells the Python interpreter which block of code belongs to that def, if, or else block. 
# 2: Quotation marks, parenthesis, square and curly brackets
# 3: all of them are in between right and wrong

# Assignment Check!
# 1: I got the result of:
"""10 is below the age limit.
Minimum age is  13
16 is old enough.
 Minimum age is  13
A grade of 79 does not indicate mastery. Seek extra practice or help.
Minimum needed percent is  80
A grade of 85 indicates mastery. Keep up the good work!
Minimum needed percent is  80
True
The color red IS in the secret sequence of colors.
The color green IS NOT in the secret sequence of colors."""
# 1 (con't): Based on the rsuelt, I do believe I have a fully completed assignment.


#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)

