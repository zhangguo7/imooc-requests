# -*- coding:utf-8 -*-
# 带参数的请求
import requests

if __name__ == '__main__':
    search_words = '美女'
    url = 'http://www.sina.com.cn/mid/search.shtml'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    params = {'range': 'all',
              'c': 'news',
              'q': '%s' % search_words,
              'from': 'home',
              'ie': 'utf-8'}

    res = requests.get(url,headers=headers,params=params)
    print(res.request.headers)
    print(res.url)

