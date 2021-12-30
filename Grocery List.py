shopping_list = []

def show_help():
    print("What should we pic up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' to print your current list.""")

def add_to_list(item):
    shopping_list.append(item)
    print("'{}' has been added to your shopping list. There are now".format(item), len(shopping_list), "items on your list")

def show_list():
    print("Shopping List:")
    for item in shopping_list:
        print("* " + item)

show_help()
while True:
    new_item = input("> ")

    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    # Enable the SHOW command to show the list. Don't forget to update the HELP documentation.
    elif new_item == "SHOW":
        show_list()
        continue

    add_to_list(new_item)
show_list()

