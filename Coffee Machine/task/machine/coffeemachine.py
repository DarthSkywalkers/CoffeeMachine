class CoffeeMachine:

    supply_name = ["water", "milk", "coffee beans", "disposable cups", "money"]
    supply_name_fill = ["water", "milk", "coffee beans", "coffee"]
    units_fill = ["ml", "ml", "grams", "disposable cups"]
    menu = ["espresso", "latte", "cappuccino"]
    menu_supplies = [[250, 0, 16, 1, -4], [350, 75, 20, 1, -7], [200, 100, 12, 1, -6]]
    supply_amount = None
    fill_item_no = None
    state = None

    def __init__(self):
        self.state = "choose action"
        self.supply_amount = [400, 540, 120, 9, 550]

    def choose_action(self, command=None):
        if self.state == "choose action":
            self.choosing_action()
        elif self.state == "make action":
            self.make_action(command)
        elif self.state == "buy" or self.state == "coffee chosen":
            self.buy(command)
        elif self.state == "take":
            self.take()
        elif self.state == "fill":
            self.fill(command)
        elif self.state == "remaining":
            self.remaining()

    def main_menu(self):
        self.state = "choose action"
        self.choose_action()

    def choosing_action(self):
        print("Write action (buy, fill, take, remaining, exit):")
        self.state = "make action"

    def set_state(self, new_state):
        if new_state is not None:
            self.state = new_state

    def make_action(self, command):
        if command is not None:
            self.set_state(command)
            self.choose_action()

    def remaining(self):
        step = 0
        print("The coffee machine has:")
        while step < len(self.supply_name):
            sign = ""
            if self.supply_name[step] == "money":
                sign = "$"
            print(f"{sign}{str(self.supply_amount[step])} of {self.supply_name[step]}")
            step += 1
        print()
        self.main_menu()

    def buy(self, command=None):
        if self.state == "buy":
            print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            self.state = "coffee chosen"
        elif self.state == "coffee chosen":
            if command == "back":
                print()
                self.main_menu()
            else:
                self.check_supplies(int(command) - 1)
                self.main_menu()

    def check_supplies(self, coffee_type):
        max_steps = len(self.supply_amount)
        for i in range(max_steps):
            if self.supply_amount[i] < self.menu_supplies[coffee_type][i]:
                print(f"Sorry, not enough {self.supply_name[i]}!\n")
                break
        else:
            print("I have enough resources, making you a coffee!\n")
            self.use_supply(coffee_type)

    def use_supply(self, coffee_type):
        step = 0
        while step < len(self.menu_supplies[coffee_type]):
            self.supply_amount[step] -= self.menu_supplies[coffee_type][step]
            step += 1

    def fill(self, command=None):
        if self.fill_item_no is None:
            self.fill_item_no = 0
        elif self.fill_item_no in range(5):
            self.supply_amount[int(self.fill_item_no) - 1] += int(command)
        if self.fill_item_no in range(4):
            print(f"Write how many {self.units_fill[self.fill_item_no]} "
                  f"of {self.supply_name_fill[self.fill_item_no]} do you want to add:")
        if self.fill_item_no < len(self.supply_name_fill):
            self.fill_item_no += 1
        else:
            print()
            self.fill_item_no = None
            self.main_menu()

    def take(self):
        print(f"I gave you ${self.supply_amount[4]}\n")
        self.supply_amount[4] = 0
        self.main_menu()


coffee = CoffeeMachine()
user_input = None
first_run = 1
while True:
    if user_input != "exit":
        if first_run == 1:
            first_run = None
        else:
            user_input = input()
        coffee.choose_action(user_input)
    else:
        break
