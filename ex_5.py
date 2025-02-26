# ex_5.py

if __name__ == "__main__":
    """ x = 0
        for i in range(10):
            x += 0.1
        print(x)
        print(x == 1)
        print(x, "==", 10*0.1)
    """
    x = float(input("Type a float number:"))
    p = 0
    while ((2**p) * x) % 1 != 0:
        print(f"Remainder = {(2**p) * x - int((2**p) * x)}")
        p += 1
    print(f"The min p for converting x to int is {p}")

    # Convert to int
    num = int(x * (2**p))
    result = ""
    if num == 0:
        result = "0"
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    print(f"Above int is {result}")

    # Add the decimal point
    for i in range(p - len(result)):
        result = "0" + result
    result = result[0:-p] + "." + result[-p:]
    print(f"The binary representation of {x} is {result}")


