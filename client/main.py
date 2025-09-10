import os, requests

HUB_URL = os.environ.get("HUB_URL", "http://localhost:8000")

def main():
    try:
        r = requests.get(f"{HUB_URL}/health", timeout=5)
        print("Hub health:", r.json())
    except Exception as e:
        print("Client could not reach hub:", e)

if __name__ == "__main__":
    main()
