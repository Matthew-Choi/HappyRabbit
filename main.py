import random
import time


def main():
    random.seed(time.time())
    option = random.randint(1, 3)

    # Turn on the corresponding LED
    if option == 1:
        print("Red")
    elif option == 2:
        print("Green")
    elif option == 3:
        print("Blue")

    # need code to timeout after x seconds
    # can be based off difficulty, or can utilize learning
    # github examples (may only work on pi but that is ok)
    # https://stackoverflow.com/questions/1335507/keyboard-input-with-timeout
    # https://gist.github.com/atupal/5865237

    choice = input()

    if(int(choice) == option):
        # activate servo control to release treat
        # send call to AWS to store data
        print("correct!")
    else:
        # Negative Feedback?
        print("incorrect!")


if __name__ == "__main__":
    main()