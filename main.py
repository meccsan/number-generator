import random

def main():
    try:
        i = int(input("Give first number (for range): "))
        j = int(input("Give second number (for range): "))
        if i > j:
            i, j = j, i
    except ValueError:
        print("That's not a legal number")
        return

    randnum = random.randint(i, j)
    
    while True:
        usrguess = int(input(f"Guess a number between {i} and {j}: "))

        if usrguess < randnum:
            print("Go higher")
        elif usrguess > randnum:
            print("Go lower")
        else:
            print("That's right")
            break

if __name__ == "__main__":
    main()