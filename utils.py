import requests

#创建工具类
class SessionUtil:
    #置空
    __session = None
    #创建session对象，并返回
    @classmethod
    def get_session(cls):
        if cls.__session is None:
            cls.__session = requests.session()
        return cls.__session

    #关闭session对象，并置空
    @classmethod
    def close_session(cls):
        if cls.__session is not None:
            cls.__session.close()
            cls.__session = None
