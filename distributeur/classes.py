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

class Solde:
    def __init__(self):
        self.amount = 30

class Distributeur:
    def __init__(self):
        self.items = []
        self.solde = Solde().amount

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
        if self.solde < item.price:
            print('Vous ne pouvez pas acheter cet objet. Insérez plus de pièces.')
        else:
            self.solde -= item.price
            item.buyFromStock()
            print('Vous avez acheté ' +item.name)
            print('Argent restant : ' + str(self.solde))

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
        while self.solde < price:
                self.solde = self.solde + float(input('Insérez ' + str(price - self.solde) + ': '))

    def checkRefund(self):
        if self.solde > 0:
            print(str(self.solde) + "€ rendu.")
            self.solde = 0

        print('Bonne journée !\n')
