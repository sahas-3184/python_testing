import random
import requests
import time
import json

class AIAgent:
    def __init__(self, base_url, output_file="test_results.json"):
        self.base_url = base_url
        self.output_file = output_file
        self.results = []

    def random_test(self, endpoint, methods, payloads=None):
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

            result = {
                "method": method,
                "url": url,
                "payload": payload,
                "status_code": response.status_code,
                "response_body": response.json() if response.content else None,
            }

            # Add response time
            result['response_time'] = response.elapsed.total_seconds() * 1000  # in milliseconds

            return result

        except Exception as e:
            return {"error": str(e)}

    def run_tests(self, endpoints, methods, payloads, iterations=5):
        print("Running tests with AI Agent...")
        for endpoint in endpoints:
            for _ in range(iterations):  # Perform multiple tests for each endpoint
                result = self.random_test(endpoint, methods, payloads)
                self.log_result(result)

    def log_result(self, result):
        # Append result to the in-memory list
        self.results.append(result)

    def save_results_to_json(self):
        # Write the results to the specified JSON file
        with open(self.output_file, "w") as outfile:
            json.dump(self.results, outfile, indent=4)
            print(f"Test results saved to {self.output_file}")

# Example of using the agent
if __name__ == "__main__":
    agent = AIAgent(base_url="http://127.0.0.1:5000")
    endpoints = ["/api/test", "/api/health"]
    methods = ["GET", "POST"]
    payloads = [{"key1": "value1"}, {"key2": "value2"}, None]

    # Run tests
    agent.run_tests(endpoints, methods, payloads)

    # Save results to a JSON file
    agent.save_results_to_json()
