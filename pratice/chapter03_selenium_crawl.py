# * : selenium을 이용해서 페이지를 크롤링


from selenium import webdriver
import time # 예약기능 같은거..

driver = webdriver.Chrome(executable_path='../webdriver/chromedriver.exe')

url ='https://www.instagram.com/explore/tags/%ED%94%BC%EA%B7%9C%EC%96%B4/'
driver.get(url) #  나만의 웹드라이버로 url 페이지 접속
time.sleep(5) # 5초간 기다림/ 콘솔이 먼저 뜨고 사진이 나중에 뜨는데 오래걸림
# sleep하여 창 다 뜨고 난 다음에 콘솔에 보여라
# : 웹드라이버에서 페이지가 완전히 로딩되기 전에 page_source를 가져오기 때문에
# 미완성된 코드로 내용을 수집하는데 한계가 있음 그래서 5초간 시간을 주고 페이지가 전부 로딩되면 그때 소스를 가져오도록 하기위함


page_code =driver.page_source # 해당 url의 전체소스코드 가져오기
print(page_code)
