# 해시태그 피드에 좋아요와 댓글을 반복적으로 다는 프로그램

from  selenium import webdriver
import  time, random
from bs4 import BeautifulSoup

# 1. 크롬 드라이버 setup
path ='..' # 상대주소가 다 다르기 때문에 이렇게 하면 편함
driver = webdriver.Chrome(executable_path='{}/webdriver/chromedriver.exe'.format(path))


# 2. 인스타그램 로그인
url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
driver.get(url)
time.sleep(3)

# what is wpath?
# : Xpath는 W3C의 표준으로 확장 생성언어 문서의 구조를 통해 경로 위에 저장한 구문을 사용하여
# 항목을 배치하고 처리하는 방법을 기술하는 언어이다.

# div[1]이 첫번째임
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys("")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys("")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click() #로그인버튼은 input아님


# 3.hashtag searching
time.sleep(2)
hash_url='https://www.instagram.com/explore/tags/%EB%A6%AC%EC%A7%93%EA%B5%B0%EC%A6%88/'
driver.get(hash_url)

# 4. 게시물 가져오기
def parse(page_code):
    soup = BeautifulSoup(page_code, 'html.parser')
    feed_list = soup.findAll('div', {'class', 'v1Nh3'})# class값은 수시로 변경됨
    print('Feed Cnt:', len(feed_list))

    links = []
    for one in feed_list:
        insta_link = 'https://www.instagram.com'
        link_addr = one.find('a')['href']
        print(insta_link + link_addr)
        links.append(insta_link + link_addr)

    return links

time.sleep(4)
page_code = driver.page_source
links = parse(page_code)
print('Feed Cnt:', len(links))

# 좋아요 누르고 댓글달기
for url in links:
    try:
        driver.get(url)

        rnd_sec=random.randint(5,15)
        time.sleep(rnd_sec)
        message = 'GTA!!'

        #좋아요
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()

        # 댓글
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').click()
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').send_keys(message)
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/button').click()
    except Exception as e:
        print(e)




