import requests

# APP_ACCESS_TOKEN & BASE URL in caps because we make them highlighted so that no other user will chnage

APP_ACCESS_TOKEN='4524609704.a74c90c.aab5743274734c15920c5d78fee925a2'
# access token:  4524609704.a74c90c.aab5743274734c15920c5d78fee925a2
# sandbox users: insta.mriu.test.0,insta.mriu.test.1,insta.mriu.test.2

BASE_URL='https://api.instagram.com/v1/'

# function to get own information and function name: self_information()
def self_information():
  request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)

  # it will convert data in json format by .json()
  user_information = requests.get(request_url).json()
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
def get_user_id(insta_username):
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
def get_user_information(insta_username):
  user_id = get_user_id(insta_username)
  print user_id
  if user_id == None:
    print 'User does not exist!'
    exit()
  request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_information = requests.get(request_url).json()

  if user_information['meta']['code'] == 200:
    if len(user_info['data']):
      print 'Username: %s' % (user_information['data']['username'])
      print 'No. of followers: %s' % (user_information['data']['counts']['followed_by'])
      print 'No. of people you are following: %s' % (user_information['data']['counts']['follows'])
      print 'No. of posts: %s' % (user_information['data']['counts']['media'])
    else:
      print 'There is no data for this user!'
  else:
    print 'Status code other than 200 received!'


# calling self_information function
self_information()