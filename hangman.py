import random

word_list = ("cat", "crime", "trial", "monkey", "piglet", "moral", "haunted", "exam", "mango", "okay", "pencil", "grey", "red", "blue", "white", "fan", "danger", "stranger", "wind", "truck", "curtain", "road", "bus", "bike", "sign", "man", "hotel", "bag", "black", "mother", "father", "son", "daughter", "phone", "mobile", "zebra", "lion", "kid", "toy", "lights", "monster", "cow", "drake", "smile", "bush", "legs", "hands", "fight", "chaos", "maths", "solve", "problem", "ignore", "match", "matrix", "date", "extend", "thumbs", "scream", "cream", "care", "way", "force", "dog", "key", "flipkart", "spotify", "chrome", "maps", "drive", "document", "files", "gmail")
word_list = list(word_list)

def get_displayed():
    display = []
    for i in range(len(word)):
        if i in guessed:
            display.append(word[i])
        else:
            display.append(" _")
    return "".join(display)


m = True
while m:
    x = 10
    word = random.choice(word_list)
    guessed = []
    while x > 0:
        guess = input("Enter an alphabet to enter the game:\n")[0]
        if guess in word:
            guessed.append(list(word).index(guess))
            print(f"correct, {x} turns left")
        else:
            x -= 1
            print(f"Incorrect, {x} turns left")
            if x == 0:
                print("You lost!!")
                print(word)
        print(get_displayed())
        if get_displayed().count("_") == 0:
            print("You win!!")
            break

    k = str(input("Do you want to continue (y/n):\n"))
    if k == "y":
        m = True
    else:
        m = False
        print("Thank you for playing!!")
