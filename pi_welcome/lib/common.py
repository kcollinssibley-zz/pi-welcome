from datetime import tzinfo, timedelta, datetime

# TODO(KCS): Add logging
def checkStatus(resp):
    status = resp.status_code
    if status == 200:
        return True
    elif status == 400:
        print("400, Invalid sort key")
    elif status == 403:
        print("403 Forbidden")
    elif status == 429:
        print("429 Too many requests")
    else:
        print("Unknown status code: {}".format(status))

    return False

class EST(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=4)
    def tzname(self, dt):
        return "+04:00"
    def dst(self, dt):
        return timedelta(hours=3)
    def  __repr__(self):
        return f"{self.__class__.__name__}()"

est = EST()
