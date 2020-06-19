

# 영화 야구소녀

import requests
from bs4 import BeautifulSoup
import test.movie.persistence.MongoDAO as DAO

mDao = DAO.MongoDAO()

cnt = 0
for page in range(1,6):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=189633&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(page)

    resp = requests.get(url)

    if resp.status_code != 200:
        print('존재하지 않는 URL')

    soup = BeautifulSoup(resp.text, 'html.parser')

    reply_list = soup.select('div.score_result li')

    for reply in reply_list :
        contents = reply.select('div.score_reple > p > span')[0].text.strip()
        previous_writer = reply.select('div.score_reple a > span')[0].text.strip()
        cut_index = previous_writer.find('(')

        if cut_index > 0:
            writer = previous_writer[:cut_index]
        else:
            writer = previous_writer

        score = reply.select('div.star_score em')[0].text.strip()
        reg_dt = reply.select('div.score_reple em')[1].text[11:]

        cnt += 1
        print('■■■■■■게시글 {} ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'.format(cnt))
        print('내용:',contents)
        print('작성자:',writer)
        print('평점:',score)
        print('작성일자:',reg_dt)

        data = {'contents':contents,
                'writer':writer,
                'score':score,
                'reg_dt':reg_dt}

        mDao.mongo_write(data)

print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')