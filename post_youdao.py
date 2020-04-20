import random
import time
import requests

# url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
# content="我是中国人"

class Youdao():
    def __init__(self,content):
        self.content=content
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()

    def get_salt(self):
        s=str(random.randint(0, 10))
        t=self.ts
        # print("random = ", s)
        # print("ts =", t)
        # print("salt =",t+s)
        return t+s
        # return '15867595017047'
    def get_md5(self,value):
        import hashlib
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        i = self.salt
        e = self.content
        s = "fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        # print("s=",s," md5=",get_md5(s))
        return self.get_md5(s)
        # return 'c40d36905b5e23c8ca0f21ddc885c6da'

    def get_ts(self):
        t = time.time()
        ts = str(int(round(t * 1000)))
        print("ts=", ts)
        return ts
        #'1586759501704'

    # def get_content(self):
    #   return content

    def yield_form_data(self):
        form_data = {
            'i': self.content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': 'b016bfc8dd420bcfc5d5a95c5a1600f4',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
        }
        return form_data

    def get_headers(self):
        headers={
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1208821272@10.108.160.18; OUTFOX_SEARCH_USER_ID_NCOO=113236325.54830773; JSESSIONID=aaas8xpgVwNAZ9B6iwvgx; ___rl__test__cookies=1587348546959',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 81.0.4044.113Safari / 537.36',
        }
        return headers

    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        return response.text

if __name__ ==  '__main__' :
    # print(form_date)
    # print(get_headers())
    youdao=Youdao('我们')
    print(youdao.fanyi())
    # print(response.text)