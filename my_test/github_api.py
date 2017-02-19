# -*- coding:utf-8 -*-

import json
import requests



def build_url(url,endpoint):
    return '/'.join([url,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def requests_method(url,endpoint):
    new_url = build_url(url,endpoint)
    # res = requests.get(new_url,auth=('zhangguo7@aliyun.com','951753zgq'))
    res = requests.get(new_url)
    print(better_print(res.text))

if __name__ == '__main__':
    url = 'https://api.github.com'
    requests_method(url,'users/zhangguo7')