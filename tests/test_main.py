from starlette.testclient import TestClient


def test_root_endpoint(testclient: TestClient):
    r = testclient.get("/")
    assert r.status_code == 200


def test_read_item(testclient: TestClient):

    r = testclient.get("/items/1", params={"q": "query"})
    assert r.status_code == 200, r.text
    assert r.json()["item_id"] == 1


def test_update_item(testclient: TestClient):
    data = {"name": "New Item", "price": "0.38", "is_offer": True}
    r = testclient.put("/items/1", json=data)
    assert r.status_code == 200, r.text
    assert r.json()["item_name"] == data["name"]
