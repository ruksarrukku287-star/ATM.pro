class Phone:
    def __init__(self,balance):
        self.__balance=balance
    def get__balance(self):
        return self.__balance
Ph=Phone(349)
print(Ph.get__balance())
