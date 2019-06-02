ENDPOINT = "http://localhost:5000"
def test():
    import requests
    url = f"{ENDPOINT}/viewmessage"
    data = {"user_id": "tester"}
    req = requests.get(url, data)
    print(req.text)
    print(req.status_code)

if __name__ == '__main__':
    test()