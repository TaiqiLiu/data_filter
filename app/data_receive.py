import json

import requests
from flask.json import jsonify
from flask_caching import Cache

from app import app

#Configure cache
config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}

app.config.from_mapping(config)
cache = Cache(app)


#Receive json data from the specified url address
#This function will be called in route2

class Receive:

    @classmethod
    @cache.memoize(timeout=300)  #Set up the cache to avoid repeated making API calls
    def get_json(cls, para: str): 
        url = "https://api.hatchways.io/assessment/blog/posts?tag="
        url = url+para  #Set the complete url path
        payload = ""
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text
