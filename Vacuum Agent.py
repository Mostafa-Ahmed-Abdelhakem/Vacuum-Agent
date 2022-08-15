### Vacuum Agent ###

# import needed library
import random

def display(room):
    print(room)

# room is 4x4 matrix
room = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]

# start case
print("All rooms are dirty")
display(room)

#### random dirts ####
x = 0
y = 0

# nested loop for 2D matrix
while x < 4:
    while y < 4:
        room[x][y] = random.choice([0, 1])
        y += 1
    x += 1
    y = 0

# 1 --> Dirty room
# 0 --> clean room

print("Before cleaning rooms, i detect all of these random dirts")
display(room)

x = 0
y = 0
count = 0

while x < 4:
    while y < 4:
        if room[x][y] == 1:   # the location is dirty 
            print(f"vacuum in this location now {x}, {y}")
            room [x][y] = 0   # the location cleaned
            print(f"Location {x}, {y} cleaned")
            count += 1
        y += 1
    x += 1
    y = 0

# find the performance of our model
performance = (100 - ((count / 16) * 100))


print("All rooms cleaned ✔")
display(room)

print(f"Performance = {performance} %")