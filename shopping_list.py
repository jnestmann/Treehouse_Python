# 1. Run the script to start using it
# 2. Put new things into the list, one at a time
# 3. Enter the word DONE - in all caps - to quit the program
# 4. And, once I quit, I want the app to show me everything that's on my list

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def shopping_list_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see current list
Enter 'DEL' to remove an item
Enter 'SAVE' to save list
""")


def shopping_list_show(shopping_list):
    clear_screen()
    position = 1
    print("Your shopping list contains")
    for item in shopping_list:
        print("\t{} - {} ".format(position, item))
        position += 1


def shopping_list_add(shopping_list, new_item):
    shopping_list_show(shopping_list)
    if shopping_list:
        position = input("Where should I add {}?\n"
                         "Press ENTER to add to the end of the list.\n"
                         "> ".format(new_item))
    else:
        position = 0

    try:
        position =  abs(int(position))
    except ValueError:
        position = None

    if (position is not None) and position != 0:
        shopping_list.insert((position - 1), new_item)
    elif position == 0:
        shopping_list.insert(0, new_item)
    else:
        shopping_list.append(new_item)

    shopping_list_show(shopping_list)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))


def shopping_list_del(shopping_list):
    shopping_list_show(shopping_list)
    what_to_remove = input("What would you like to remove?\n>")

    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    shopping_list_show(shopping_list)









def shopping_list_save(shopping_list):
    try:
        f = open('shopping_list.txt', 'w')
    except OSError:
        print("Problem opening file.")
    else:
        try:
            f.write("Your shopping list contains\n")
            for item in shopping_list:
                message = "- " + item + "\n"
                f.write(message)
            f.close()
            shopping_list_show(shopping_list)
            print("{} items saved to file.".format(len(shopping_list)))
        except:
            print("Unable to write to file")


def main():
    shopping_list = []

    shopping_list_help()

    while(True):
        new_item = input("> ")
        if str.upper(new_item) == "DONE" or new_item.upper() == "QUIT":
            break
        elif str.upper(new_item) == "SHOW":
            shopping_list_show(shopping_list)
            continue
        elif str.upper(new_item) == "HELP":
            shopping_list_help()
            continue
        elif new_item.upper() == "DEL" or new_item.upper() == "DELETE":
            shopping_list_del(shopping_list)
            continue
        elif str.upper(new_item) == 'SAVE':
            shopping_list_save(shopping_list)
        else:
            shopping_list_add(shopping_list, new_item)
            continue

    shopping_list_show(shopping_list)


main()