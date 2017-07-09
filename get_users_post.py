# get_users_post.py file created
import requests
from get_user_id import get_user_id
from constants import APP_ACCESS_TOKEN, BASE_URL

def get_users_post( insta_username):
    # function logic

    user_id = get_user_id(insta_username)

    if user_id == None:
        print 'Username doesnot exist'
        exit()

    request_url = (BASE_URL + '/users/%s/media/recent/?access_token= %s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    