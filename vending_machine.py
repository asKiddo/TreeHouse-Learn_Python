drink = ['Water', 'Gatorade', 'Orange Juice', 'Apple Juice']
snack = ['Pretzels', 'Almonds', 'Trail Mix']
sweet = ['Chocolate Bar', 'Cookie']

while True:
    choice = input("Would you like a drink, a snack, or a sweet?\n").lower()
    
    try:
        if choice == 'drink':
            vend = drink.pop()
        elif choice == 'snack':
            vend = snack.pop()
        elif choice == 'sweet':
            vend = sweet.pop()
        elif choice == 'quit':
            break
        else:
            print("Sorry I don't know what you want.")
            continue
    except IndexError:
        print("We're all out of {}s :(".format(choice))
    else:
        print("Here's your {}: {}".format(choice, vend))