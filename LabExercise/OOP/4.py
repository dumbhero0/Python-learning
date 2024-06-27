# Write a python program to create a class representing a shopping cart . create  stock as class variable and check for out-of-stack while adding to card . Include methods for adding and removing items , and calculating the total prices for a cart.
class ShoppingCart:
    def __init__(self):
        self.stock = {}  
        self.cart = {}   
        self.items = {}  

    def CheckStock(self, item):
        return self.stock.get(item, 0)

    def AddtoCart(self, item, qty):
        if item in self.cart:
            self.cart[item] += qty
        else:
            self.cart[item] = qty

        if item in self.stock and self.stock[item] >= qty:
            self.stock[item] -= qty
            print("Added to cart")
        else:
            print("Cannot add to cart. Not enough stock.")

    def AddItems(self, item, price, qty):
        if item in self.items:
            self.stock[item] += qty
        else:
            self.items[item] = price
            self.stock[item] = qty

        print("Added  to stock")

    def RemoveItems(self, item):
        if item in self.items:
            del self.items[item]
            del self.stock[item]
            if item in self.cart:
                del self.cart[item]
            print(f"Deleted {item} from stock and cart")
        else:
            print(f"{item} does not exist in stock.")

cart1 = ShoppingCart()

cart1.AddItems("pendrive", 1000, 5)
cart1.AddItems("keyboard", 2000, 3)

print("Stock of pendrive:", cart1.CheckStock("pendrive"))

cart1.AddtoCart("pendrive", 2)
cart1.AddtoCart("keyboard", 1)
cart1.AddtoCart("pendrive", 4)  
cart1.RemoveItems("keyboard")
cart1.RemoveItems("mouse")
