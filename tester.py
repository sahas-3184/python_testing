import requests
import random
import time

class AIAgent:
    def __init__(self, base_url):
        self.base_url = base_url

    def random_test(self, endpoint, methods, payloads):
        method = random.choice(methods)
        payload = random.choice(payloads) if method == "POST" else None
        url = f"{self.base_url}{endpoint}"

        try:
            if method == "GET":
                response = requests.get(url, params=payload)
            elif method == "POST":
                response = requests.post(url, json=payload)
            else:
                return {"error": "Unsupported method"}

            return {
                "method": method,
                "url": url,
                "payload": payload,
                "status_code": response.status_code,
                "response_body": response.json() if response.content else None
            }
        except Exception as e:
            return {"error": str(e)}

def run_tests():
    base_url = "http://127.0.0.1:5000"
    agent = AIAgent(base_url)

    # Define test scenarios
    endpoints = ["/api/test", "/api/health"]
    methods = ["GET", "POST"]
    payloads = [{"key1": "value1"}, {"key2": "value2"}, None]

    print("Waiting for server to be ready...")
    time.sleep(2)  # Small wait to ensure Flask server starts

    print("Running tests with AI Agent...")
    for endpoint in endpoints:
        for _ in range(5):  # Perform 5 random tests per endpoint
            result = agent.random_test(endpoint, methods, payloads)
            print("Test Result:", result)

if __name__ == '__main__':
    run_tests()
