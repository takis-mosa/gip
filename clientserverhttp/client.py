import requests

url = f"http://192.168.0.4:8000/measurements/store/{temperatuur}/{neerslag}/" 
requests.get(url)
