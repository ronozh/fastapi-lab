def test_root(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello, FastAPI!"}


def test_hello_with_query_param(client):
    assert client.get("/hello/Ada").json() == {"message": "Hello, Ada."}
    assert client.get("/hello/Ada?excited=true").json() == {"message": "Hello, Ada!"}
