import requests

from clint.textui import colored
from constants import APP_ACCESS_TOKEN, BASE_URL
# self_info function
def self_info():
    # function logic
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print colored.yellow('GET request url :- %s' % (request_url))
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):


            print colored.green('\nUsername is : %s' % (user_info['data']['username']))
            print colored.green('\nNumber of people who are following you are : %s' % (user_info['data']['counts']['followed_by']))
            print colored.green('\nNumber of people whom you are following are : %s' % (user_info['data']['counts']['follows']))
            print colored.green('\nNumber of posts you have uploaded till now are : %s' % (user_info['data']['counts']['media']))

        else:
            print colored.red('User does not exist')

    else:
        print colored.red('status code received is other than 200')
        exit()