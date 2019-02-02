import json
import re
import os
from botocore.vendored import requests

def message(event, context):
  if event:
    if event.get('body'):
      body = json.loads(event['body'])
      if body and re.match(os.environ['GROUPME_BOT_TRIGGER_REGEX'], body['text']):
        msg = {
          "bot_id"  : os.environ['GROUPME_BOT_ID'],
          "text": "",
          "attachments" : [
            {
              "type"  : "image",
              "url"   : os.environ['GROUPME_IMAGE_LINK']
            }
          ]
        } 
        print("**** Sending response for: {}".format(body['text']))
        requests.post('https://api.groupme.com/v3/bots/post', json=msg)

