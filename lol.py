import requests

url = "https://community-hacker-news-v1.p.rapidapi.com/topstories.json"

querystring = {"print":"pretty"}

headers = {
    'x-rapidapi-host': "community-hacker-news-v1.p.rapidapi.com",
    'x-rapidapi-key': "da61819e2cmsh5ce4ac534aaad45p1b29fejsnfcbad15808db"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
