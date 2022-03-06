
import base64
import json
import os
import time

#install both requests and tweepy libraries using pip
import requests
import tweepy

CACHE_FILE_NAME = ".twitter_bot_reaper.json"
CONFIG_FILE = 'config_reaper.json'
#add your access keys into config.json



def load_config(config_file):
   with open(config_file) as f:
      config = json.loads(f.read())
   return config

def get_bearer_header(consumer_key, consumer_secret):
    uri_token_endpoint = 'https://api.twitter.com/oauth2/token'
    key_secret = f"{consumer_key}:{consumer_secret}".encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')
    auth_headers = {
       'Authorization': 'Basic {}'.format(b64_encoded_key),
       'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
       }

    auth_data = {
       'grant_type': 'client_credentials'
    }


    auth_resp = requests.post(uri_token_endpoint, headers=auth_headers, data=auth_data)
    bearer_token = auth_resp.json()['access_token']
   
    bearer_header = {
       'Accept-Encoding': 'gzip',
       'Authorization': 'Bearer {}'.format(bearer_token),
       'oauth_consumer_key': consumer_key 
    }
   
    return bearer_header

def get_cached_data(file_name):
    if not os.path.exists(file_name):
       return []
    with open(file_name) as f:
        data = json.loads(f.read())
    if data:
       return data
    else:
       return []


def save_cached_data(file_name, data):
    with open(file_name, 'w') as f:
        f.write(json.dumps(data))
     
def getConversationId(id, bearer_header):
    uri = 'https://api.twitter.com/2/tweets?'

    params = {
       'ids':id,
       'tweet.fields':'conversation_id'
    }
   
    resp = requests.get(uri, headers=bearer_header, params=params)
    return resp.json()['data'][0]['conversation_id']

def getConversation(conversation_id, bearer_header):
    uri = 'https://api.twitter.com/2/tweets/search/recent?'

    params = {'query': f'conversation_id:{conversation_id}',
              'tweet.fields': 'in_reply_to_user_id', 
              'tweet.fields':'conversation_id'
    }
   
    resp = requests.get(uri, headers=bearer_header, params=params)
    tweets_ids = resp.json()['data']


    return tweets_ids


def connect_twitter(consumer_key, consumer_secret, access_key, access_token):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_token)
    api = tweepy.API(auth)
    return api

def get_all_mentions(file_name, tw_handler):
    previous_mentions = get_cached_data(file_name)
    all_mention_id = {}
    new_mentions = {}
    mentions = tw_handler.mentions_timeline()
    for mention in mentions:
        if mention.in_reply_to_status_id:
            all_mention_id[mention.id] = {'reply_id':mention.in_reply_to_status_id,
                                          'user_id':mention.user.id
         }

    for key in all_mention_id:
        if key not in previous_mentions:
            new_mentions[key] = all_mention_id[key]
    previous_keys = [value for value in all_mention_id.keys()]
    save_cached_data(file_name, previous_keys)
    return new_mentions


def main():
    config = load_config(CONFIG_FILE)
    consumer_key = config['consumer_key']
    consumer_secret = config['consumer_secret']
    key = config['key']
    secret = config['secret']
    tw_handler = connect_twitter(consumer_key, consumer_secret, key, secret)
    auth_header = get_bearer_header(consumer_key, consumer_secret)
    
    while True:
        new_mentions = get_all_mentions(CACHE_FILE_NAME, tw_handler)
        print(f"Got {len(new_mentions)} new mentions")
        for m_id, m_value in new_mentions.items():
            tweets_text = []
            conversation_id = getConversationId(m_value['reply_id'], auth_header)
            conversation = getConversation(conversation_id, auth_header)
            for index, value in enumerate(conversation):
                tweets_text.append(f"[{index}]: {value['text']}")

            response = tw_handler.send_direct_message(m_value["user_id"], "\n\n".join(tweets_text))
            message = response._json['message_create']['message_data']['text']
            print(f"Send {message} to {m_value['user_id']}")

        time.sleep(10)
        
if __name__ == '__main__':
    main()
