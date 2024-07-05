import requests
import json
import time

def send_data():
    url = 'https://122.50.5.62:8700/api/v1/EbtKjHbosu6PEHyNMQKJ/telemetry'
    headers = {
        'X-Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJkZW1vQHNvbHUuY28uaWQiLCJ1c2VySWQiOiIwMzliYmRjMC1kNWQ2LTExZWUtYmViZS1kOTdhMWJmZTZhNzkiLCJzY29wZXMiOlsiVEVOQU5UX0FETUlOIl0sInNlc3Npb25JZCI6ImMwNWIwMzg2LTM0MmItNGIxOS1hZDNkLWFhN2IyNGUyZTk0YyIsImV4cCI6MTcyMDE2ODk2OCwiaXNzIjoidGhpbmdzYm9hcmQuaW8iLCJpYXQiOjE3MjAxNTk5NjgsImZpcnN0TmFtZSI6IkRlbW8iLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiOGMyMTMxODAtZDVkNS0xMWVlLWJlYmUtZDk3YTFiZmU2YTc5IiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCJ9.3jLGZNwxzmj5bLdQy4mkKg0YVAegMK2QhAQNCA03fRHvfkkMzkusCGnW0BNO8e90hdzQ1-VTFRljQ-BIlsZE6g',
        'Content-Type': 'application/json'
    }
    payload = {
        "moisture": 90,
        "temperature": 20,
        "humidity": 90,
        "voltage": 220
    }

    try:
        response = requests.post(url, headers=headers, json=payload, verify=False)
        print(f'Status Code: {response.status_code}')
        print(f'Response: {response.text}')
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == "__main__":
    interval_seconds = 3
    
    while True:
        send_data()
        time.sleep(interval_seconds)
