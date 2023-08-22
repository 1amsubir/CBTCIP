
Player1 = input("Enter your name: ")
Player2 = input("Enter your name: ")
n = int(input("Enter the number of digits: "))


player1guess = 0
player2guess = 0

while True:

    print("*******************************************")
    num1 = int(input(f"\n{Player1} enter the number: "))
    num2 = int(input(f"\n{Player2} guess the number: "))

    if num2 == num1:
        print(f"\n{Player2} congratulations you've guessed the number in 1st try.")
        print("\nYou're a MASTERMIND!")
    else:
        while(num2 != num1):
            player2guess+=1
            digcount = 0

            num2 = str(num2)
            num1 = str(num1)

            correctdigit = ['X']*n

            for i in range(0,n):
                if(num1[i] == num2[i]):
                    digcount+=1
                    correctdigit[i] = num2[i]
                else:
                    continue

            if(digcount == 0):
                print("\nNot a single digit matched.")
                num2 = int(input(f"\n{Player2} please enter an another guess: "))
            elif digcount<n:
                print(f"\nYou've entered {digcount} correct digits: {correctdigit}")
                num2 = int(input(f"\n{Player2} please enter an another guess: "))
            else:
                break

    print("\n")
    print(f"{Player2} took {player2guess} guesses to guess the number correct.")
    break

while True:

    print("*******************************************")
    num1 = int(input(f"\n{Player2} enter the number: "))
    num2 = int(input(f"\n{Player1} guess the number: "))

    if num2 == num1:
        print(f"\n{Player1} congratulations you've guessed the number in 1st try.")
        print("\nYou're a MASTERMIND!")
    else:
        while (num2 != num1):
            player1guess += 1
            digcount = 0

            num2 = str(num2)
            num1 = str(num1)

            correctdigit = ['X'] * n

            for i in range(0, n):
                if (num1[i] == num2[i]):
                    digcount += 1
                    correctdigit[i] = num2[i]
                else:
                    continue

            if (digcount == 0):
                print("\nNot a single digit matched.")
                num2 = int(input(f"\n{Player1} please enter an another guess: "))
            elif digcount < n:
                print(f"\nYou've entered {digcount} correct digits: {correctdigit}")
                num2 = int(input(f"\n{Player1} please enter an another guess: "))
            else:
                break

    print("\n")
    print(f"{Player1} took {player1guess} guesses to guess the number correct.")
    break


if(player1guess > player2guess):
    print(f"{Player2} congratulations you're the MASTERMIND!")
elif(player1guess < player2guess):
    print(f"{Player1} congratulations you're the MASTERMIND!")
else:
    print(f"The Match is a Draw!")

