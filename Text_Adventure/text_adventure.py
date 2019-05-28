from __future__ import print_function
import random

# this will let the user input their username
username = raw_input("Username: ")

if username == " ":
    print("Please enter a username")
    username = raw_input("Username: ")

username = username[0].upper() + username[1:]

usernames = username + "'s"

# this is the end function if the user does something wrong
def end():
    print("The murderer found and killed", username)

def stage_2():
    # the paragraph below is the opening scene
    print(username, "works for the police, and has just gotten promoted to a \
lieutenant. ", username, "is taking a casual stroll in the park, when a flash \
of light catches", usernames, "eye.  Curious,", username, "walks towards the \
copse of trees the light had come from.  As", username, "approaches the area,"\
, username, "sees a clearing with a mound on it. ", username, "finds a body in \
the grass. A fair man is wearing a grey suit and a gold watch- that must have \
been where the light had come from. His hair is a platinum blonde, and he is \
wearing a wedding ring. There is a knife wound in his chest. ", username, \
"calls the police chief and he tells", username, "that either", username, "can \
lead the investigation or let someone else. He hangs up.\n")
stage_2()

# This is the first choice in the game, it is if you take investigation or not
take_job = raw_input('Take the investigation?(Yes or No):  ')

path = 0

if take_job == 'Yes':
    path = 1
elif take_job == 'No':
    path = 2
else:
    end()
# this is the correct choice
if path == 1:
    print(username, 'sets up a crime scene there as the other police arrive.',\
    username,'thinks about how to start the investigation. Should he pick DNA'\
    ' from the victim\'s body, or should he find out how long ago  he was'\
    ' murdered?\n')
# time or dna is another choice in the story
    time_or_dna = raw_input('Pick DNA or find out how long ago the murder took'\
    'place? (DNA or Time):  ')
# story if picked DNA; LOSING PATH
    if time_or_dna == 'DNA':
        print(username, 'picks up some DNA from the body of the victim.', \
        username, 'has just gotten the results with the identity of the victim'\
        'back, when he is suddenly murdered.')
# story if picked time; WINNING PATH
    elif time_or_dna == "Time":
        print(username, 'submitted some of the victim\'s blood to the lab to '\
        'find out how long ago the person was murdered. While waiting for the'\
        ' results of the test to come back,', username, 'begins looking for'\
        ' suspects. Only one name comes up: Anthony Lang. Once',username,
        'gets the lab results back,',username,'goes to the house of '\
        'Anthony Lang.',username,'knocks on Lang\'s door. Lang opens the door.'\
        'you ask him a series of questions.',username,'thinks to himself,'\
        ' should I search his house or leave?\n') 
# another choice in the game
        search_or_leave = raw_input('Search his house or leave? (Search or '\
        'Leave):  ')
# result if picked search
        if search_or_leave == 'Search': 
            print(username,'steps inside his house. He first goes inside '\
            'the living room, checking all the obvious places. The two '\
            'officers with', username,'go past the living room into his '\
            'kitchen. Suddenly, one of the officers runs up to you, holding'\
            ' the knife in a bag.',username,' arrests the man and goes back '\
            'to the police headquarters.',username,'interrogates the '\
            'suspect. He confesses to the murder.'\
            '                                                                 '\
            ' Congratulations! You won. The End.')
# result if picked leave
        elif search_or_leave == 'Leave':
            print(username,'tells Anthony Lang bye and leaves. Then, the'\
            ' murderer strikes again and stabs you in the stomach. Then the'\
            ' murderer flees.')
        else:
            end()
            
# second choice where you lose    
elif path == 2:
    end()
    path = 0