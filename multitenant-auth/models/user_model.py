# models/user_model.py
class UserModel:
    def __init__(self, db):
        self.collection = db["users"]

    def create_user(self, username, password):
        if self.collection.find_one({"username": username}):
            return False
        self.collection.insert_one({"username": username, "password": password})
        return True

    def get_user(self, username):
        return self.collection.find_one({"username": username})
