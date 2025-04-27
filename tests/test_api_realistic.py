import time

def test_health_check(playwright_context):
    response = playwright_context.get("/api/health")
    assert response.status == 200
    assert response.headers.get("content-type", "").startswith("application/json")
    json_data = response.json()
    assert json_data == {"status": "healthy"}

def test_valid_get_request(playwright_context):
    params = {"name": "John", "age": "30"}
    response = playwright_context.get("/api/test", params=params)
    assert response.status == 200
    json_data = response.json()
    assert json_data["message"] == "This is a GET request"
    assert json_data["params"]["name"] == "John"
    assert json_data["params"]["age"] == "30"

def test_valid_post_request(playwright_context):
    payload = {"username": "admin", "password": "secret"}
    response = playwright_context.post("/api/test", data=payload)
    assert response.status == 201
    json_data = response.json()
    assert json_data["message"] == "This is a POST request"
    assert json_data["data"]["username"] == "admin"
    assert json_data["data"]["password"] == "secret"

def test_invalid_endpoint(playwright_context):
    response = playwright_context.get("/api/unknown")
    assert response.status == 404

def test_post_invalid_payload(playwright_context):
    payload = "just_a_string_instead_of_json"
    response = playwright_context.post("/api/test", data=payload)
    assert response.status == 415  # corrected

def test_response_time_under_threshold(playwright_context):
    start = time.perf_counter()
    response = playwright_context.get("/api/health")
    end = time.perf_counter()
    elapsed_time_ms = (end - start) * 1000
    assert elapsed_time_ms < 500  # milliseconds
