
def send_sms(text):

    import requests
    url = "https://api-sens.ncloud.com/v1/sms/services/{serviceId}/messages".format(serviceId="ncp:sms:kr:254226311303:test")
    access_key = "96731ee77ea24d69921701a9fb589a23"
    import datetime
    now = str(datetime.datetime.now())
    API_KEY = "ipPXMDKFhzteTHY5ipS6"
    API_SECRET = "96731ee77ea24d69921701a9fb589a23"
    headers = {"Content-Type":"application/json; charset=utf-8","x-ncp-auth-key":API_KEY,"x-ncp-service-secret":API_SECRET}
    data = {
    "type":"SMS",
    "contentType":"COMM",
    "countryCode":"82",
    "from":"01029209599",
    "to":[
        "01066474058"
    ],
    "subject":"",
    "content":""
    }
    import json
    data = json.dumps(data)
    req = requests.post(url,data=data,headers=headers)
    print(req.status_code)
    print(req.content)
if __name__ == '__main__':
    send_sms("hello world")