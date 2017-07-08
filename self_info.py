import requests
from constants import APP_ACCESS_TOKEN, BASE_URL
# self_info function
def self_info():
    # function logic
    request_url = (BASE_URL + 'users/self/?access_token= %s') % (APP_ACCESS_TOKEN)
    print 'GET request url :- %s' % (request_url)
    user_info = requests.get(request_url).json()
    print user_info