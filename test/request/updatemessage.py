ENDPOINT = "http://localhost:5000"
def test():
    message_id = '5cf31a39ef093c99181bc448'
    import requests
    url = f"{ENDPOINT}/updatemessage"
    data = {"id": message_id,"text":"업데이트 메세지 테스트입니다"}
    headers = {'Content-Type': 'application/json'}
    import json
    req = requests.post(url, data=json.dumps(data),headers=headers)
    print(req.text)
    print(req.status_code)


if __name__ == '__main__':

    test()