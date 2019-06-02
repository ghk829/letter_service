ENDPOINT = "http://localhost:5000"

def test():
    import requests
    url = f"{ENDPOINT}/sendmessage"
    data = {"source":"tester","target":"01029209599","type":"text","text":"사랑한다 근화야"}
    req = requests.post(url,data)
    print(req.text)
    print(req.status_code)

    import requests
    url = f"{ENDPOINT}/sendmessage"
    data = {"source": "tester", "target": "01066544058", "type": "text", "text": "사랑한다 현석아"}
    req = requests.post(url, data)
    print(req.text)
    print(req.status_code)



if __name__ == '__main__':
    test()