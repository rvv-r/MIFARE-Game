class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def updateStock(self, stock):
        self.stock = stock

    def buyFromStock(self):
        if self.stock == 0:
            # raise not item exception
            pass
        self.stock -= 1



class Distributeur:
    def __init__(self):
        self.amount = 0
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def showItems(self):
        print('\nObjets disponibles \n***************')

        for item in self.items:
            if item.stock == 0:
                self.items.remove(item)
        for item in self.items:
            print(item.name, ":", item.price, "€")

        print('***************\n')

    # def addCash(self, money):
    #     self.amount = self.amount + money

    def buyItem(self, item):
        if self.amount < item.price:
            print('Vous ne pouvez pas acheter cet objet. Insérez plus de pièces.')
        else:
            self.amount -= item.price
            item.buyFromStock()
            print('Vous avez acheté ' +item.name)
            print('Argent restant : ' + str(self.amount))

    def containsItem(self, wanted):
        ret = False
        for item in self.items:
            if item.name == wanted:
                ret = True
                break
        return ret

    def getItem(self, wanted):
        ret = None
        for item in self.items:
            if item.name == wanted:
                ret = item
                break
        return ret

    def insertAmountForItem(self, item):
        price = item.price
        while self.amount < price:
                self.amount = self.amount + float(input('Insérez ' + str(price - self.amount) + ': '))

    def checkRefund(self):
        if self.amount > 0:
            print(self.amount + " rendu.")
            self.amount = 0

        print('Bonne journée !\n')
