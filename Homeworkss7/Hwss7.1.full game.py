#pusher
#box
#destination
#map


#set pusher coordinate
#rep: P

pusher = {
    "x": 1,
    "y": 0
    }

##pusher_x = 1
##pusher_y = 0

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

size = {
    "x": 10,
    "y": 10
    }

##size_x = 10
##size_y = 10

#Reset
pusher1 = {"x": pusher["x"], "y": pusher["y"]}
boxes1 = [box.copy() for box in boxes]

def is_in_map(size, x, y):
    return 0 <= x <size["x"] and 0 <= y <size["y"]

##def check_overlap(x, y, items):
##    for item in items:
##        if x == item["x"] and y == item["y"]:
##            return True
##    return False

def check_overlap(x, y, items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return item
    return None

##def which_box(x, y, items):
##    for item in items:
##        if x == item["x"] and y == item["y"]:
##            return item        

def print_map(size, pusher, boxes, dests):
    for y in range(size["y"]):
        for x in range(size["x"]):
            if x == pusher["x"] and y == pusher["y"]:
                print(" P ", end = "")
            elif check_overlap(x, y, boxes): # check x, y. if x and y are equal to any of the item in the list => print " B ". You don't even need " == True"
                print(" B ", end = "")
            elif check_overlap(x, y, dests):
                print(" D ", end = "")
            else:
                print(" - ", end = "")
        print()

print_map(size, pusher, boxes, dests)

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
##    else:
##        print("Please select the direction from W/A/S/D only!")
    return dx, dy # we dont need x, y as arguments of the function. 

def check_onvertex(size, x, y):
    if x * (x - size["x"] + 1)**2 + y * (y - size["y"] + 1)**2 ==0:
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

def reset_game():
    return pusher1.copy(), boxes1.copy()
    

##def check_position(item, items):
##    items = items.remove(item)
##    if check_overlap(item["x"], item["y"], items) is not None:
##        return True
##    return False
    
while True:
##    all_of_them = [pusher] + boxes + dests
##    for item in all_of_them:
##        if check_position(item, all_of_them):
##            print("Please double check positions of the pusher, the boxes, and the destinations")
##            break

    undo_check = 0
    direction = input("What is your next move? W/A/S/D: \n Enter R to reset the game \n Enter U to undo the game \n").upper()
    
    if direction == "R":
        pusher, boxes = reset_game()
    
    dx, dy = input_process(direction)
    found_box = check_overlap(pusher["x"]+ dx, pusher["y"] + dy, boxes)
    if check_overlap(pusher["x"] + dx, pusher["y"] + dy, boxes) is not None: # check if the box is right ahead of the pusher
        if check_overlap(pusher["x"]+ 2*dx, pusher["y"] + 2*dy, boxes) is not None: #check if there is another box right behind the box being pushed)
            print("2 boxes at the same time?? You are not that strong bro ;)")
        else:
            if is_in_map(size, pusher["x"]+ 2*dx, pusher["y"] + 2*dy): # check if the box will be pushed out of the map
                pusher["x"] += dx
                pusher["y"] += dy
##                box = which_box(pusher_x, pusher_y, boxes)
##                box["x"] += dx
##                box["y"] += dy
                found_box["x"] += dx
                found_box["y"] += dy

                undo_check = 1
                
            else:
                print("You can't push the box out of the map bro!!!")
    
    else: # if there is no box ahead of the pusher
        if is_in_map(size, pusher["x"] + dx, pusher["y"] + dy):
            pusher["x"] += dx
            pusher["y"] += dy

            undo_check = 1
            
        else:
            print("You can't walk out of the map bro!!!")

    print_map(size, pusher, boxes, dests)
    
    # undo
    
    if undo_check == 1:
        undo = input("Wanna undo bro? (U/any key) ").upper()
        if undo == "U":
            pusher["x"]-= dx
            pusher["y"] -= dy
            if found_box is not None:
                found_box["x"] -= dx
                found_box["y"] -= dy
            print_map(size, pusher, boxes, dests)
        else:
            pass
        
    
    # check win:
    check_win = 0
    for box in boxes:
        if check_overlap(box["x"], box["y"], dests):
            check_win +=1
    if check_win == min(len(boxes), len(dests)):
        print("CONGRATULATIONS!! You Dit It!!!!!!!!!!!!")
        break




##    check_lose = 0        
##    for box in boxes:
##        if check_onvertex(size, box["x"], box["y"]):
##            check_lose += 1
##        elif box["x"] * (box["x"] - size["x"] + 1) == 0 and check_samecol(box["x"], dests) == False:
##            check_lose += 1
##        elif box["y"] * (box["y"] - size["y"] + 1) == 0 and check_samerow(box["y"], dests) == False:
##            check_lose += 1
##    if check_lose > 0:
##        print("You Lose Bro :( Better Luck Next Time!")
##        break 
##            
    



        
    
    



