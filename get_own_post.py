# get_own_post.py file created
import requests
import urllib

from clint.textui import colored
from constants import APP_ACCESS_TOKEN,BASE_URL

def get_own_post():

    # function logic
    request_url = (BASE_URL + 'users/self/media/recent/?access_token= %s') % (APP_ACCESS_TOKEN)
    print colored.yellow('GET request url : %s' % (request_url))

    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:

        #extract post id
        if len(own_media['data']):

            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url =  own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)

            print colored.green('Your image has been downloaded')

        else:
            print colored.red('Post does not exist')

    else:
        print colored.red('Status code received is other than 200')
        exit()

