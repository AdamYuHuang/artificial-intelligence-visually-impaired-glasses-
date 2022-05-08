# <snippet_imports>
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
# </snippet_imports>

'''
Authenticate
Authenticates your credentials and creates a client.
'''
# <snippet_vars>
subscription_key = 
endpoint = 
# </snippet_vars>
OCR=[]
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
with open(r"path", 'rb') as f:
    #result = computervision_client.describe_image_in_stream(f, max_candidates=5, language='zh', description_exclude=None, model_version='latest', custom_headers=None, raw=False, callback=None)
   #print(*result.captions)
    #print(result)
    result=computervision_client.recognize_printed_text_in_stream(f, detect_orientation=True, language='zh-Hans', model_version='latest', custom_headers=None, raw=False, callback=None)
    word=result.regions[0].lines
    for i in range(len(word)):
        for j in range(len(word[i].words)):
                OCR.append(word[i].words[j].text)
        print(OCR)
        OCR=[]
