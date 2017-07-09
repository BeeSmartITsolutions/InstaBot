# get_user_info.py file created
import requests

from get_user_id import get_user_id
from constants import APP_ACCESS_TOKEN, BASE_URL
from clint.textui import colored

# this file is used to fetch the user info from the instagram
def get_user_info(insta_username):
    # function logic
    user_id = get_user_id(insta_username)

    if user_id == None:
        print colored.red('Username does not exist')
        exit()
    request_url = (BASE_URL + 'users/%s/?access_token= %s') % (user_id, APP_ACCESS_TOKEN)
    print colored.yellow('GET request url : %s' % (request_url))
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print colored.red('Status code received is other than 200')
        exit()
