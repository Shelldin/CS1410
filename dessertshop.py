from dessert import Candy, Cookie, IceCream, Sundae, Order
from receipt import make_receipt
from payable import PayType


class DessertShop:
    customer_db: dict[str, 'Customer'] = {}
    def get_positive_float(self, input_text):
        while True:
            try:
                value = float(input(input_text))
                if value < 0:
                    raise ValueError
                return value
            except ValueError:
                print("Input invalid. Please enter a positive number.")

    def get_positive_int(self, input_text):
        while True:
            try:
                value = int(input(input_text))
                if value < 0:
                    raise ValueError
                return value
            except ValueError:
                print("Input invalid. Please enter a positive whole number.")

    def user_prompt_candy(self):
        name = input("Enter the type of candy: ")
        candy_weight = self.get_positive_float("Enter number of pounds: ")
        price_per_pound = self.get_positive_float("Enter price per pound: ")
        return Candy(name, candy_weight, price_per_pound)

    def user_prompt_cookie(self):
        name = input("Enter the type of cookie: ")
        cookie_quantity = self.get_positive_int("Enter the number of cookies: ")
        price_per_dozen = self.get_positive_float("Enter the price per dozen: ")
        return Cookie(name, cookie_quantity, price_per_dozen)

    def user_prompt_icecream(self):
        name = input("Enter the type of ice cream: ")
        scoop_count = self.get_positive_int("Enter the number of scoops: ")
        price_per_scoop = self.get_positive_float("Enter the price per scoop: ")
        return IceCream(name, scoop_count, price_per_scoop)

    def user_prompt_sundae(self):
        name = input("Enter the type of sundae: ")
        scoop_count = self.get_positive_int("Enter the number of scoops: ")
        price_per_scoop = self.get_positive_float("Enter the price per scoop: ")
        topping_name = input("Enter the type of topping: ")
        topping_price = self.get_positive_float("Enter the price of the topping: ")
        return Sundae(name, scoop_count, price_per_scoop, topping_name, topping_price)

    def user_prompt_pay_type(self):
        prompt = '\n'.join(['\n',
                            '1: CASH',
                            '2: CARD',
                            '3: PHONE',
                            '\nHow would you like to pay? (1-3): '])
        while True:
            choice = input(prompt)
            if choice == '1':
                return PayType.CASH
            elif choice == '2':
                return PayType.CARD
            elif choice == '3':
                return PayType.PHONE
            else:
                print('Invalid input. Please select 1, 2 , or 3')


class Customer:
    id = 0

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.order_history: list[Order] = []
        Customer.id += 1
        self.customer_id = Customer.id

    def add2history(self, order: Order) -> 'Customer':
        self.order_history.append(order)
        return self

    def get_total_orders(self):
        return len(self.order_history)


def admin_module(shop: DessertShop):
    while True:
        admin_prompt = '\n'.join(['\nAdmin Module: ',
                                  '1: Shop Customer List',
                                  '2 Customer Order History',
                                  '3: Best Customer',
                                  '4: Exit Admin Module',
                                  '\nWhat would you like to do? (1-4): '])

        choice = input(admin_prompt)
        match choice:
            case '1':
                print("\nShop Customer List: ")
                for customer_name, customer in shop.customer_db.items():
                    print(f"Customer Name: {customer_name}, Customer ID: {customer.customer_id}")

            case '2':
                customer_name = input("Enter customer name: ").strip()
                if customer_name in shop.customer_db:
                    customer = shop.customer_db[customer_name]
                    print(f"\nOrder History for {customer_name}")
                    for order in customer.order_history:
                        print(order)
                else:
                    print(f"{customer_name} not in database.")

            case '3':
                best_customer = max(shop.customer_db.values(), key=lambda c: len(c.order_history))
                print(f"Best Customer: {best_customer.customer_name}"
                      f" with {len(best_customer.order_history)} orders.")

            case '4':
                break

            case _:
                print("Invalid input. Please enter a valid choice (1-4)")


def main():
    shop = DessertShop()

    while True:
        order = Order()

        receipt_data = [["Name", "Quantity", "Unit Price", "Item Cost", "Tax"]]
        '''
        order.add(Candy('Candy Corn', 1.5, .25))
        order.add(Candy("Gummy Bears", .25, .35))
        order.add(Cookie("Chocolate Chip", 6, 3.99))
        order.add(IceCream("Pistachio", 2, .79))
        order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
        order.add(Cookie("Oatmeal Raisin", 2, 3.45))
        '''

        # boolean done = false
        done: bool = False
        # build the prompt string once
        prompt = '\n'.join(['\n',
                            '1: Candy',
                            '2: Cookie',
                            '3: Ice Cream',
                            '4: Sundae',
                            '5: Admin Module',
                            '\nWhat would you like to add to the order? (1-4, Enter for done): '
                            ])

        while not done:
            choice = input(prompt)
            match choice:
                case '':
                    done = True
                case '1':
                    item = shop.user_prompt_candy()
                    order.add(item)
                    print(f'{item.name} has been added to your order.')
                case '2':
                    item = shop.user_prompt_cookie()
                    order.add(item)
                    print(f'{item.name} has been added to your order.')
                case '3':
                    item = shop.user_prompt_icecream()
                    order.add(item)
                    print(f'{item.name} has been added to your order.')
                case '4':
                    item = shop.user_prompt_sundae()
                    order.add(item)
                    print(f'{item.name} has been added to your order.')
                case '5':
                    admin_module(shop)
                case _:
                    print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')

        if choice != '5':
            customer_name = input("Enter customer name: ").strip()
            if customer_name not in shop.customer_db:
                shop.customer_db[customer_name] = Customer(customer_name)

        customer = shop.customer_db[customer_name]
        customer.add2history(order)

        receipt_data.append([f"Customer Name: {customer.customer_name}", "", "", "", ""])
        receipt_data.append([f"Customer ID: {customer.customer_id}", "", "", "", ""])
        receipt_data.append([f"Total Orders: {customer.get_total_orders()}", "", "", "", ""])

        #
        # add your code below here to print the PDF receipt as the last thing in main()
        #

        payment_type = shop.user_prompt_pay_type()
        order.set_pay_type(payment_type)

        for dessert_item in order.order:
            # print(dessert_item.name)
            if isinstance(dessert_item, Candy):
                receipt_data.append([f"{dessert_item.name} ({dessert_item.packaging})", f"{dessert_item.candy_weight}lb(s)",
                                     f"{dessert_item.price_per_pound}/lb",
                                     dessert_item.calculate_cost(), dessert_item.calculate_tax()])
            elif isinstance(dessert_item, Cookie):
                receipt_data.append(
                    [f"{dessert_item.name} ({dessert_item.packaging})", f"{dessert_item.cookie_quantity} cookie(s)",
                     f"{dessert_item.price_per_dozen}/dozen",
                     dessert_item.calculate_cost(), dessert_item.calculate_tax()])
            elif isinstance(dessert_item, Sundae):
                receipt_data.append(
                    [f"{dessert_item.name} ({dessert_item.packaging})", f"{dessert_item.scoop_count} scoop(s)",
                     f"{dessert_item.price_per_scoop}/scoop",
                     dessert_item.calculate_cost(), dessert_item.calculate_tax()])
                receipt_data.append([f"---{dessert_item.topping_name}", "", f"{dessert_item.topping_price}", "", ""])
            elif isinstance(dessert_item, IceCream):
                receipt_data.append(
                    [f"{dessert_item.name} ({dessert_item.packaging})", f"{dessert_item.scoop_count} scoop(s)",
                     f"{dessert_item.price_per_scoop}/scoop",
                     dessert_item.calculate_cost(), dessert_item.calculate_tax()])

        # print(f"Number of items in order: {len(order)}")

        order.sort()

        subtotal = order.order_cost()
        tax_total = order.order_tax()
        cost_total = round((subtotal + tax_total), 2)

        receipt_data.append(["---------", "---------", "---------", "---------", "----------"])
        receipt_data.append(["Total items in order", len(order), "", "", "", ])
        receipt_data.append(["Order Subtotals", "", "", subtotal, tax_total])
        receipt_data.append(["Order Total", "", "", cost_total, ""])
        receipt_data.append([f"Paid with {order.get_pay_type().name}", "", "", "", ""])

        make_receipt(receipt_data, "receipt.pdf")

        string_receipt = [f"Customer Name: {customer.customer_name}", f"Customer ID: {customer.customer_id}",
                          f"Total Orders: {customer.get_total_orders()}", order.__str__()]

        print("\n".join(string_receipt))

        new_order_prompt = input("Would you like to start another order?\n"
                                 "(Enter 'y' for yes or any other key for no): ").strip().lower()
        if new_order_prompt != 'y':
            print("Thanks for shopping!")
            break


if __name__ == "__main__":
    main()
