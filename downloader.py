import requests

def get_query(query: str) -> None:
    req = requests.get(f"https://mangadexpi.vercel.app/anime/zoro/{query}?page=1")
    
    print(req.json())
    
if __name__ == "__main__":
    get_query("konosuba")