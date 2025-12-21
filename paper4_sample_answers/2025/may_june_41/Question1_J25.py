# -------------------------------------------------------------------
# 1) (a)
Queue = []

for i in range(20):
    Queue.append(-1)

HeadPointer = -1
TailPointer = -1
NumberItems = 0


# -------------------------------------------------------------------
# 1) (b)
def Enqueue(num):
    global HeadPointer
    global TailPointer
    global Queue
    global NumberItems

    if NumberItems == 20:
        return False
    elif NumberItems == 0:
        HeadPointer = 0
        TailPointer = 0

    else:
        TailPointer = (TailPointer + 1) % 20

    Queue[TailPointer] = num
    NumberItems += 1
    return True


# -------------------------------------------------------------------
# 1) (d)
def Dequeue():
    global HeadPointer
    global TailPointer
    global Queue
    global NumberItems

    if NumberItems == 0:
        return -1
    else:
        return_val = Queue[HeadPointer]
        HeadPointer = (HeadPointer + 1) % 20
        NumberItems -= 1

        if NumberItems == 0:
            HeadPointer = -1
            TailPointer = -1

        return return_val


# -------------------------------------------------------------------
# 1) (c)
for i in range(1, 26):
    Enqueue_result = Enqueue(i)

    if Enqueue_result == False:
        print(f"{i} Unsuccessful")
    else:
        print(f"{i} Successful")

# -------------------------------------------------------------------
# 1) (e) (i)
for _ in range(2):
    print(Dequeue())
# -------------------------------------------------------------------
