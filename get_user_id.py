# get_user_id.py file created
import requests

from constants import APP_ACCESS_TOKEN, BASE_URL
from clint.textui import colored


# get_user_id function defined

def get_user_id(insta_username):
    # function logic

    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print colored.yellow('GET request url :- %s' % (request_url))
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print colored.red('Status code received is other than 200')
        exit()
