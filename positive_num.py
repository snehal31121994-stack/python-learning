def is_positive(number):
    if number > 0:
        print("Positive number")
        return True
    else:
        print("Not a positive number")
        return False

print(is_positive(5))
print(is_positive(-3))
print(is_positive(0))