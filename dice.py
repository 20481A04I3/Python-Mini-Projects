import random
s1=0  #sum of player 1
s2=0  #sum of player 2
Target=100
i=0
while s1<Target and s2<Target:
    i+=1
    if i%2!=0:
        p1=random.randrange(1,50)
        s1+=p1
        print("Player1 rolls",p1)
        if s1>=Target:
            print("Player1 is the Winner")
            print("Player2 is the Loser")
    else:
        p2=random.randrange(1,50)
        s2+=p2
        print("Player2 rolls",p2)
        if s2>=Target:
            print("Player2 is the Winner")
            print("Player1 is the Loser")

