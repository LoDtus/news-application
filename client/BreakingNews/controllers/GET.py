import requests
from requests.auth import HTTPBasicAuth

def getAllPost():
    url = "http://localhost:8080/posts"
    username = "user"
    password = ""
    
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        posts = response.json()
        return posts
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def getPost_byId(id):
    url = f"http://localhost:8080/posts/{id}"
    username = "user"
    password = ""
    
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        posts = response.json()
        return posts
    except requests.RequestException as e:
        return f"An error occurred: {e}"