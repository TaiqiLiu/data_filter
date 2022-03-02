import json
import operator

from flask import jsonify, request

from app import app

from .data_receive import Receive

#route1:Return fixed Response body and Response status
@app.route('/api/ping', methods=['GET'])
def route1():
    response_body = {"success": "True"}
    return json.dumps(response_body), 200

#Perform data processing and return sorted json data
@app.route('/api/posts', methods=['GET'])
def route2():
    #Receive tags parameter and handling invalid tags
    tags = request.args.get('tags', type=str, default=None)
    if (tags == None):
        return {"error": "Tags parameter is required"}, 400
    
    #Receive sortBy parameter and handling invalid sortBy
    sortBy = request.args.get('sortBy', type=str, default='id')
    if (sortBy != "id") & (sortBy != "reads") & (sortBy != "likes") & (sortBy != "popularity"):
        return {"error": "sortBy parameter is invalid"}, 400
    
    #Receive direction parameter and handling invalid parameter
    direction = request.args.get('direction', type=str, default='asc')
    if (direction != "asc") & (direction != "desc"):
        return {"error": "direction parameter is invalid"}, 400
    if (direction == 'asc'):
        reverse = False
    if (direction == 'desc'):
        reverse = True

    tag_list = tags.split(",")  #Store tag values into the list

    data = []
    #De-duplication and merging of data, 
    #only elements that are not in the data list will enter the data list
    for index in range(len(tag_list)):
        new_data = json.loads(Receive.get_json(tag_list[index])).get("posts", [])
        for item in new_data:
            if item not in data:
                data.append(item)
    
    #Sort the internal elements of the list, 
    #according to the sortBy and direction parameters
    sorted_x = sorted(data, key=operator.itemgetter(sortBy), reverse=reverse)
    result = json.dumps({"posts": sorted_x})

    return result, 200
