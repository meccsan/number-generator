import random

def main():
    try:
        i = int(input("Give first number (for range): "))
        j = int(input("Give second number (for range): "))
        if i > j:           # If the user enters the first number
            i, j = j, i     # and the first number is smaller than second, swap them
    except ValueError:
        print("That's not a legal number")
        return

    randnum = random.randint(i, j)  # set the range of randnum to the values of i and j
    
    while True: # the main loop of guessing until randnum == usrguess
        usrguess = int(input(f"Guess a number between {i} and {j}: "))

        if usrguess < randnum:
            print("Go higher")
        elif usrguess > randnum:
            print("Go lower")
        else:
            print("That's right")
            break

# prevent importation errors
if __name__ == "__main__":
    main()