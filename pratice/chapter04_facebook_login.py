# selenium 이용해서 페북 로그인
# 지속적으로 사용 불가능.. 페이스북이 보안을 위해 로그인버튼의
# 선택자를 수시로 변경함

from selenium import webdriver

# selenium을 사용해서 페북에 로그인
# 로그인버튼은 보안조치 때문에 id가 자꾸 변동

path ='..' # 상대주소가 다 다르기 때문에 이렇게 하면 편함
driver = webdriver.Chrome(executable_path='{}/webdriver/chromedriver.exe'.format(path))

url ='https://www.facebook.com/'
driver.get(url) #  나만의 웹드라이버로 url 페이지 접속

driver.find_element_by_id('email').send_keys('아이디 입력(이메일형식)') #아이디가 이메일인것 찾아라
driver.find_element_by_id('pass').send_keys('비밀번호입력')
driver.find_element_by_id('u_0_e').click() # 로그인 버튼 ID값이 수시로 변경