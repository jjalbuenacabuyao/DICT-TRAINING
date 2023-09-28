grocery_list = list[str]


def print_grocery_items() -> None:
    """
    Print the items in the grocery list.
    """
    if grocery_list == []:
        print("There is no item in the grocery list.")
    else:
        print("Grocery list:")
        for i in range(len(grocery_list)):
            print(f"Item #{i + 1}: {grocery_list[i]}")


while True:
    print(
        """
MENU:
1 - Print the Grocery list
2 - Add the item to the Drocery list
3 - Remove an item in Grocery List
4 - Exit
    """
    )

    command = input("Enter command: ")

    if command == "1":
        print_grocery_items()

    elif command == "2":
        item_to_be_added = input("Enter an item to add on the Grocery list: ").title()
        if not item_to_be_added in grocery_list:
            grocery_list.append(item_to_be_added)
            print(f"{item_to_be_added} added to the list")
        else:
            print(f"{item_to_be_added} is already in the list.")

    elif command == "3":
        item_to_be_removed = input("Enter the item that you want to remove: ").title()
        if item_to_be_removed in grocery_list:
            grocery_list.remove(item_to_be_removed)
            print(f"{item_to_be_removed} removed from the list")
        else:
            print(f"{item_to_be_removed} is not on the list.")

    elif command == "4":
        break

    else:
        print("Invalid command")
