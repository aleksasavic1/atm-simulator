import abc

class EventListener:
    def limit_reached(self, sender):
        pass

class ATM:
    def __init__(self, balance):
        self.balance = balance
        self.limit = 20
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def remove_listener(self, listener):
        self.listeners.remove(listener)

    def distribute_event(self):
        for listener in self.listeners:
            if isinstance(listener, EventListener):
                listener.limit_reached(self)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} USD! Current balance: {self.balance} USD.")
        else:
            print(f"Not enough money! Current balance: {self.balance} USD.")

        if self.balance <= self.limit:
            self.distribute_event()

class MyListener(EventListener):
    def limit_reached(self, sender):
        print("Alert! There isn't much money remaining on your card.")


if __name__ == "__main__":
    while True:
        try:
            input_balance = int(input("Enter the amount of money you want to deposit: "))
            break
        except ValueError:
            print("Please enter the number!")
            continue
    atm = ATM(input_balance)

    atm.add_listener(MyListener())

    while atm.balance > 0:
        try:
            atm.withdraw(int(input("Enter the amount of money you want to withdraw: ")))
        except ValueError:
            print("Please enter the number!")
            continue
    else:
        print("You have no more money on the card.")
