numbers = [10, 20, 30, 40]
print(numbers[0])
print(numbers[3])
print(len(numbers))
numbers[0] = 100
print(numbers)
numbers.append(50)
print(numbers)
removed = numbers.remove(100)
print(removed)
last = numbers.pop()
print(last)
removed = numbers.remove(20)
print(numbers)