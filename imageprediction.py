from clarifai import rest
from clarifai.rest import ClarifaiApp

#  CLARIFAI_API_KEY='da2b1959b1e64afb9e4a96b1da783688'
app=ClarifaiApp(api_key='da2b1959b1e64afb9e4a96b1da783688')

# get the general model
model = app.models.get("general-v1.3")

# predict with the model
print model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

