# selenium 의 webdriver사용방법 (+chrome driver)

from selenium import webdriver

# 인스타그램 페이지에서 원하는 해쉬태그로 selenium 접속(+크롬 드라이버)
# 내 위치로부터 찾아감 =상대주소
driver = webdriver.Chrome(executable_path='../webdriver/chromedriver.exe')

# url주소의 한글은 유니코드로 변환(한글이면 깨지는 경우가 있음)
url ='https://www.instagram.com/explore/tags/%ED%94%BC%EA%B7%9C%EC%96%B4/'
driver.get(url)

# 드라이버 끄는 코드
# driver.close()