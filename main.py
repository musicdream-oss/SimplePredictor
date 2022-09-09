__authour__ = "ultra"
print("ꗥ～ꗥ█▀▄▀█ █▀█ █▀█ █▄░█ █▄▄ █░░ ▄▀█ █▀ ▀█▀ꗥ～ꗥ")
print("ꗥ～ꗥ█░▀░█ █▄█ █▄█ █░▀█ █▄█ █▄▄ █▀█ ▄█ ░█░ꗥ～ꗥ")
print("")
print("What mode do you want to use with Ultra Predictor")
print("Mines Predictors 85% = type Mines")
print("Roll predictor 60% = type Roll")

mode = input()
print("Loading, " + mode )
print(" ")
if mode == ("Mines"):
    print("mine 1")
    import random

    n = random.randint(0, 25)
    print(n)
    # which mine
    # there are 25 mines in total (number represents mine)

    print("mine 2")
    import random

    n = random.randint(0, 25)
    print(n)
    # which mine

    print("mine 3")
    import random

    n = random.randint(0, 25)
    print(n)
    # which mine

    print("mine 4")
    import random

    n = random.randint(0, 25)
    print(n)
    # which mine

    print("accuracy")
    import random

    acc_output = random.randint(0, 99)
    print(acc_output)
    # accuracy
    print("by numbers it means for example 4 would be first row 4th number, for example 19 would be the 4th row , 5 number")
    print("this is random gen")
else:
    print("1 stands for purp")
    print("2 stands for red")
    print(" ")
    import random
    roll = random.randint(1, 2)
    print(roll)
    print("This software is yet unable to predict, yelllow coller becuase it uses V.1.1 Algoritim")

