import requests

url = "https://httpbin.org/post"

user_data = {
    "username": "python_coder",
    "status": "learning requests",
    "score": 100,
    "city": "Bishkek",
    "Language": "Python"
}

response = requests.post(url, json=user_data)
print(f"Pesponse Status: {response.status_code}")
print("-" * 30)

data = response.json()

print(data["json"])

print(f"\nHello, {data['json']['username']}! Your status: {data['json']['status']}")