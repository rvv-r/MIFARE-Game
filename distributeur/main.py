from classes import *

def vend():

    machine = Distributeur()
    item1 = Item('Coca',  2,  2)
    item2 = Item('Evian', 1,  1)
    item3 = Item('Ice Tea',  1.5,  3)
    item4 = Item('Sprite',  2, 1)
    machine.addItem(item1)
    machine.addItem(item2)
    machine.addItem(item3)
    machine.addItem(item4)

    print('Bienvenue sur le distributeur!\n***************')

    continueToBuy = True
    while continueToBuy == True:
        machine.showItems()
        selected = input('Sélectionnez un objet à acheter : ')
        if machine.containsItem(selected):
            item = machine.getItem(selected)

            machine.insertAmountForItem(item)
            machine.buyItem(item)

            a = input('Acheter quelquechose d\'autre? (y/n): ')
            if a == 'n':
                continueToBuy = False
                machine.checkRefund()
            else:
                continue

        else:
            print('Objet non disponible. Sélectionnez un autre objet.')
            continue

vend()
