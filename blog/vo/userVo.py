class User:
    def __init__(self):
        self.user_id = None
        self.user_pwd = None

    #get set 메서드

    def getUserId(self):
        return self.user_id

    def setUSerId(self, user_id):
        self.user_id = user_id

    def getUserPwd(self):
        return self.user_pwd

    def setUSerPwd(self, user_pwd):
        self.user_pwd = user_pwd