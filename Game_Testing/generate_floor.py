import random
import rooms
import csv
#rooms = [room_name, Left, Right, Up, Down, *Has Spawned] *Might get rid of
x= 1
y = 1
current_location = x, y
check_location = x, y
rooms_generated = []
i = 2

def room_exists(x, y):
    for rooms in rooms_generated:
        if x == rooms_generated [rooms][6] & y == rooms_generated [rooms] [7]:
            return rooms
        else:
            continue

    
    while i > 0:
        room_selection = random.randint(0, len(rooms.list_of_all_rooms))
        j = 0
        exists = room_exists(x, y)
        while j < 1:
            #left
            if room_selection[1] == True:
                x -= 1
                if x == 0:
                    j += 1
                    continue
                elif len(rooms_generated) == 0:
                    #skip to top
                    continue
                elif exists != "none":
                    if rooms_generated[2] == False:
                        j += 1
                        continue
            #right
            elif room_selection[2] == True:
                x += 1
                if x == 0:
                    j += 1
                    continue
                elif len(rooms_generated) == 0:
                    #skip to top
                    continue
                elif exists != "none":
                    if rooms_generated[1] == False:
                        j += 1
                        continue
            #up
            elif room_selection[3] == True:
                y -= 1
                if y == 0:
                    j += 1
                    continue
                elif len(rooms_generated) == 0:
                    #skip to top
                    continue
                elif exists != "none":
                    if rooms_generated[4] == False:
                        j += 1
                        continue
            #down
            elif room_selection[4] == True:
                y += 1
                if y == 0:
                    j += 1
                    continue
                elif len(rooms_generated) == 0:
                    #skip to top
                    continue
                elif exists != "none":
                    if rooms_generated[3] == False:
                        j += 1
                        continue



#open csv
f = open("world_map.csv", "w", newline="")
#wipe csv
f.truncate()
floor_list = []
#spawn room_1 in the top left spot/record in floor_list
writer = csv.writer(f)
writer.write("room_1")
floor_list.append(rooms.room_1)
#Check where the the doors are
for i in range(len(rooms.room_1)):
    if rooms.room_1[i] == True:
        random_value = random.randint(len(rooms.list_of_all_rooms))
        if rooms.list_of_all_rooms[random_value][1] == True: #& Allows for spawn
                writer.write(rooms.list_of_all_rooms[random_value])
#Spawn one on one of the doors

    #Check to see if door has room spawned on the other side

    #Check for out of bounds

#Check for any other doors

#Repeat until all doors are done

#Go to second room in floor_list

#Check doors

#Spawn new room/record in floor_list

    #Check to see if door has room spawned on the other side

    #Check for out of bounds
