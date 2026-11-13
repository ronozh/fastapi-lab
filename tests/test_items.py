def test_item_crud_flow(client):
    # create
    resp = client.post("/items/", json={"name": "Widget", "price": 9.99})
    assert resp.status_code == 201
    item = resp.json()
    assert item["id"] == 1
    assert item["in_stock"] is True

    # read
    assert client.get("/items/1").json()["name"] == "Widget"
    assert len(client.get("/items/").json()) == 1

    # partial update
    resp = client.patch("/items/1", json={"price": 4.5})
    assert resp.json()["price"] == 4.5
    assert resp.json()["name"] == "Widget"

    # delete
    assert client.delete("/items/1").status_code == 204
    assert client.get("/items/1").status_code == 404


def test_validation_error(client):
    resp = client.post("/items/", json={"name": "", "price": -1})
    assert resp.status_code == 422
