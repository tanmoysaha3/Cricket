import random


def batting(target):
    ball = 0
    run = 0
    wicket = 0
    while wicket < 2 and ball < 5:
        bowl = random.randint(1, 6)
        # print("Bowler : " + (str)(bowl))
        print("Batsman : ")
        bat = int(input())
        print("Bowler : " + str(bowl))
        ball += 1
        if bat == bowl:
            wicket += 1
            print("total wicket down : " + str(wicket))
            # continue
        else:
            run = run + bat
            print("total run " + str(run) + " at " + str(wicket) + " wicket")
        if run > target:
            break
    return run, wicket


def bowling(target):
    ball = 0
    run = 0
    wicket = 0
    while wicket < 2 and ball < 5:
        bat = random.randint(1, 6)
        # print("Batsman : " + (str)(bat))
        print("Bowler : ")
        bowl = int(input())
        print("Batsman : " + str(bat))
        ball += 1
        if bat == bowl:
            wicket += 1
            print("total wicket down : " + str(wicket))
            continue
        else:
            run = run + bat
            print("total run " + str(run) + " at " + str(wicket) + " wicket")
        if run > target:
            break
    return run, wicket


print('Toss Coin. Enter 0 or 1 :')
tossp = int(input())
tossc = random.randint(0, 1)
if tossp == tossc:
    print("Input your 0 for batting or 1 for bowling")
    twin = int(input())
    if twin == 0:
        (run1, wicket1) = batting(360)
        (run2, wicket2) = bowling(run1)
        if run2 > run1:
            print("win by " + str(10 - wicket2) + " wicket(s)")
        else:
            print("win by " + str(run1 - run2) + " run(s)")
    else:
        (run1, wicket1) = bowling(360)
        (run2, wicket2) = batting(run1)
        if run2 > run1:
            print("win by " + str(10 - wicket2) + " wicket(s)")
        else:
            print("win by " + str(run1 - run2) + " run(s)")

else:
    twin = random.randint(0, 1)
    if twin == 0:
        (run1, wicket1) = batting(360)
        (run2, wicket2) = bowling(run1)
        if run2 > run1:
            print("win by" + str(10 - wicket2))
        else:
            print("win by" + str(run1 - run2))
    else:
        (run1, wicket1) = bowling(360)
        (run2, wicket2) = batting(run1)
        if run2 > run1:
            print("win by" + str(10 - wicket2) + "wicket(s)")
        else:
            print("win by" + str(run1 - run2) + "run(s)")
