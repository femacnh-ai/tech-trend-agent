import requests
import os
def search_news():
   url = "https://api.tavily.com/search"
   payload = {
       "api_key": os.environ["TAVILY_API_KEY"],
       "query": "smart tv os platform webos tizen chromium browser engine",
       "max_results": 10
   }
   response = requests.post(url, json=payload)
   return response.json()["results"]
