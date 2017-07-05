import requests,urllib
# requests for making request to fetch the data ,urllib for downloading post/media

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

# APP_ACCESS_TOKEN & BASE URL in caps because we make them highlighted so that no other user will chnage
global APP_ACCESS_TOKEN , BASE_URL
APP_ACCESS_TOKEN='4524609704.a74c90c.aab5743274734c15920c5d78fee925a2'
# access token:  4524609704.a74c90c.aab5743274734c15920c5d78fee925a2
# sandbox users: insta.mriu.test.0,insta.mriu.test.1,insta.mriu.test.2

BASE_URL='https://api.instagram.com/v1/'

# function to get own information and function name: self_information()


def self_information():
  request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_information = requests.get(request_url).json()         # it will convert data in json format by .json()
  print user_information

  # if else loop to check whether there is user exist or not and if not then it will show 200 error
  if user_information['meta']['code'] == 200:
    if len(user_information['data']):
      print 'Your Username: %s' % (user_information['data']['username'])
      print 'Number of followers you have : %s' % (user_information['data']['counts']['followed_by'])
      print 'Number of people you are following: %s' % (user_information['data']['counts']['follows'])
      print 'Number of posts you have: %s' % (user_information['data']['counts']['media'])
    else:
      print 'User does not exist!'
  else:
    print 'Status code other than 200 received!'


# get_user_id function to fetch the user id from username
def get_follower_user_id(insta_username):
  request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_information = requests.get(request_url).json()
  print user_information

  if user_information['meta']['code'] == 200:
    if len(user_information['data']):
      return user_information['data'][0]['id']
    else:
      return None
  else:
    print 'Status code other than 200 received!'
    exit()


# function for getting user information from username
def get_follower_user_information(insta_username):
  user_id = get_follower_user_id(insta_username)
  print user_id
  if user_id == None:
    print 'User does not exist!'
    exit()
  request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_information = requests.get(request_url).json()
  print user_information

  if user_information['meta']['code'] == 200:
    if len(user_information['data']):
      print 'Username: %s' % (user_information['data']['username'])
      print 'No. of followers: %s' % (user_information['data']['counts']['followed_by'])
      print 'No. of people you are following: %s' % (user_information['data']['counts']['follows'])
      print 'No. of posts: %s' % (user_information['data']['counts']['media'])
    else:
      print 'There is no data for this user!'
  else:
    print 'Status code other than 200 received!'


def get_own_post():
  request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  own_media = requests.get(request_url).json()

  if own_media['meta']['code'] == 200:
    if len(own_media['data']):
      image_name = own_media['data'][0]['id'] + '.jpeg'
      image_url = own_media['data'][0]['images']['standard_resolution']['url']
      urllib.urlretrieve(image_url, image_name)
      print 'Your image has been downloaded!'
    else:
      print 'There is no post available!'
  else:
    print 'Status code other than 200 received!'

def get_follower_user_post(insta_username):
  user_id = get_follower_user_id(insta_username)
  if user_id == None:
    print 'User does not exist!'
    exit()
  request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_media = requests.get(request_url).json()

  if user_media['meta']['code'] == 200:
    if len(user_media['data']):
      image_name = user_media['data'][0]['id'] + '.jpeg'
      image_url = user_media['data'][0]['images']['standard_resolution']['url']
      urllib.urlretrieve(image_url, image_name)
      print 'Your image has been downloaded!'
    else:
      print 'There is no post available!'
  else:
    print 'Status code other than 200 received!'


# calling self_information function
self_information()
get_follower_user_id('insta.mriu.test.0')
get_follower_user_information('insta.mriu.test.0')
get_own_post()
get_follower_user_post('insta.mriu.test.0')