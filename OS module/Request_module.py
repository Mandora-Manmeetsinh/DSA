import requests

response = requests.get("https://www.linkedin.com")
print(response.text)