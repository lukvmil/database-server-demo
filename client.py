import httpx

base_url = "http://localhost:4000"

def get(key: str):
    resp = httpx.get(f"{base_url}/get?key={key}")
    return resp.content
    
def set(key: str, val: str):
    resp = httpx.post(f"{base_url}/set?{key}={val}")
