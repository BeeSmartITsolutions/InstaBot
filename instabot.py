# instabot.py file created
from self_info import self_info
#fetching own informaation

print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print '\t\tWelcome to InstaBot'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'

answer = raw_input('Enter your choice: \n1.\tShow your own profile Details \n2.\tSearch a User by its Username 3.\nExit')

if len(answer) > 0 :
    if answer == 1:
        self_info()
    if answer == 2:
        get_user_id()