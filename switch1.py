ch=int(input("Enter any number in between 1 to 5:"))
match ch:
    case 1:
        print("One")
        print("C programming")
    case 2:
        print("Two")
        print("Cpp")
    case 3:
        print("Three")
        print("python")
    case 4:
        print("Four")
        print("Java")
    case 5:
        print("Five")
        print("ROR")
    case _:
        print("Invalid Choice")
