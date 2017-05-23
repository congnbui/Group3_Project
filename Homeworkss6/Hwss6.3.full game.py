#pusher
#box
#destination
#map


#set pusher coordinate
#rep: P
pusher_x = 1
pusher_y = 0

#set box coordinate
#rep: B

boxes = [
    {"x" : 2,
     "y" : 1
     },
    {"x" : 1,
     "y" : 2
     },
    {"x" : 3,
     "y" : 5
     }
    ]

#set destination coordinate
#rep: D

dests = [
    {"x" : 3,
     "y" : 4
     },
    {"x" : 6,
     "y" : 7
     },
    {"x" : 0,
     "y" : 7
     }
    ]

#set map_size
size_x = 10
size_y = 10


def is_in_map(size_x, size_y, x, y):
    return 0 <= x <size_x and 0 <= y <size_y

def check_overlap(x, y, items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return True
    return False

def which_box(x, y, items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return item        

def print_map(size_x, size_y, pusher_x, pusher_y, boxes, dests):
    for y in range(size_y):
        for x in range(size_x):
            if x == pusher_x and y == pusher_y:
                print(" P ", end = "")
            elif check_overlap(x, y, boxes): # check x, y. if x and y are equal to any of the item in the list => print " B ". You don't even need " == True"
                print(" B ", end = "")
            elif check_overlap(x, y, dests):
                print(" D ", end = "")
            else:
                print(" - ", end = "")
        print()

print_map(size_x, size_y, pusher_x, pusher_y, boxes, dests)

def input_process(direction):
    dx = 0
    dy = 0
    if direction == "W":
        dy = -1
    elif direction == "A":
        dx = -1
    elif direction == "S":
        dy = 1
    elif direction == "D":
        dx = 1
    else:
        print("Please select the direction from W/A/S/D only!")
    return dx, dy # we dont need x, y as arguments of the function. 

def check_onvertex(size_x, size_y, x, y):
    if x * (x - size_x + 1)**2 + y * (y - size_y + 1)**2 ==0:
        return True
    return False

def check_samerow(y, items):
    for item in items:
        if y == item["y"]:
            return True
    return False

def check_samecol(x, items):
    for item in items:
        if x == item["x"]:
            return True
    return False
            
while True:

    direction = input("What is your next move? W/A/S/D: ").upper()
    dx, dy = input_process(direction)

    if check_overlap(pusher_x + dx, pusher_y + dy, boxes): # check if the box is right ahead of the pusher
        if check_overlap(pusher_x + 2*dx, pusher_y + 2*dy, boxes): #check if there is another box right behind the box being pushed)
            print("2 boxes at the same time?? You are not that strong bro ;)")
        else:
            if is_in_map(size_x, size_y, pusher_x + 2*dx, pusher_y + 2*dy): # check if the box will be pushed out of the map
                pusher_x += dx
                pusher_y += dy
                box = which_box(pusher_x, pusher_y, boxes)
                box["x"] += dx
                box["y"] += dy
            else:
                print("You can't push the box out of the map bro!!!")
    
    else: # if there is no box ahead of the pusher
        if is_in_map(size_x, size_y, pusher_x + dx, pusher_y + dy):
            pusher_x += dx
            pusher_y += dy
        else:
            print("You can't walk out of the map bro!!!")

    # check win/lose:
    check_win = 0
    for box in boxes:
        if check_overlap(box["x"], box["y"], dests):
            check_win +=1
    if check_win == len(boxes):
        print("CONGRATULATIONS!! You Dit It!!!!!!!!!!!!")
        break
    check_lose = 0        
    for box in boxes:
        if check_onvertex(size_x, size_y, box["x"], box["y"]):
            check_lose += 1
        elif box["x"] * (box["x"] - size_x + 1) == 0 and check_samecol(box["x"], dests) == False:
            check_lose += 1
        elif box["y"] * (box["y"] - size_y + 1) == 0 and check_samerow(box["y"], dests) == False:
            check_lose += 1
    if check_lose > 0:
        print_map(size_x, size_y, pusher_x, pusher_y, boxes, dests)
        print("You Lose Bro :( Better Luck Next Time!")
        break 
            
    print_map(size_x, size_y, pusher_x, pusher_y, boxes, dests)


        
    
    



