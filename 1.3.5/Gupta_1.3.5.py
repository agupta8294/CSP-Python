# Answers

# number 5: The types int and float can be used to represent six million.
# number 6: the second input will produce an error becuase it has no parenthesis for one of the strings
# number 7: h is the seventh to last character
# number 8: slogan [17:21] returns 'best'
# number 9: In[15]: slogan + ' in the whole world!' Out[15]: 'My school is the best in the whole world!'
# number 10a: the word theater has 7 letters so it returns 7
# number 10b: it starts at 0 and is 7-1=6 so it returns the first six letters
# number 11: the letters int he words 'test goo' was in the sentence so it was returned as true

from __future__ import print_function # must be first in file 
import random

# number 12


def how_eligible(essay):
    score = 0
    if '!' in essay:
         score += 1
    if ',' in essay:
         score += 1
    if '?' in essay:
         score += 1
    if '"' in essay:
         score += 1 
    return score
# Assignment Check

#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))
