from pymongo import MongoClient


class MongoDAO: # 파이썬은 객체 만들때 두줄을 띄워조야함 class윗부분
    reply_list = [] # MongoDB Document를 담을 List 선언

    def __init__(self):
        # >> MongoDB Connection
        # 객체를 생성할때 하는 일들을 넣어줌. #커넥션 맺는거를 init생성자 블록에 넣어준거임
                                # 아이피주소, 포트번호
        self.client = MongoClient('127.0.0.1', 27017) # 클래스 객체 할당(ip, Port)

        # 몽고디비안에있는 local안에 movie를 사용하겠다 (무비에다가 저장해놓을것이여서구체적으로)
        # 위치를 상세히 구체적으로 저장해놔야지 내가 어디서 가져오고 저장할건지 알 수 있음.
        self.db = self.client['local'] # MongoDB의 'local' DB를 할당
        self.collection = self.db.get_collection('movie') # 동적으로 Collection 선택 // 여기까지 주석임 13,14번


        # 타입은 파이썬의 딕셔너리 타입으로 저장해야하기때문에
        # 다음무비페이지에 딕셔너리 타입으로 변형해서 data 변수에 저장함.
        # MongoDB에 Insert

    def mongo_write(self, data):
        print('>> MongoDB WRITE DATA:)')
        self.collection.insert(data) # JSON Type = Dict Type(Python)


        # MongoDB에서 SelectAll
    def mongo_select_all(self):
        for one in self.collection.find({}, {'_id':0,'content':1,'score':1}):
            self.reply_list.append([one['title'], one['content'],one['score']]) # dict에서 Value와 Score만 추출
        return self.reply_list