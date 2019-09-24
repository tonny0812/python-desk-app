from random import random

import eel

def mongo_init():  # Local function
    global user

    # client = MongoClient('localhost', 27017)
    # db = client.eel_database
    # user = db.users
    user = [
        {
            "email": "user1@1.com",
            "password": "123"
        },
        {
            "email": "user1@1.com",
            "password": "123"
        } ]


@eel.expose  # Eel function
def set_title():  # Example to send data for javascript/html
    return "Code example - Eel + Bootstrap 4 + MongoDb"

# 这是一个回调函数
def print_num(n):
    print('Got this from Javascript:', n)

@eel.expose  # Eel function
def save_user(email, password):
    dict_user = {"email": email, "password": password}
    # user.insert_one(dict_user).inserted_id
    user.append(dict_user)
    print('Calling Javascript...')
    eel.my_javascript_function(1, 2, 3, 4)(print_num)  # This calls the Javascript function
    # 同步返回
    # 在python端, 我们只要不使用回调函数就能同步返回:
    n = eel.js_random()()  # 这里有两个括号
    print('Got this from Javascript:', n)

@eel.expose
def py_random():
    return random()

@eel.expose  # Eel function
def drop_database():
    # client = MongoClient('localhost', 27017)
    # client.drop_database('eel_database')
    pass


@eel.expose  # Eel function
def get_users():
    # all_users = []
    # cursor = user.find({})
    # for x in cursor:
    #     x.pop("_id")  # Remove objects id
    #     all_users.append(x)
    # return all_users
    return user


if __name__ == '__main__':
    eel.init('web')  # Give folder containing web files
    mongo_init()  # Init mongodb

    web_app_options = {
        'mode': "chrome-app",  # or "chrome"
        'port': 8080,
        'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
    }

    eel.start('index.html', size=(800, 600), options=web_app_options)  # Start


