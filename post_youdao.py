from random import randint

import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    s=str(randint(0, 10))
    t=get_ts()
    # print("random = ", s)
    # print("ts =", t)
    # print("salt =",t+s)
    return t+s
    # return '15867595017047'


def get_sign():
    return 'c40d36905b5e23c8ca0f21ddc885c6da'


def get_ts():
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts
    #'1586759501704'


form_date={
    'i': '我和你都是中国',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv': 'b016bfc8dd420bcfc5d5a95c5a1600f4',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
}
response=requests.post(url,form_date)
print(response.text)