my_list = [
    "mummy",
    "hannah",
    "murder for a jar of red rum",
    "mom",
    "seagull",
    "tomato",
    "no lemon",
    "no melon",
    "some men interpret nine memos",
    "madam"
]

for item in my_list:

    # Remove spaces
    # make lowercase

    cleaned_mylist = item.replace(" ", "").lower()

    reversedlist = cleaned_mylist[::-1]

    if cleaned_mylist == reversedlist:

        print(f'"{item}" is a palindrome')

    else:
        print(f'"{item}" is not a palindrome')