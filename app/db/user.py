from fasthtml.common import *
from dataclasses import dataclass

import bcrypt

# Form dataclass, basically the object that is used as standard for the database
@dataclass
class User: name: str; email:str; password:str; gender:bool; # 0 (False) is male, 1 is female 

# Database
db = database("data/staging-users.db")
users = db.create(User, pk="email")

# for u in users():
#     print(u)

GENDER_MEN_STR = "men"
GENDER_WOMAN_STR = "woman"
GENDER_MEN = False
GENDER_WOMAN = True

# User register handling
def register(name: str, email: str, password: str, gender: str):
    gender_value = False
    if gender == GENDER_WOMAN_STR:
        gender_value = GENDER_WOMAN
    elif gender == GENDER_MEN_STR:
        gender_value = GENDER_MEN

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    user = User(name, email, hashed_password, gender_value) 
    users.insert(user)

def fetch(email: str, input_password: str):
    if not email in users:
        return -2 # User has not been registered, does not exist

    user = users[email] # Email is the primary key

    result = bcrypt.checkpw(input_password.encode(), user.password)

    if result == False: # Very secure password
        return -1 # User exists but wrong password
    
    return user