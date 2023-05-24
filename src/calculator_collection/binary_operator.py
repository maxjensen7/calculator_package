print("Welcome to my calculator.")
print("You may perform both unary an binary operations.")
print("Please type you operations in the following forms:")
print("Unary operator: - 7")
print("Binary operator: 4 + 7")
bop = input("Enter your binary operation: ")
bop_list = bop.split()
if len(bop_list) == 2:
    op = bop_list[0]
    x = int(bop_list[1])
    if op == "-":
        result = -x
        print(result)
elif len(bop_list) == 3: 
    x = bop_list[0]
    op = bop_list[1]
    y = bop_list[2]

    if op == "+":
        ans= int(x) + int(y)
        print(ans)
    elif op == "-":
        ans= int(x) - int(y)
        print(ans)
    elif op == "*":
        ans= int(x) * int(y)
        print(ans)
    elif op == "/":
        ans= int(x) / int(y)
        print(ans)
    elif op == "%":
        ans= int(x) % int(y)
        print(ans)
    elif op == ">":
        ans= int(x) > int(y)
        print(ans)
    elif op == "<":
        ans= int(x) < int(y)
        print(ans)
    elif op == "=":
        ans= int(x) == int(y)
        print(ans)
    else:
        print("Invalid Bop")


