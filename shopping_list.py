# Create shopping list
# Add items to list (one at a time)
# Enter "DONE" to stop adding things
# When stopped print everything in the list
def show_help():
    print("Type SHOW to display what is in your list")
    print("Type DONE to stop adding items to your list")
    print("Type HELP to repeat this help message")
    
def show_list(lst):    
    print("Here is what you need to get: {}".format(", ".join(lst)))
    
def add_to_list(lst, itm):
    lst.append(itm)
    
shopping_list = []
print("Before you go shopping let's make your list...")
show_help()

while True:
    new_item = input(">> ")
    if new_item == "DONE":
        break
    elif new_item == "SHOW":
        show_list(shopping_list)
        continue
    elif new_item == "HELP":
        show_help()
        continue
    add_to_list(shopping_list, new_item)
    
show_list(shopping_list)