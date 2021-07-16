class parkingGarage():


    def __init__(self, tickets, spaces, current_ticket):
        self.tickets = tickets
        self.spaces = spaces
        self.current_ticket = current_ticket


    def addTicket(self):
        temp = self.tickets.pop()
        space = self.spaces.pop()
        self.current_ticket[temp] = "not paid"
        print(f'Your ticket and spot number is {temp}. We will see you when you pay.')


    def payTicket(self):
        user_input = int(input("Input your ticket number? "))
        self.current_ticket[user_input] = "paid"
        print("Thank you for paying, you have 15 minutes to leave. ")


    
    def leaveGarage(self):
        input_ticket = int(input("What is your ticket number? "))
        if self.current_ticket[input_ticket] == "paid":
            print("Thank you, have a nice day")
            self.tickets.append(input_ticket)
            self.spaces.append(input_ticket)
            del self.current_ticket[input_ticket] 
        elif self.current_ticket[input_ticket] != "paid":
            print("You need to pay your ticket before you leave. Please go back and pay for the ticket")


garage = parkingGarage([1,2,3, 7], [1,2,3], {})


def run():
    whole_foods = ShoppingBag(2,10,[])
    while True:
        response = input("What do you want to do? add/show/quit ")
        if response.lower() == 'quit':
            whole_foods.showShoppingBag()
            print("Thank you for shopping at Whole Foods")
            break
        elif response.lower() == 'add':
            whole_foods.addToShoppingBag()
        elif response.lower() == 'show':
            whole_foods.showShoppingBag()
        else:
            print("Not a valid input, please retry, you fucking failure")




garage = parkingGarage([], [], {})