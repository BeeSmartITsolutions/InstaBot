# comment_on_user_post.py file created

import requests

from clint.textui import colored
from constants import APP_ACCESS_TOKEN,BASE_URL
from get_users_post import get_users_post

def commment_on_a_post(insta_username):
    # function logic
    media_id = get_post_id(insta_username)

    if media_id == None:
        print colored.red('\nUsername does not exist')
        exit()
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    comment = raw_input('\n\nPlease enter your comment:-\t')
    payload = {'access_token': APP_ACCESS_TOKEN , 'text': comment}
    print colored.yellow('\nPOST request url : %s' % (request_url))
    user_info = requests.post(request_url,payload).json()

    if user_info['meta']['code'] == 200:
        print colored.red('\nComment posted  Successfully')
    else:
        print colored.red('\n\nStatus code received is other than 200')
        print colored.red('\nUnable to post the comment on the recent Post')
        exit()
