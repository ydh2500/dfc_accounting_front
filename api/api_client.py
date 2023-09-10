import requests

BASE_URL = "http://127.0.0.1:8000/api/"

def fetch_regions():
    response = requests.get(f"{BASE_URL}regions/")
    return response.json()

def fetch_region_by_name(name):
    response = requests.get(f"{BASE_URL}regions/?name={name}")
    return response.json()
