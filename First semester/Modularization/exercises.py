# Task 1
def listManipulation(alist, command="add", location="beginning", value=None):
    if command == "remove" and location == "end":
        removed = alist.pop()
        return removed
    elif command == "remove" and location == "beginning":
        removed = alist.pop(0)
        return removed
    elif command == "add" and location == "beginning":
        alist.insert(0, value)
        return alist
    elif command == "add" and location == "end":
        alist.append(value)
        return alist

print(listManipulation([1, 2, 3], value=20, location="end"))
print(listManipulation([1, 2, 3], "remove", "end"))
print(listManipulation([1, 2, 3], "remove", "beginning"))
print(listManipulation([1, 2, 3], "add", "beginning", 20))
print(listManipulation([1, 2, 3], "add", "end", 30))
print(listManipulation(alist=[1, 2, 3], value=20))

#############################################################################

# Task 2  Convert Seconds
def convertTime(sec):
    h = sec // 3600
    m = sec % 3600 // 60
    s = sec % 60
    return f"{h}h:{m}m:{s}s"

print(convertTime(1234))
print(convertTime(4567))

#############################################################################

#  Task 3  Censorship
def censor (string):
    words = string.split(" ")
    new_string = []
    for i in words:
        if len(i) > 4:
            new_string.append('*'*len(i))
        else:
            new_string.append(i)
    return " ".join(new_string)

print(censor("The code is fourty"))
print(censor("Two plus three is five"))
print(censor("aaaa aaaaa 1234 12345"))

#############################################################################

# Task 4  Supermarket

cart1 = ["milk", "sugar", "milk", "x3", "sugar", "beer", "x12", "bread", "milk", "butter", "x2", "salad", "x3", "juice",
         "sugar", "x2", "juice", "butter", "sugar", "flour"]
pricelist1 = {"milk": 1.3, "sugar": 1.6, "beer": 1.25, "bread": 2.6, "butter": 1.99, "salad": 0.89, "flour": 1.2,
              "juice": 1.2}

def bill(cart, pricelist):
    cart_list = []
    for i in range(len(cart) - 1):
        if cart[i].startswith("x"):
            continue
        elif cart[i].isalpha():
            if cart[i + 1].startswith("x"):
                cart_list += [(cart[i], int(cart[i + 1][1:]))]
            else:
                cart_list += [(cart[i], 1)]
    if not cart[-1].startswith('x'):
        cart_list += [(cart[-1], 1)]
    cart_dict = {}
    for i in cart_list:
        if i[0] not in cart_dict:
            cart_dict[i[0]] = i[1]
        else:
            cart_dict[i[0]] += i[1]
    print(cart_dict)
    bill_ = 0
    for a, b in cart_dict.items():
        bill_ += b * pricelist[a]
    print(bill_)

bill(cart1, pricelist1)
