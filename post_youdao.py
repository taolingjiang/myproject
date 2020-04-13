import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_date={
    'i': '我和你都是中国',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15867595017047',
    'sign': 'c40d36905b5e23c8ca0f21ddc885c6da',
    'ts': '1586759501704',
    'bv': 'b016bfc8dd420bcfc5d5a95c5a1600f4',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
}
response=requests.post(url,form_date)
print(response.text)