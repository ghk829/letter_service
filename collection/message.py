class Message:
    source = ""
    target = ""
    type = ""
    date = ""
    url = ""
    text = ""

    def __init__(self,**kwargs):
        for k,v in kwargs:
            setattr(self,k,v)
        import datetime
        self.date = datetime.datetime.now()
