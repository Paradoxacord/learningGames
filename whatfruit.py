import random
#numbersinlist = [1,2,3,4]
numlist = [1,2,3,4]
running = True
loops = 0

while running == True:
    loops += 1
    print("Loops =", loops)
    y = random.randint(0,30000)
    x = random.randint(0,30000)
    numA = x
    numB = y
    print(numA, numB)
    if numA == numB:
        running = False
    
