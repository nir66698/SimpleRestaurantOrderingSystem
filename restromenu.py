# Define the menu of the resturant
menu = {
    'Prawn pie':60,
    'Italian macaroni':80,
    'paneer steak':50,
    'coffee':70,
    'lemonade':30,
}
#greet
print("Welcome to Our Resturant")
print("Here's our Menu for placing your order")
print("Prawn pie: Rs60\nItalian macaroni: Rs80\nPaneer steak: 50\nCoffee: Rs70\nLemonade: Rs30 ")

order_total = 0

item_1 = input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 70
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not avaliable in our resturant!!")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not avaliable!")

print(f"The total amount to be paid is Rs{order_total}")
print(f"Thank you for the visit!!")