class Store():
    def __init__(self):
        self.inventory = {
            "Milk": [2.75, 7],
            "Bread": [4.99, 4], 
            "Cheddar Cheese": [3.49, 10], 
            "Eggs": [1.99, 25],
            "Butter": [1.50, 15], 
            "Broccoli": [1.79, 20], 
            "Oranges": [3.00, 15], 
            "Apples": [2.00, 35]
        }
        self.cash_register = {
            20: 10, 
            10: 20, 
            5: 50, 
            1: 100, 
            .25: 30, 
            .10: 50, 
            .05: 40, 
            .01: 100
        }

    #The List of Products in Store
    def __str__(self):
        return f'{self.inventory}, {self.cash_register}'

class Payment(Store):
    def __init__(self):
        super().__init__()

    # Function for the shopper to buy a product by entering the product name and quantity wanted
    # checks if it is in stock and then returns the total price
    def transaction(self, item, quantity):
        global total_p
        if quantity <= self.inventory[item][1]:
            total_p = quantity*self.inventory[item][0]
            total_p_format = "${:.2f}".format(total_p)
            print("Your total is", total_p_format)
        else:
            raise ValueError("Not enough in stock")

    #Function that allows the user to enter the bills and/or coins they want to use to pay
    #If they are finished entering the bills and coins, they enter 0 for both
    #The function will print out a dictionary of the money they entered
    def pay(self):
        global money_given
        money_given = {}
        money = float(input("Enter bill or coin: "))
        m_q = int(input("Enter quantity of that bill or coin: "))
        money_given.update({money: m_q})
        while(money > 0):
            money = float(input("Enter bill or coin, (enter 0 if done): "))
            m_q = int(input("Enter quantity of that bill or coin, (enter 0 if done): "))
            if money > 0:
                money_given.update({money: m_q})
        print("Money given : ", money_given)
        return money_given

class Updater(Store):
    def __init__(self):
        super().__init__()

    # Function to update cash register after shopper pays
    def new_cash(self):
        for bill in money_given:
            self.cash_register[bill] += money_given[bill]
        print("Cash Register was updated: ")
        return self.cash_register

    # Function adds up the money given by the shopper and then outputs the total given and what the change is
    def total(self):
        global total_given
        global change_needed
        change_needed = 0
        total_given = 0
        for bill in money_given:
            total_given += bill * money_given[bill]
        total_given_str = "${:.2f}".format(total_given)
        print("Total amount entered is", total_given_str)
        change_needed = total_given - total_p
        change_needed_str = "${:.2f}".format(change_needed)
        print("Your change is", change_needed_str)
        return round(change_needed, 2)

class Change(Store):
    def __init__(self):
        super().__init__()

    # Function that computes the specific bills and coins the shopper will get in change
    def change_given(self, change_needed):
        global change_received
        change_received = {}
        for key in self.cash_register:
            c_q = 0
            while key < change_needed or key == change_needed:
                c_q += 1
                change_needed = change_needed - key
                self.cash_register[key] -= 1
                change_received.update({key: c_q})
        print("Change in bills/coins: ", change_received)
        return change_received

    # Function that updates cash register after change is given to the shopper
    def cash_after_change(self):
        balance = 0
        for bill in change_received:
            self.cash_register[bill] -= change_received[bill]
        for key in self.cash_register:
            balance += key * self.cash_register[key]
        print(balance)
        print(self.cash_register)
        return self.cash_register
