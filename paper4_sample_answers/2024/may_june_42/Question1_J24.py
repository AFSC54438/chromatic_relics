WordArray = []
NumberWords = 0

# ---------------------------------------------------------------------------------------------
# 1) (c) (i)
def Play():
    global WordArray, NumberWords

    print(f"Main word: {WordArray[0]}")
    print(f"Number of answers: {NumberWords}")

    WordArray.pop(0)
    correct_answers = 0

    get_input = ""
    while get_input != "no":
        if correct_answers == NumberWords:
            print("You've gotten all the words")
            break

        get_input = input("Enter a word or 'no' to stop: ").lower().strip()
        if get_input in WordArray:
            correct_answers += 1
            print("You got a correct answer.")
            WordArray[WordArray.index(get_input)] = None
        elif get_input == "no":
            print(f"Score: {correct_answers}")
            # --------------------------------------------------------------------------
            # 1) (c) (ii)
            print(f"Percentage answered: {(correct_answers/NumberWords * 100):.2f}%")
            print("Other answers:")
            print("| ", end="")
            for item in WordArray:
                if item is not None:
                    print(f"{item}", end=" | ")
            print()
            # --------------------------------------------------------------------------
            break
        else:
            print("Not a valid answer")


# ---------------------------------------------------------------------------------------------
# 1) (a)
def ReadWords(file_name):
    global NumberWords, WordArray
    try:
        with open(file_name, "r") as file:
            for line in file:
                WordArray.append(line.strip())

        NumberWords = len(WordArray) - 1
    except FileNotFoundError:
        print("File not found")

    # ------------------
    # 1) (d) (i)
    Play()
    # ------------------

# ---------------------------------------------------------------------------------------------
# 1) (b)
get_input = input("Which file do you want to open (easy/medium/hard)? ").lower().strip()

while get_input not in ["easy", "medium", "hard"]:
    get_input = (
        input("Which file do you want to open (easy/medium/hard)? ").lower().strip()
    )

if get_input == "easy":
    ReadWords("Easy.txt")
elif get_input == "medium":
    ReadWords("Medium.txt")
else:
    ReadWords("Hard.txt")

# ---------------------------------------------------------------------------------------------
