# -------------------------------------------------------------------
# 2) (a)
def ReadData():
    arr = []
    try:
        with open(input("Enter a file name: "), "r") as file:
            for line in file:
                arr.append(line.strip())
            return arr
    except FileNotFoundError:
        print("File not Found")
        return None


# -------------------------------------------------------------------
# 2) (b)
def SplitData(DataArray):
    red = []
    green = []
    blue = []
    orange = []
    yellow = []
    pink = []

    for i in DataArray:
        color_int, color = i.split(",")

        if color == "red":
            red.append(color_int)
        elif color == "green":
            green.append(color_int)
        elif color == "blue":
            blue.append(color_int)
        elif color == "orange":
            orange.append(color_int)
        elif color == "yellow":
            yellow.append(color_int)
        elif color == "pink":
            pink.append(color_int)

    # ---------------------------------------------------------------
    # 2) (d)
    StoreData(red, "Red.txt")
    StoreData(green, "Green.txt")
    StoreData(blue, "Blue.txt")
    StoreData(orange, "Orange.txt")
    StoreData(yellow, "Yellow.txt")
    StoreData(pink, "Pink.txt")

    # ---------------------------------------------------------------


# -------------------------------------------------------------------
# 2) (c)
def StoreData(DataToStore, filename):
    try:
        with open(filename, "a") as file:
            for _ in DataToStore:
                file.write(f"{_}\n")

    except FileNotFoundError:
        print("File not found")


# -------------------------------------------------------------------
# 2) (e) (i)
SplitData(ReadData())

# -------------------------------------------------------------------
