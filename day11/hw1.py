"""
    HW: Fetch content from URLS
"""

from concurrent.futures import ThreadPoolExecutor
import time
import random 
import requests

urls = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://api.github.com/users/octocat",
    "https://dog.ceo/api/breeds/image/random",
    "https://api.coindesk.com/v1/bpi/currentprice.json",
    "https://api.agify.io/?name=sam",
    "https://example.com/",
    "https://httpbin.org/html",
    "https://loripsum.net/api/1/short/plaintext",
    "https://httpbin.org/get",
    "https://reqres.in/api/users?page=2"
]

def fetch_content(url):
    
    try:
        req = requests.get(url)
        if req.status_code == 200:
            return (url, req.content)
    except:
        return (url, "NO CONTENT")        

with ThreadPoolExecutor(max_workers=3) as texec:
    
    futures = [texec.submit(fetch_content, url) for url in urls]
    
    for f in futures:
        url, content = f.result()
        print(f"{url}: {content}\n\n")
        
print("Fetched contents from all URLS")