clothes = ["T-Shirt", "Sweater"]

loop = 0
while loop <10:

    func = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    func = func.upper()
    if func == "C":
        new_item = input("enter new item: ")
        clothes.append(new_item)
    elif func == "R":
        print("Our items: ", clothes)
    elif func == "U":
        position = int(input("Update position? "))
        if position < len(clothes) and position >= 0:
            new_item = input("New item: ")
            clothes[position] = new_item
        else:
            print("The position must be less than {0} and greater than or equal to 0".format(len(clothes)-1))
    elif func == "D":
        position = int(input("Delete position? "))
        if position < len(clothes) and position >= 0:
            clothes.pop(position)
        else:
            print("The position must be less than {0} and greater than or equal to 0".format(len(clothes)-1))   
    else:
        print("Your request is out of range")
        pass

    loop += 1
        
        
