names = ["first nickname", "second nickname"]


class UsersName:

    def __init__(self):
        pass

    @staticmethod
    def get_login(who):
        if who:
            return names[0]
        return names[1]

    @staticmethod
    def set_login(who, nickname):
        if who:
            names[0] = nickname
        else:
            names[1] = nickname
