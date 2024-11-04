import requests
from requests.auth import HTTPBasicAuth

def GetAllPost():
    url = "http://localhost:8080/posts"
    username = "admin"
    password = "root"
    
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        result = response.json()
        return result
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def GetPost_byId(id):
    url = f"http://localhost:8080/posts/{id}"
    username = "admin"
    password = "root"
    
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        result = response.json()
        return result
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def GetAllFollower():
    url = "http://localhost:8081/emails"
    username = "admin"
    password = "root"
    
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        result = response.json()
        return result
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def GetAllMessage():
    url = "http://localhost:8082/messages"
    username = "admin"
    password = "root"
    
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        result = response.json()
        return result
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def GetMessage_byId(id):
    url = f"http://localhost:8082/messages/{id}"
    username = "admin"
    password = "root"
    
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        result = response.json()
        return result
    except requests.RequestException as e:
        return f"An error occurred: {e}"
    
def GetAllStatistic():
    url = "http://localhost:8083/statistic"
    username = "admin"
    password = "root"
    
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        result = response.json()
        return result
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []