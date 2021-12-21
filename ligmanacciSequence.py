running = True
numA = 0
numB = 1
answer = 1
iterations = 0

val = input("Enter number of iterations: ")
while running == True:
    iterations += 1
    answer = numA + numB
    print(numA, numB, answer)
    numA = numB
    numB = answer
  
    if iterations == int(val):
        answer = numA + numB
        print(numA, numB, answer)
        running = False

# n! = n - 1 + n - 2 + .....