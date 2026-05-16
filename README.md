# Monty-Hall-Simulation
A simple python program that simulates the Monty Hall problem.

This simulation has a couple of conditions:
-The contestant will have a random first pick
-The contestant will always switch from the first pick
-Each run has 1000 rounds

# Randomizing the content of the 3 doors
The first step is to create a list where each door contains a number from 0 to 1. 0 being a goat (loss) and 1 being a car (win)

    doors=[random.randint(0,1),random.randint(0,1),random.randint(0,1)]
    
but this isn't enough on its own since there can be duplicate cars or no cars at all, which in the real Monty Hall problem does not happen.
The following logic fixes it by checking each door for a car and changing the rest to 0 if it indeed has a car, if none of them has a car
then it will forcefully assign a car to a random door.

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

# Picking and revealing
In the real Monty Hall problem the contestant picks a door first before reavling a door that contains a goat. The contestant then is given
a choice either to stay with their pick or switch to the other door. Here the first pick will be randomized and so will be the revealed door.
The logic is that the revealed door and the picked door cannot be the same and the revealed door cannot contain a car.

    pick = random.randint(0, 2)

    reveal = random.randint(0, 2)
    while reveal == pick or doors[reveal] == 1:
        reveal = random.randint(0, 2)
    del doors[reveal]

The next step is switching from the original pick to the other available door. This can be achieved by delcaring the switch as a second variable
(in this case selection) and defining it as follows:

    selection = doors[1 - (pick if pick < reveal else pick - 1)]

# Counting and output
if selection is =1 that means the program selected a door that contains 1 and the contestant won a round. else it picks a 0 and the contestant lost.

    if selection==1:
        wins+=1
    else:
        loss+=1

  The ratio is then presented as percentages and will be the output for the program.

    print("wins:",str(wins*100/1000)+"%","loss:",str(loss*100/1000)+"%")
# Results
In a sample of 1 Million rounds the contestant won 66.7123% of the time, as predicted in the Monty Hall problem. You can try a sample size as big as you want
But the results seem to always converge to 66.7%. Perhaps this can be used as emperical proof that the Monty Hall problem is correct, but im sure that has
been done many times.
<img width="1081" height="820" alt="{2FEED6CB-7663-4C7C-940E-6C1BF1A86AD0}" src="https://github.com/user-attachments/assets/c92a1688-1680-4de4-9f35-139dcfe4d7fe" />
