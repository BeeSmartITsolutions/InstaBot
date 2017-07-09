# get_own_post.py file created
import requests
from constants import APP_ACCESS_TOKEN,BASE_URL
def get_own_post():
    # function logic
    request_url = (BASE_URL + '/users/self/media/recent/?access_token= %s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        #extract post id
        if len(own_media['data']):
            return own_media['data'][0]['id']
        else:
            print 'Post does not exist'
    else:
        print 'status code received is other than 200'
        exit()

