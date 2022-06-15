from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.03isz.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


# 여러개의 리스트를 볼때 이렇게 사용함
# all_users = list(db.users.find({}, {"_id": False})) # "_id": False는 리스트가 나온게 한다.

# for user in all_users:
#     print(user)


# 하나의 list를 보고 싶을때 찝어서 하나를 보고 싶을때 사용하는 법

# user = db.users.find_one({"name": "bobby"})
# print(user)

# 만약 여기서 bobby의 age를 알고싶으면

# print(user["age"])

# bobby가 있는 곳에가서 나이를 19살로 바꿔라고 할때 사용할 수 있는 코드

# db.users.update_one({"name": "bobby"}, {"$set": {"age": 19}})

# db 삭제

# db.users.delete_one({"name": "bobby"}) bobby를 삭제시킴

# PYMONGO 코드요약 - 저장하고 복사해서 사용함
# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})