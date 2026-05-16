import random
wins=0
loss=0

for i in range(1000000):
    doors=[random.randint(0,1),random.randint(0,1),random.randint(0,1)]

    if doors[0]==1:
        doors[1]=0
        doors[2]=0
    elif doors[1]==1:
        doors[0]=0
        doors[2]=0
    elif doors[2]==1:
        doors[0]=0
        doors[1]=0
    else:
        doors[random.randint(0,2)]=1

    pick = random.randint(0, 2)

    reveal = random.randint(0, 2)
    while reveal == pick or doors[reveal] == 1:
        reveal = random.randint(0, 2)
    del doors[reveal]

    selection = doors[1 - (pick if pick < reveal else pick - 1)]

    if selection==1:
        wins+=1
    else:
        loss+=1

print("wins:",str(wins*100/1000000)+"%","loss:",str(loss*100/1000000)+"%")