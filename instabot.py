# instabot.py file created
import time

from clint.textui import colored

from self_info import self_info
from get_user_info import get_user_info
from get_own_post import get_own_post
from get_users_post import get_users_post
from like_user_post import like_a_post
from comment_on_user_post import commment_on_a_post


print colored.yellow('\n\n\t***************************************************')
print colored.green('\t\t\tWelcome to InstaBot')
print colored.green('\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print colored.yellow('\t***************************************************\n')

show_menu = True

while show_menu:

    menu_choices = colored.cyan("\nWhat do you want to do? \n\n1.\tFetch your own details \n2.\tFetch your recent "
                                "post \n3.\tFetch your other users detail \n4.\tFetch your other users recent post "
                                "\n5.\tLike the other users recent post \n6.\tComment on other users recent post "
                                "\n7.\tClose Application\n\n")
    menu_choice = raw_input(menu_choices)

    if len(menu_choice) > 0:
        menu_choice = int(menu_choice)

        if menu_choice == 1:

            # fetching own information
            print colored.green('\n\nYou want to see your own details\n')
            self_info()
            print '\n\n'

        elif menu_choice == 2:

            # fetching your recent post
            print colored.green('\n\nYou want to see your recent post\n')
            get_own_post()
            print '\n\n'

        elif menu_choice == 3:

            # fetching other users detail
            print colored.green('\n\nYou want to see other users detail\n')
            other_username = 'kunal_pathak21'
            get_user_info(insta_username= other_username)
            print '\n\n'


        elif menu_choice == 4:

            # fetching the other users recent post
            print colored.green('\n\nYou want to see other users recent post\n')
            other_username = raw_input('Enter the username')
            get_users_post(insta_username=other_username)
            print '\n\n'

        elif menu_choice == 5:

            # like the other users recent post
            print colored.green('\n\nYou want to like the other users recent post\n')
            other_username = raw_input('Enter the username')
            like_a_post(insta_username= other_username)
            print '\n\n'

        elif menu_choice == 6:

            # Post a comment on the other users recent post
            print colored.green('\n\nYou want to post a comment on the other users recent post\n')
            other_username = raw_input('Enter the username')
            commment_on_a_post(insta_username=other_username)
            print '\n\n'

        elif menu_choice == 7:

            # you want to close the application
            print colored.green('\n\nYou are about to exit in 5 seconds....')
            s = 0
            m = 0
            h = 0
            while s <= 5:
                print h, colored.cyan('Hours'), m, colored.cyan('Minutes'), s, colored.cyan('Seconds')
                time.sleep(1)
                s += 1
                if s == 5:
                    exit()
                    show_menu = False
        else:
            print colored.red('\n\nYou entered the wrong input. Please provide the input according to list.')
    else:
        print colored.red('\n\nYou haven\'t provided input. Please enter some input')
