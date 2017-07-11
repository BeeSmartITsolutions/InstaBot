# list_of_comments.py file created
import requests

from get_user_post_id import get_post_id
from constants import APP_ACCESS_TOKEN, BASE_URL
from clint.textui import colored


# this file is used to fetch the user info from the instagram
def get_list_of_comments(insta_username):
    # function logic
    post_id = get_post_id(insta_username)

    if post_id == None:
        print colored.red('Username does not exist')
        exit()
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (post_id, APP_ACCESS_TOKEN)
    print colored.yellow('GET request url : %s' % (request_url))
    post_comment_info = requests.get(request_url).json()

    if post_comment_info['meta']['code'] == 200:
        if len(post_comment_info['data']):
           return post_comment_info['data']
        else:
            return None
    else:
        print colored.red('Status code received is other than 200')
        exit()