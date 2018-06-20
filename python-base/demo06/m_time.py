
import time


def say_time():
    return time.ctime()

def application(request, handle_headers):
    env = {
        "PATH_INFO":file_name,
        "QUERY_STRING":param
    }

    handle_headers(status_code, [("Content-type","text/plain"),("hello","world")])
    pass
