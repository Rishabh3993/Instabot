import requests

APP_ACCESS_TOKEN='4524609704.a74c90c.aab5743274734c15920c5d78fee925a2'
# access token:  4524609704.a74c90c.aab5743274734c15920c5d78fee925a2
# sandbox users:

BASE_URL='https://api.instagram.com/v1/'

# function to get own information
def self_information():
  request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()
  print user_info



# calling self_information function
self_information()