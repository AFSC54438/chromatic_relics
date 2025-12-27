# ------------------------------------------------------------------------------------------------
# 2) (a)
class NewRecord():
    def __init__(self, key, item1, item2):
        self.Key = key # Integer
        self.Item1 = item1 # Integer
        self.Item2 = item2 # Integer
    
# ------------------------------------------------------------------------------------------------
# 2) (b) (i)
HashTable = []
Spare = []

# ------------------------------------------------------------------------------------------------
# 2) (b) (ii)
def Initialise():
    global HashTable
    global Spare
    new_record = NewRecord(-1, -1, -1)
    for _ in range(200):
        HashTable.append(new_record)
    for _ in range(100):
        Spare.append(new_record)

# ------------------------------------------------------------------------------------------------
# 2) (c)
def CalculateHash(key):
    return key % 200

# ------------------------------------------------------------------------------------------------
# 2) (d)
def InsertIntoHash(new_record):
    global HashTable
    global Spare

    hash_address = CalculateHash(new_record.Key)

    check_record = HashTable[hash_address]

    if check_record.Key == -1 and check_record.Item1 == -1 and check_record.Item2 == -1:
        HashTable[hash_address] = new_record
    else:
        for i in range(100):
            check_spare = Spare[i]
            if check_spare.Key == -1 and check_spare.Item1 == -1 and check_spare.Item2 == -1:
                Spare[i] = new_record
                break

# ------------------------------------------------------------------------------------------------
# 2) (e)
def CreateHashTable():
    try:
        with open("HashData.txt", "r") as file:
            for line in file:
                line = line.strip()
                vals = line.split(",")
                InsertIntoHash(NewRecord(int(vals[0]), int(vals[1]), int(vals[2])))
    except FileNotFoundError:
        print("File not found")

# ------------------------------------------------------------------------------------------------
# 2) (f) (i)
def PrintSpare():
    for item in Spare:
        if item.Key == -1 and item.Item1 == -1 and item.Item2 == -1:
            break
        else:
            print(item.Key)

# ------------------------------------------------------------------------------------------------
# 2) (f) (ii)
Initialise()
CreateHashTable()
PrintSpare()
# ------------------------------------------------------------------------------------------------
