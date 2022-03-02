import json

#Test whether route1 can return correct data
def test_error_handling(app, client):
    res = client.get('/api/ping')
    assert res.status_code == 200
    expected = {"success": "True"}
    assert expected == json.loads(res.get_data(as_text=True))