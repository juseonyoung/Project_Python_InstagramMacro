# chapter01_crawl.py
# requests로 크롤링하는 부분을 모듈화 하고,
# import해서 사용하는 코드


from libs.crawler import crawl

# 수집하고 싶은 인스타그램의 #해시태그 페이지 url주소
url= 'https://www.instagram.com/explore/tags/%ED%94%BC%EA%B7%9C%EC%96%B4/'

pageString = crawl(url)
print(pageString)

