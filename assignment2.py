import time

list1 = []
list2 = []

# Populate list1
while True:
    item = input("Enter item for list1: ")
    list1.append(item)

    answer = input("Are you through? (yes/no): ")

    if answer.lower() == "yes":
        break

# Populate list2
while True:
    item = input("Enter item for list2: ")
    list2.append(item)

    answer = input("Are you through? (yes/no): ")

    if answer.lower() == "yes":
        break

# Compare lengths
if len(list1) != len(list2):
    print("Lengths of lists don't match.")
else:
    print("Lengths match.")
    time.sleep(1)

    print("Proceeding...")
    time.sleep(1)

    result = dict(zip(list1, list2))

    print(result)