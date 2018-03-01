from models import Model
import json


class User(Model):
    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.note = form.get('note', '')

    def validate_login(self):
        # f = open(r'F:\weiyundiskDownload\web3\document\db\User.txt')
        # s = f.read(1000)
        # user_dict = json.loads(s)
        # # user_list = list(s)
        # u = self.__class__.form()
        # # dict_str = str(dict)
        # if u in user_dict:
        #     print('ok')
        # else:
        #     print('bu ok')
        us = User.all()
        for u in us:
            if u.username == self.username and u.password == self.password:
                return True
        return False


    def validate_register(self):
        return len(self.username) > 2 and len(self.password) > 2 and len(self.note) > 2

# def main():
#
#     u = User.find_by(password=123)
#     print(u)
#
# if __name__ == '__main__':
#     main()
