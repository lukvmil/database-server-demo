import argparse
import httpx


base_url = "http://localhost:4000"

def get(key: str):
    resp = httpx.get(f"{base_url}/get?key={key}")
    return resp.text
    
def set(key: str, val: str):
    httpx.post(f"{base_url}/set?{key}={val}")

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=True)

get_parser = subparsers.add_parser("get")
get_parser.add_argument("key", type=str)

set_parser = subparsers.add_parser("set")
set_parser.add_argument("key", type=str)
set_parser.add_argument("val", type=str)

if __name__ == "__main__":
    args = parser.parse_args()
    
    if args.command == "get":
        print(get(args.key))
    elif args.command == "set":
        set(args.key, args.val)
        print(f"set {args.key}={args.val}")