class Secret_pin():
    def __init__(self,__pin):
        self.__pin = __pin
    def pin_keep(self):
        return self.__pin
print('To know the secret password,enter the owners favourite color')
answer = input('Enter favourite color here: ').lower()
if answer == 'blue':
    p1 = Secret_pin(1496)
    print('Access Granted!')
    print('The secret pin is',p1.pin_keep())
elif answer != 'blue':
    print('Access Denied!')