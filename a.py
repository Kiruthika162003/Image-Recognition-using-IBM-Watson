# simple Python  example for using the IBM Watson Visual Recognition service to analyze an image and detect objects:
# Import the required libraries
import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Replace with your IBM Cloud API Key
api_key = 'YOUR_API_KEY'

# Initialize the Visual Recognition service
authenticator = IAMAuthenticator(api_key)
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)

# Replace 'url' with the URL of the image you want to analyze
image_url = 'URL_OF_YOUR_IMAGE'

# Call the API to classify the image
response = visual_recognition.classify(url=image_url).get_result()

# Extract and display the results
if 'images' in response and len(response['images']) > 0:
    image = response['images'][0]
    if 'classifiers' in image and len(image['classifiers']) > 0:
        classifier = image['classifiers'][0]
        if 'classes' in classifier and len(classifier['classes']) > 0:
            classes = classifier['classes']
            print("Detected Objects:")
            for obj in classes:
                print(f"- {obj['class']} (Confidence: {obj['score']})")
else:
    print("No objects detected in the image.")
