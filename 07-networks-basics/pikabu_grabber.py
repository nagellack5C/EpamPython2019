import requests
import pikabu_headers
import time

class PikabuGrabber:
    PKB_GET_HEADERS = pikabu_headers.PKB_GET_HEADERS
    HEADERS_LOGIN = pikabu_headers.HEADERS_LOGIN_2
    HOME = "https://pikabu.ru"

    def __init__(self, username, password):
        self.session = requests.Session()
        # self.session.headers = self.PKB_GET_HEADERS
        self.get_main()
        self.auth(username, password)

    def get_main(self):
        get = self.session.get(self.HOME)
        # print(get.text)
        # print(self.session.cookies)
        self.csrf = get.text.split('"sessionID":"')[1].split('","')[0]

    def auth(self, username, password):
        data = pikabu_headers.LOGIN_PAYLOAD

        self.session.headers = self.HEADERS_LOGIN
        self.session.headers["x-csrf-token"] = self.csrf
        print("posting auth...")
        post = self.session.post("https://pikabu.ru/ajax/auth.php",
                                 data=data)
        print(post.text)
        print(post.cookies)
        print(self.ppd(post.request.headers))
        # self.session.headers.update(self.PKB_GET_HEADERS)
        self.session.headers = self.PKB_GET_HEADERS
        print(self.session.cookies)
        time.sleep(2)
        print("auth posted! getting page...")
        # print(self.session.cookies)
        if "dasgeschaft" in self.session.get(self.HOME).text:
            print("Success!")
        else:
            print("da yebaniy v rot blya")
        # print(self.session.get(self.HOME).text)

    @staticmethod
    def ppd(dict):
        for i in dict:
            print(f"{i}: {dict[i]}")


pg = PikabuGrabber("test", "test")
# pg.test()
# print(pg.HEADERS_LOGIN)
