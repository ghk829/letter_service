
def send_sms(text):

    import nexmo

    client = nexmo.Client(key='8ddd8da6', secret='wa5yleKByu6FNWpG')

    client.send_message({
        'from': 'GlassWill',
        'to': '821029209599',
        'text': text,
    })

if __name__ == '__main__':
    send_sms("hello world")