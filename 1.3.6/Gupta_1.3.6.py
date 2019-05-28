# Answers

# 4 (1,3,4,694342424269)
# 5 Homework has to have name, date and period number. My teacher wants us to use lowercase words and underscores separating the words
# 6a the output is 'b' because it is the second thing in the tuple
# 6b The output is the same as the original, because it only has three inputs
# 7a b[1] is 10 because it was changed from a to 10
# 7b since b[1] is a again the answer is 10
# 8 prints all values of the list except for the first one
# 9 first reassigns value the 4th value; the second one checks a conditional statemen
# 10a is [a,b,3,4,5]
# 10b is [a,b,3,4,5,6,7]
# 11 error says that int can't be added to a list
# 12 a = 18 because 6*3 is 18

# Conclusion
# 1 a[3] is a string, b[3] can't be changed, c[3] is a value in a list
# 2 using multiple vairable types open up any other oppurtunities and simplifies code alot
# 3 we have learned about functions, strings, tuples, lists, branching and output, and nested branching and input, raw input

# Code

from __future__ import print_function # must be first in file 
import random

def roll_two_dice():
    a = random.randint(1, 6)
    b = random.randint(1, 6) 
    return a + b

# Assignment Check
#1.3.6 Function Test
print(roll_two_dice())