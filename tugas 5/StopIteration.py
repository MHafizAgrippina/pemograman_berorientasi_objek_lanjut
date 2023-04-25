numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
        if number == 4:
            raise StopIteration
    except StopIteration:
        break
