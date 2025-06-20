# seed_users.py
from services.db_manager import get_db
from models.user_model import UserModel

if __name__ == "__main__":
    for tenant in ["client1", "client2"]:
        db = get_db(tenant)
        users = UserModel(db)
        users.create_user("john", "pass123")
        users.create_user("alice", "alicepwd")
    print("Seeded users for client1 and client2")
