from random import randint

oddEven = False
running = True
score = 0
loops = 0

while running == True:
    randNum = randint(0, 1000)
    loops += 1
    print("Round: "+ str(loops))
    print("Is this number odd or even!?!: "+ str(randNum))
    if randNum % 2 == 0:
        oddEven = True
    else:
        oddEven = False

    val = input("Is number Even (Y/N)")
    if (val.lower() == "y" and oddEven) | (val.lower() == "n" and not oddEven):
        score += 1
        print("Good Job, your score is: " + str(score))        
    elif val.lower() == "esc":
        running = False
    else:
        print("dumb dummy, your score is: " + str(score))
