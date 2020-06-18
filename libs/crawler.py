import requests

def crawl(url):
    resp = requests.get(url)
    print(resp,url)
    return  resp.content #나를 호출한 url에게 resp전체 소스코드를 줌

