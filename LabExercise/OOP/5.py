class Bank:
    def __init__(self):
        self.customers = {}
        self.transactions = []

    def CreateCustomer(self, name, amount):
        if name not in self.customers:
            self.customers[name] = amount
            print("Customer Created Successfully")
        else:
            print("Customer with that name already exists")

    def make_transaction(self, from_name, to_name, amount):
        if from_name not in self.customers or to_name not in self.customers:
            print("Invalid customer names")
            return

        if self.customers[from_name] < amount:
            print("Insufficient Balance")
            return

        self.customers[from_name] -= amount
        self.customers[to_name] += amount

        transaction_data = {"from": from_name, "to": to_name, "amount": amount}
        self.transactions.append(transaction_data)
        print("Transaction Successful")

    def SeeMybalance(self, name):
        if name in self.customers:
            print(f"{name} has {self.customers[name]} balance")
        else:
            print(f"Customer '{name}' does not exist")

# Example usage:
babish = Bank()
babish.CreateCustomer("babish", 10000)
babish.CreateCustomer("ram", 10000)

babish.make_transaction("babish", "ram", 1000)

babish.SeeMybalance("babish")
babish.SeeMybalance("ram")