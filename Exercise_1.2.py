#In the second exercise the idea is to create a small grocery shopping list with the list datastructure. In short, create a program that allows the user to (1) add products to the list, (2) remove items and (3) print the list and quit.
#If the user adds something to the list, the program asks "What will be added?: " and saves it as the last item in the list. If the user decides to remove something, the program informs the user about how many items there are on the list (There are [number] items in the list.") and prompts the user for the removed item ("Which item is deleted?: "). If the user selects 0, the first item is removed. When the user quits, the final list is printed for the user "The following items remain in the list:" followed by the remaining items one per line. If the user selects anything outside the options, including when deleting items, the program responds "Incorrect selection.".

note = []
while True:

    try:
        userchoice = int(input("Would you like to \n(1)Add or \n(2)Remove items or\n(3)Quit?:"))
    except Exception:
        print("Incorrect input: Enter a number")

    if userchoice == 'end':
        break
    elif userchoice == 1:
        note.append(input("What will be added?: "))
    elif userchoice == 2:
        print("There are", len(note),"items in the list.")
        itemToDelete=int(input("Which item is deleted?: "))
        try:
            note.pop(itemToDelete)
        except Exception:
            print("Incorrect selection.")
    elif userchoice == 3:
        print("The following items remain in the list:")
        for i in note:
            print(i)
        break
    else:
        print("Incorrect selection.")
