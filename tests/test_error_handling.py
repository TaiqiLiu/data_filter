import json


def test_route1(app, client):
    #Test invalid tags
    res = client.get('http://localhost:5000/api/posts?sortBy=reads&direction=desc')
    assert res.status_code == 400
    expected = {"error": "Tags parameter is required"}
    assert expected == json.loads(res.get_data(as_text=True))
    
    #Test invalid sortBy
    res = client.get('http://localhost:5000/api/posts?tags=design,science&sortBy=author&direction=desc')
    assert res.status_code == 400
    expected = {"error": "sortBy parameter is invalid"}
    assert expected == json.loads(res.get_data(as_text=True))

    #Test invalid direction
    res = client.get('http://localhost:5000/api/posts?tags=design,science&sortBy=reads&direction=')
    assert res.status_code == 400
    expected = {"error": "direction parameter is invalid"}
    assert expected == json.loads(res.get_data(as_text=True))

    