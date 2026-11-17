print("Welcome to the Fantasy Item Shop!")
player_name = input("What is your name? ")

player_gold = 100
inventory = []
shop_items = ['Sword', 'Shield', 'Potion', 'Bow']
prices = {'Sword': 50, 'Shield': 40, 'Potion': 20, 'Bow': 60}

print()
print(f"Hello {player_name}! You have {player_gold} gold.")

while True:
    print()
    print("=== Fantasy Item Shop ===")
    i = 1
    for item in shop_items:
        print(f"{i}. Buy {item} ({prices[item]} gold)")
        i += 1
    print("5. View Inventory")
    print("6. Exit Shop")

    print()
    choice = input("What would you like to do? ")
    item_to_buy = ""

    if choice == "1":
        item_to_buy = shop_items[0]
    elif choice == "2":
        item_to_buy = shop_items[1]
    elif choice == "3":
        item_to_buy = shop_items[2]
    elif choice == "4":
        item_to_buy = shop_items[3]
    elif choice == "5":
        print()
        print("Your inventory:")
        for item in inventory:
            print(f"- {item}")
    elif choice == "6":
        print()
        print(f"Thanks for visiting, {player_name}!")
        print(f"You have {player_gold} gold left.")
        break

    if item_to_buy != "":
        if player_gold >= prices[item_to_buy]:
            player_gold -= prices[item_to_buy]
            inventory.append(item_to_buy)
            print()
            print(f"You bought a {item_to_buy}!")
            print(f"Remaining gold: {player_gold}")
        else:
            print()
            print("You don't have enough gold!")
