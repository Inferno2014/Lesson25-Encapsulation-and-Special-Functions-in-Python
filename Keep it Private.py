class my_class():
    age = 13
    __privateVar = 435
    def __privmeth(self):
        print("I'm inside class myClass")
    def hello(self):
        return self.__privateVar
#not allowed: print(my_class.__privateVar)
print(my_class().hello())
#print(my_class._my_class__privateVar)