from pymongo import *

class gen:
#connect to database 
    def __init__(self): 
        self.conn = pymongo.Connection('host='127.0.0.1',port=27017')
        self.db = self.conn.darma
        self.collection = self.db.health_data

#generate large user data
    def insert_user_data(self, user_num, times):
        for i in range(times):
            for j in range(user_num):
                post = {}
                post['user_id'] = j+1
                post['time'] = datetime.now().isoformat()
                post['data'] = i
                self.collection.save(post) 
