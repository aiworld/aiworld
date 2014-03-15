import sys
from time import sleep
import requests
from random import random
from datetime import datetime


def get_milliseconds(t):
    return (t.days * 24 * 60 * 60 + t.seconds) * 1000 + t.microseconds / 1000.0


start = datetime.now()
total_requests = 0
while True:
    total_requests += 1

    sleep(0.1)

    url = 'http://localhost:' + sys.argv[1] + '/'

    print url

    payload = {
        'move_x': random() * 2.0 - 1.0,
        'move_y': random() * 2.0 - 1.0,
        'look_x': random() * 2.0 - 1.0,
        'look_y': random() * 2.0 - 1.0,
        'jump'  : random() < 0.5,
        'shoot' : random() < 0.5
    }

    # print payload

    requests.get(url, params=payload)

    end = datetime.now()

    total_seconds = get_milliseconds(end - start) / 1000

    print 'requests per second: ', str(total_requests / total_seconds)


