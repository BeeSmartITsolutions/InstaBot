#import libraries for natural language processing
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from get_post_id import *
from constants import *
import requests

#define a function for deleting the negative comment
def del_neg_comment(insta_username):
    post_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (post_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comnt_info = requests.get(request_url).json()

    if comnt_info['meta']['code'] == 200:
        if len(comnt_info['data']):
            #Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comnt_info['data'])):
                comnt_id = comnt_info['data'][x]['id']
                comnt_text = comnt_info['data'][x]['text']
                anlz = TextBlob(comnt_text, analyzer=NaiveBayesAnalyzer())

               #check that text contain negative sentiment or positive sentiment.if negative comment found sent request to delete that comment
                if anlz.sentiment.p_neg > anlz.sentiment.p_pos:
                    print 'Negative comment : %s' % comnt_text
                    del_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (post_id, comnt_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (del_url)
                    delete_info = requests.delete(del_url).json()

                    #return the delete request response
                    if delete_info['meta']['code'] == 200:
                        print 'comment successfully deleted!\n'
                    else:
                        print 'unable to delete comment!'
                else:
                    print 'positive comment : %s' % (comnt_text)
        else:
            print 'no comments on the post!'
    else:
        print 'no response from server'
