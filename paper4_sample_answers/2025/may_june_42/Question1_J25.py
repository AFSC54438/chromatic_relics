# ------------------------------------------------------------------------
# 1) (a)
Stack = []
TopOfStack = -1

for _ in range(20):
    Stack.append("-1")

# ------------------------------------------------------------------------
# 1) (b)
def Push(new_str):
    global Stack
    global TopOfStack

    if TopOfStack < 19:
        TopOfStack += 1
        Stack[TopOfStack] = new_str
        return 1
    else:
        return -1
    
# ------------------------------------------------------------------------
# 1) (c)
def Pop():
    global Stack
    global TopOfStack

    if TopOfStack == -1:
        return "-1"
    else:
        return_val = Stack[TopOfStack]
        TopOfStack -= 1
        return return_val
    
# ------------------------------------------------------------------------
# 1) (d)
def ReadData(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                push_val = Push(line.strip())
                if push_val == -1:
                    print("Stack full")
    except FileNotFoundError:
        print("File not found")

# ------------------------------------------------------------------------
# 1) (e)
def Calculate():
    total = int(Pop())
    operator = ""

    while operator != "-1": 
        operator = Pop()
        num = int(Pop())
        if operator == "+":
            total = total + num
        elif operator == "-":
            total = total - num
        elif operator == "*":
            total = total * num
        elif operator == "/":
            total = total/num
        elif operator == "^":
            total = total ** num

    return int(total)
    
# ------------------------------------------------------------------------
# 1) (f) (i)
get_file = input("Filename: ").strip()
ReadData(get_file)
print(f"Total: {Calculate()}")

# ------------------------------------------------------------------------
