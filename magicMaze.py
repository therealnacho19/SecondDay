moves=0
fails=0
lives=3
lock=['S', 'S', 'N', 'W', 'E', 'S']
flag=True
lockRecord=0

while flag:
    play=input("You are in the magic maze. Which way (N,S,E,W) do you want to go?: ")
    moves +=1
    lockRecord +=1
    if moves <= (len(lock)-1):
        if play != lock[lockRecord - 1]:
            lockRecord=0
            fails+=1
            if (fails==5):
                lives -=1
                if (lives > 0):
                    flag=True
                    print("You lost one life! You still have" ,lives, "lives left.")
                else:
                    flag=False
                    print("You have run out of lives!")
                    break
            print("You are starting back from the beginning!")



    else:
        print("You have escaped the maze in" ,moves, "moves.")
        break








