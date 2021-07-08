def divideBy(num):
    try:
        return 42 / num
    except ZeroDivisionError:
        print("Cannot divide by Zero")
