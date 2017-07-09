# like_user_post.py file is created

import requests

from clint.textui import colored
from constants import APP_ACCESS_TOKEN,BASE_URL
from get_users_post import get_users_post

def like_a_post(insta_username):
    # function logic
    media_id = get_users_post(insta_username)

    if media_id == None:
        print colored.red('\nUsername does not exist')
        exit()
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {'access_token' : APP_ACCESS_TOKEN}
    print colored.yellow('\nPOST request url : %s' % (request_url))
    user_info = requests.post(request_url,payload).json()

    if user_info['meta']['code'] == 200:
        print colored.red('\nPost liked Successfully')
    else:
        print colored.red('\n\nStatus code received is other than 200')
        print colored.red('\nUnable to like the recent Post')
        exit()
