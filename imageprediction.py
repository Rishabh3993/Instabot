from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Geo, GeoPoint, GeoLimit

#  CLARIFAI_API_KEY='da2b1959b1e64afb9e4a96b1da783688'
app=ClarifaiApp(api_key='da2b1959b1e64afb9e4a96b1da783688')

# get the general model
model = app.models.get("general-v1.3")

def predict_image():


    # predict with the model
    #print model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

    #image = CImage(url='https://samples.clarifai.com/metro-north.jpg')
    #model.predict([image])

    #url_enter=raw_input('Please enter the URL of the image you want see :')
    #print model.predict_by_url(url=url_enter)


    predict_by_geo=app.inputs.search_by_geo(GeoPoint(30, 40), GeoLimit("mile", 10))
    print predict_by_geo

    #app.inputs.search_by_original_url(url='https://samples.clarifai.com/metro-north.jpg')
    #print app.inputs.search_by_original_url

predict_image()
'''
To access the models: use app.models
To access the inputs: use app.inputs
To access the concepts: use app.concepts


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
'''