# eel-example
Just a basic example of using the "Eel" library. 
This example makes a simple insertion and removal of values in a NoSQL database, just to demonstrate the communication between Javascript and the backend written in Python. For this is being used the framework "Bootstrap4" and the "Jquery" library for the frontend, and the non-relational database "MongoDb".

# What is Eel ?
"Eel is a little Python library for making simple Electron-like offline HTML/JS GUI apps, with full access to Python capabilities and libraries. It hosts a local webserver, then lets you annotate functions in Python so that they can be called from Javascript, and vice versa. It is designed to take the hassle out of writing short and simple GUI applications."

For more information, click [here](https://github.com/ChrisKnott/Eel) (repository link)

# Installation

### Install MongoDB:

[MongoDB Installation](https://docs.mongodb.com/manual/installation/?jmp=footer&_ga=2.168173224.803608867.1506133999-480232443.1506015152)

### Clone repository:

```bash
$ git clone https://github.com/ViniciusRomano/eel-example.git
$ cd eel-example
```

### Install requirements:

```bash
$ pip install -r requirements.txt
```

# Run
Copy and paste the following line into a terminal window.
```bash
$ python run.py
```

# 其他参考
[html技术构建python桌面程序-利用eel](https://mlln.cn/2018/11/09/html%E6%8A%80%E6%9C%AF%E6%9E%84%E5%BB%BApython%E6%A1%8C%E9%9D%A2%E7%A8%8B%E5%BA%8F-%E5%88%A9%E7%94%A8eel/#Eel%E7%AE%80%E4%BB%8B)

# 生成requirements.txt

pip freeze > requirements.txt

