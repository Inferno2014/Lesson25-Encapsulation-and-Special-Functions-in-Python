class Computer():
    price = 1000
    def __init__(self,price,__max_price):
        self.__max_price = __max_price
        self.price = price
    def print_sell(self):
        return('The original price was',self.price)
    def update_sell(self):
        return self.__max_price
    def updated_sell(self):
        return('The updated price is',self.__max_price)
c1 = Computer(1000,1250)
print(c1.print_sell())
print(c1.updated_sell())