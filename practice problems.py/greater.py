#keep asking user for number until they enter the no greater than 100
while True:
    num = int(input("enter the number greater than 100: "))
    if num>100:
        print("i love you")
        break
    else:
        print("try again")
        #

        #secret word guess
        secret = "god"
        while True:
            guess = input("guess the secret word:")
            if guess.lower() == secret:
                print("correct")
                break
            else:
                print("wrong guess. Try again")

#no from 1 to 5 using loop
for i in range(1,10):
    print(i)
    