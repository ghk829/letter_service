
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
    "type":"LMS",
    "contentType":"COMM",
    "countryCode":"82",
    "from":"01029209599",
    "to":[
        "01066474058"
    ],
    "subject":"GlassWill 유서편지서비스",
    "content":"유서편지서비스"
              "\n"
              "GlassWill에서 박채현님이 작성한 편지가 도착했습니다"
              "\n"
              "http://www.glasswill.com?token=1iyu2u318dh21828"
    }
    import json
    data = json.dumps(data)
    req = requests.post(url,data=data,headers=headers)
    print(req.status_code)
    print(req.content)
if __name__ == '__main__':
    send_sms("hello world")